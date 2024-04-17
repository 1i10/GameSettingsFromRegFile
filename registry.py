import winreg

def readRegistryValue(key, path="", valueName=''):
    """
    Читает значение из реестра Windows.

    Parameters:
    - key (int): Ключ реестра, например, winreg.HKEY_LOCAL_MACHINE.
    - path (str): Путь к разделу реестра.
    - valueName (str): Наименование ключа.

    Returns:
    - str or None: Значение ключа или None в случае ошибки.
    """
    try:
        with winreg.OpenKeyEx(key, path) as regKey:
            value, _ = winreg.QueryValueEx(regKey, valueName)
        return value
    except Exception as e:
        print(f"Ошибка при чтении реестра: {e}")
        return None