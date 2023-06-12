"""
Elimina db.sqlite3 y todas las migraciones
"""

import os
import subprocess
from pathlib import Path


def buscar_py_migrations(carpeta_base: Path) -> list[str] | None:
    """Recorre recursivamente todas las sub-carpetas de la carpeta especificada y añade a la lista
    'resultado' los archivos .py que encuentra."""
    resultado = []

    for carpeta in carpeta_base.rglob("**"):
        if carpeta.is_dir() and carpeta.resolve().parts[-1] == "migrations":
            for elemento in carpeta.iterdir():
                if elemento.resolve().parts[-1] == "__init__.py":
                    continue
                if elemento.is_file() and elemento.suffix == ".py":
                    resultado.append(elemento)
                if elemento.resolve().parts[-1] == "__pycache__":
                    for i in elemento.iterdir():
                        if i.is_file() and i.suffix == ".pyc":
                            resultado.append(i)
    return resultado


def eliminar_archivos(archivos: list[str]) -> None:
    """Elimina los archivos .py de las subcarpetras migrations"""

    for archivo in archivos:
        print(f"\033[36m{archivo}\033[0m")
        os.remove(archivo)


def main() -> None:
    carpeta_base = Path(__file__).resolve().parent
    archivos = buscar_py_migrations(carpeta_base)
    try:
        os.remove("project/db.sqlite3")
    except:
        pass
    if archivos:
        print("*** Archivos eliminados ***")
        eliminar_archivos(archivos)
    else:
        print("No se encontraron archivos")


main()
