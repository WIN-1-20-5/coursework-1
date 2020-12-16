import csv

class loginAndRegistr:

    def __init__(self):
        self.menu()
        self.userStatus = ''

    def menu(self):
        print("Добро пожаловать! Пожалуйста, войдите в ситему или зарегестрируйтесь.")
        print("1. Войти в систему")
        print("2. Зарегестрироваться")
        choice = input("Введите номер функции: ")
        if choice == "1":
            self.login()
        elif choice == "2":
            self.registration()
        else:
            print("К сожалению функции с таки номером нет.")

    def registration(self):
        print("Регистрация нового пользователя")
        status = True
        while status:
            name = input("Имя: ")
            password = input("Пароль: ")
            with open ("users.csv", "r", newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter = ",")
                count = 0
                next(reader)
                for i in reader:
                    if name == i[0]:
                        count += 1
                if count > 0:
                        print("Извините, это имя уже занято")
                else:
                    with open("users.csv", "a", newline='') as users:
                        writer = csv.writer(users)
                        writer.writerow([name, password, "user"])
                    status = False  
                    self.menu()  
    
    def login(self):
        print("Введите имя и пароль")
        status = True
        while status:
            message = ''
            name = input("Имя: ")
            password = input("Пароль: ")
            with open ("users.csv", "r", newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter = ",")
                next(reader)
                for i in reader:
                    if name == i[0] and password == i[1]:
                        message = 'Добро пожаловать, ' + name + '!'
                        self.userStatus = i[2]
                        status = False
                    else:
                        message = 'Имя или пароль неправильно введены. Повторите попытку.'
            print(message)