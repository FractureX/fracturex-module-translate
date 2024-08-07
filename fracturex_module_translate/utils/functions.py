from httpx import Timeout
from googletrans.client import Translator

from fracturex_module_translate.config.config import config_translate
from fracturex_module_translate.repository.text_repository import translated_texts
from fracturex_module_translate.model.language import Language
from fracturex_module_translate.model.text_translation import Text_Translation

__translator = Translator(timeout=Timeout(connect_timeout=10.00))

def set_language(language: Language) -> None:
    """
    Método para establecer el lenguaje para la respuesta por parte del módulo de traducción
    
    Parameters
    ----------
    language: fracturex_module_translate.model.language.Language
        Lenguaje con el cual se devolverán las respuestas del módulo de traducción
    
    Returns
    -------
    None
    """
    config_translate.language = language

def __translate(*, from_language: Language = Language.AUTO, text: str, to_language: Language):
    returnValue: str = ""
    for translated_text in translated_texts:
        if translated_text.text == text and translated_text.to_language == to_language:
            returnValue = translated_text.text_dest
            break
    if returnValue == "":
        returnValue = __translator.translate(text = text, dest = to_language.value, src = from_language.value).text
        translated_texts.append(Text_Translation(text = text, to_language = to_language, text_dest = returnValue))
    return returnValue

def translate(text: str) -> str:
    """
    Método para retornar un texto traducido a otro idioma
    
    Parameters
    ----------
    text: str
        Texto a traducir al lenguaje configurado con fracturex_module_translate.utils.functions.set_language
    
    Returns
    -------
    None
    """
    return __translate(text = text, to_language = config_translate.language)

def translate_to_language(text: str, to_language: Language) -> str:
    """
    Método para retornar un texto traducido a otro idioma
    
    Parameters
    ----------
    text: str
        Texto a traducir
    to_language: fracturex_module_translate.model.language.Language
        Lenguaje al cual el texto se va a traducir
    
    Returns
    -------
    str
        Texto traducido
    """
    return __translate(text = text, to_language = to_language)

def translate_from_language_to_language(from_language: Language, text: str, to_language: Language) -> str:
    """
    Método para retornar un texto traducido a otro idioma
    
    Parameters
    ----------
    from_language: fracturex_module_translate.model.language.Language
        Lenguaje base del texto a traducir
    text: str
        Texto a traducir
    to_language: fracturex_module_translate.model.language.Language
        Lenguaje al cual el texto se va a traducir
    
    Returns
    -------
    str
        Texto traducido
    """
    return __translate(from_language = from_language, text = text, to_language = to_language)
