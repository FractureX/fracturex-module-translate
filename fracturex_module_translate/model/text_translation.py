from pydantic import BaseModel

from fracturex_module_translate.model.language import Language

class Text_Translation(BaseModel):
    from_language: Language = Language.AUTO
    text: str
    to_language: Language
    text_dest: str
