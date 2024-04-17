import os
import re

def getGamesPathsFromVdf(vdfPath):
    """
    Извлекает пути к папкам с играми из файла libraryfolders.vdf.

    Parameters:
    - vdfPath (str): Путь к файлу libraryfolders.vdf.

    Returns:
    - list: Список путей к папкам с играми.
    """
    try:
        with open(vdfPath, 'r') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return []

    paths = []
    for line in lines:
        if '"path"' in line:
            path = re.findall(r'"(.*?)"', line)[1] + r"/steamapps/common/"
            paths.append(path)

    return paths

def findGamePath(gameName, paths):
    """
    Находит путь к папке с указанной игрой.

    Parameters:
    - gameName (str): Название игры.
    - paths (list): Список путей к папкам с играми.

    Returns:
    - str or None: Путь к папке с игрой или None, если игра не найдена.
    """
    for path in paths:
        gamePath = os.path.join(path, gameName)
        if os.path.exists(gamePath):
            return gamePath
    return None