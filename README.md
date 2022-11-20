
 
<h1> Лабораторная работа №3 Вариант 27</h1>

> __Задание__: 

C помощью библиотеки Qt Designer реализовать следующие формы:
1. __Главная страница:__ Форма регистрации/авторизации. Обязательные поля:
username(или ФИО), password. Выводить результат криптографического преобразования в
файл.
2. __Страница «личного кабинета»:__ Допускается использования несколько форм или одной, но со всей функциональностью.   
    - Первая форма для ввода текстовой информации и дальнейшим шифрованием. Выводить результат криптографического преобразования в файл.
    - Вторая форма для ввода файла с зашифрованным содержимым, расшифровки и вывода на экран. Кнопка «Выйти».
3. __Экран выхода:__ Форма с неким текстом после выхода из личного кабинета и кнопкой перейти на главную страницу.

> Информация к файлам: 

1. В _"output"_ находиться .exe файл.
2. В _"Laba_3.py"_ находиться основной код
3. В _"HillCipher.py"_ находиться код шифрования и функции для доп. оптимизации. 

> Информация по алгоритму шифрованию:

Всю информацию по алгоритму шифрования можно найти здесь: [Матричное кодирование/ Шифр Хила](https://habr.com/ru/post/332714/)

> Недочет программы: 

При вводе текста с абзацами. В ответ получаешь тест в одну строку, т.е после шифрования все абзацы пропадают. 