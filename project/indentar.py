"""
Este script indenta todos los archivos HTML de un proyecto teniendo en cuenta las etiquetas Django
"""

import subprocess
from pathlib import Path


def buscar_html(carpeta_base: Path) -> list[str] | None:
    """Recorre recursivamente todas las sub-carpetas de la carpeta especificada y añade a la lista
    'resultado' los archivos HTML que encuentra."""
    resultado = []

    for carpeta in carpeta_base.rglob("**"):
        if carpeta.is_dir():
            for elemento in carpeta.iterdir():
                if elemento.is_file() and elemento.suffix == ".html":
                    resultado.append(elemento)
    return resultado


def aplicar_formato_djhtml(archivos: list[str]) -> None:
    """Aplica el formato de Django a una lista de archivos HTML."""

    for archivo in archivos:
        print(f"\033[36m{archivo}\033[0m")
        subprocess.call(["djhtml", archivo])


def main() -> None:
    carpeta_base = Path(__file__).resolve().parent
    archivos = buscar_html(carpeta_base)
    if archivos:
        aplicar_formato_djhtml(archivos)
    else:
        print("No se encontraron archivos")


main()
