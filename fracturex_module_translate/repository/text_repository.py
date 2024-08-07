from typing import List

from googletrans import Translator
from httpx import Timeout

from fracturex_module_translate.config.config import config_translate
from fracturex_module_translate.model.language import Language
from fracturex_module_translate.model.text_translation import Text_Translation

class Translate_Repository:

    __translator = Translator(timeout=Timeout(connect_timeout=10.00))
    __translated_texts: List[Text_Translation] = list()

    def __translate(self, *, from_language: Language = Language.AUTO, text: str, to_language: Language):
        returnValue: str = ""
        for translated_text in self.__translated_texts:
            if translated_text.text == text and translated_text.to_language == to_language:
                returnValue = translated_text.text_dest
                break
        if returnValue == "":
            returnValue = self.__translator.translate(text = text, dest = to_language.value, src = from_language.value).text
            self.__translated_texts.append(Text_Translation(text = text, to_language = to_language, text_dest = returnValue))
        return returnValue
    
    def translate(self, text: str) -> str:
        return self.__translate(text = text, to_language = config_translate.language)

    def translate_to_language(self, text: str, to_language: Language) -> str:
        return self.__translate(text = text, to_language = to_language)

    def translate_from_language_to_language(self, from_language: Language, text: str, to_language: Language) -> str:
        return self.__translate(from_language = from_language, text = text, to_language = to_language)
