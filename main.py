import cat

mycat = cat.Cat()

while True:
    print("1 - покормить")
    print("2 - уложить спать")
    print("3 - мяукнуть")
    print("4 - климат")
    print("5 - выйти из программы")

    chois = input("Выбирите действие что вы хотите сделать с котом: ")
    if chois == "1":
        mycat.eat()

    elif chois == "2":
        mycat.sleep()

    elif chois == "3":
        mycat.meow()
