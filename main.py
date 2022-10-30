from shedule_class import FileShedule
from watchdog.observers import Observer
try:
    while True:
        print("Введите слово: ")
        true: bool = True
        word: str = input()
        if word.isalpha() and len(word) > 3:
            file = f"C:\\Users\\User\\PycharmProjects\\SystemProgramming-PR2\\test\\{word}.txt"
            with open (file, "w"):
                print("Файл успешно создан")
        else:
            print("Введите корректные данные!!!")
except Exception:
    print("Ошибка!!!")
except KeyboardInterrupt:
    print("Завершение работы")
