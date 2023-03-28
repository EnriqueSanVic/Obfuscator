import os


def isStrEmpty(string: str) -> bool:
    return len(string) == 0 or string.count(' ') == len(string)


def extractPathExtension(ruta):
    _, extension = os.path.splitext(ruta)
    return extension
