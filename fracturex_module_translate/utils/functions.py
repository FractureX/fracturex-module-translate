from fracturex_module_translate.config.config import config_translate
from fracturex_module_translate.repository.text_repository import (
    Translate_Repository
)
from fracturex_module_translate.model.language import Language

# Obtener repositorio de las traducciones
translate_repository: Translate_Repository = Translate_Repository()

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
    return translate_repository.translate(text = text)

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
    return translate_repository.translate_to_language(text = text, to_language = to_language)

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
    return translate_repository.translate_from_language_to_language(from_language = from_language, text = text, to_language = to_language)

def hola() -> None:
    pass
