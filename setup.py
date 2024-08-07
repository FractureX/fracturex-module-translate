from setuptools import setup, find_packages

setup(
    name="fracturex-module-translate",
    version="1.0.4",
    # aaaaaaaa
    packages=find_packages(),
    install_requires=[
        "pydantic==2.8.2",
        "googletrans==4.0.0rc1"
    ],
    author="FractureX",
    author_email="shaquille.montero.vergel123@example.com",
    description="Módulo de traducción",
    url="https://github.com/FractureX/fracturex-module-translate"
)