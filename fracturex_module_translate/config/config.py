from pydantic import BaseModel

from fracturex_module_translate.model.language import Language

class Config(BaseModel):
    language : Language = Language.SPANISH

config_translate : Config = Config()
# AAAAAAAAAAaaa
# asdasdasdfsdfa
# si tuviera aaaaaaassdasdfasdasd