## Навигация
+ [Краткое описание](#краткое-описание)
+ [Структура репозитория](#структура-репозитория)
+ [Предварительные настройки и запуск](#предварительные-настройки-и-запуск-скрипта)
+ [Пример](#пример)


## Краткое описание

Проект был разработан на языке Python 3.9 в среде Microsoft Visual Studio Code под ОС Windows.  
Данный пакет скриптов позволяет пользователю изменить настройки игры Goose Goose Duck в Steam через .reg файл, который хранится в Google Drive.  
  
Скрипт отрабатывает по следующему сценарию:  
1. Определяется расположение Steam через реестр Windows ([Подробнее о расположении игр Steam](https://github.com/NPBruce/valkyrie/issues/1056));  
2. Далее, с помощью файла libraryfolders.vdf определяется возможное расположение искомой игры;
3. Скачиваем .reg файл по ссылке и сохраняем в директорию игры; 
4. Вносим значения из файла в реестр;
5. Пытаемся запустить игру (если исполняемый файл находится на верхнем уровне директории и соотвествует названию игры). В ином случае запускаем Steam.

## Структура репозитория

* [*main.py*](https://github.com/1i10/GameSettingsFromRegFile/blob/main/main.py) - Основной файл программы, который координирует все операции, включая чтение реестра, поиск игры и скачивание файла настроек. (Там же можно изменить название игры и ссылку к .reg файлу);  

* [*registry.py*](https://github.com/1i10/GameSettingsFromRegFile/blob/main/registry.py) - Модуль, содержащий функции для работы с реестром Windows. Он используется для чтения значений из реестра;  

* [*steam.py*](https://github.com/1i10/GameSettingsFromRegFile/blob/main/steam.py) - Модуль, содержащий функции для работы с клиентом Steam. Он используется для получения путей к играм и поиска конкретной игры;  
* [*fileDownloader.py*](https://github.com/1i10/GameSettingsFromRegFile/blob/main/fileDownloader.py) - Модуль, содержащий функцию для скачивания файла из облачного хранилища и сохранения его в указанном месте.    
 
*Методы задокументированы в самом коде с использованием docstrings*

## Предварительные настройки и запуск скрипта

Загрузите проект на локальную машину, воспользовавшись командой *git clone*.    

Для успешного запуска скрипта, выполните следующие шаги:

**1. Зависимости:**  
Убедитесь, что на вашей системе установлен Python 3.x и следующие библиотеки:

* gdown
* winreg
  
**2. Запуск скрипта**  
После установки зависимостей выполните следующие действия:

Запустите исполняемый скрипт main.py с помощью Python.
Например, через командную строку:
> python main.py 
  
## Пример

**Пример выполнения в командной строке:**  
![Пример1](https://github.com/1i10/GameSettingsFromRegFile/blob/main/example.png)  
  
