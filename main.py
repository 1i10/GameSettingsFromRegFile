import os
import winreg
import time
from registry import readRegistryValue
from fileDownloader import downloadFile
from steam import getGamesPathsFromVdf, findGamePath
    

if __name__ == "__main__":
    gameName = "Goose Goose Duck"
    fileUrl = "https://drive.google.com/uc?export=download&id=1IGENwFzLm8bBEboISadYSNEdxbnjz1fH" #ссылка на reg файл игры

    registryPath = winreg.HKEY_LOCAL_MACHINE
    keyPaths = [
        r"SOFTWARE\Wow6432Node\Valve\Steam", # 64 бит
        r"SOFTWARE\Valve\Steam" # 32бит
    ]
    
    # Определяем, где установлен Steam
    steamPath = None
    for keyPath in keyPaths:
        steamPath = str(readRegistryValue(registryPath, keyPath, 'InstallPath'))
        if steamPath and os.path.exists(steamPath):
            break
    
    if steamPath:
        libraryFoldersFilePath = os.path.join(steamPath, "steamapps", "libraryfolders.vdf")
        gamePaths = getGamesPathsFromVdf(libraryFoldersFilePath)

        # Ищем путь к искомой игре
        gamePath = findGamePath(gameName, gamePaths)
        if gamePath:
            print(f"Путь к игре '{gameName}' найден: {gamePath}")

            settingsGameFilePath = os.path.join(gamePath, "settings.reg")
            downloadFile(fileUrl, settingsGameFilePath)
            
            # Вносим изменения в реестр windows
            if os.path.exists(settingsGameFilePath):
                try:
                    os.startfile(settingsGameFilePath)
                    print("Вносим изменения в реестр...")
                    time.sleep(5) # Пауза для внесения изменений в реестр
                except Exception as e:
                    print(f"Ошибка при внесении изменений в реестр: {e}")

            # Запускаем игру или steam
            exeGameFile = os.path.join(gamePath, f"{gameName}.exe")
            if os.path.exists(exeGameFile):
                try:
                    print("Запускаем игру...")
                    os.startfile(exeGameFile)
                except Exception as e:
                    print(f"Ошибка при запуске игры: {e}")
            else:
                try:
                    print("Запускаем Steam...")
                    os.startfile(os.path.join(steamPath, "steam.exe"))
                except Exception as e:
                    print(f"Ошибка при запуске Steam: {e}")

        else:
            print(f"Игра '{gameName}' не найдена.")
    else:
        print("Приложение Steam не найдено.")
