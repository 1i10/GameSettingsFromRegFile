import gdown

def downloadFile(url, savePath):
    """
    Скачивает файл по указанному URL и сохраняет его по указанному пути.

    Parameters:
    - url (str): URL для скачивания файла.
    - savePath (str): Путь для сохранения скачанного файла.
    """
    try:
        gdown.download(url, savePath, quiet=False)
    except Exception as e:
        print(f"Ошибка при скачивании файла: {e}")