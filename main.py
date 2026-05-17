print("Hello worl1232123d")
privet="Hello world"
name=input("Введите имя")
print(privet, name)
import random


class APIConnection:
    def __init__(self, retries=5):
        self.retries = retries
        self.success = False

    def __enter__(self):
        for i in range(self.retries):
            x = random.randint(1, 3)

            if x == 1:
                print("ok")
                self.success = True
                return self
            else:
                print("fail")

        raise Exception("Не удалось подключиться после нескольких попыток")

    def __exit__(self, exc_type, exc_value, traceback):
        if self.success:
            print("Соединение закрыто")

        if exc_type:
            print(f"Ошибка: {exc_value}")

        return False

    print("Hello World")
