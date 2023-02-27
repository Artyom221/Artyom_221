class User():
    """Класс по созданию пользователей"""
    def __init__(self, login, password):
        """Инициализация атрибутов пользователя"""
        self.login = login
        self.password = password
        self.count = 0
    def log_in(self, log_in, pass_word):
        """Логин и счётчик логинов"""
        if self.login == log_in and self.password == pass_word:
            print('Добро пожаловать в аккаунт, ' + self.login.title())
            self.count = self.count + 1
        else:
            print('Вы неправильно ввели логин или пароль.')
    def unlogin(self, check):
        """Выход"""
        if check == 'Выйти':
            print('До свидания, ' + self.login.title())
    def print_count_of_logins(self):
        """Вывод счётчика логинов"""
        print(self.count)

class AdminRule():
    def __int__(self, privilege="King"):
        self.privilege = privilege
        print("Admin is a ", self.privilege)

class Admin(User):
    """administrar"""
    def __int__(self, log_in, pass_word):
        """admini atributner"""
        super().__init__(log_in, pass_word)
        self.privilege = AdminRule()

    def admin_rule(self):
        """admini iravunqner"""
        desc = self.login + self.password
        return desc.title()




user1 = User('Ivan', 12345)
user1.log_in('Ivan', 12345)
user1.unlogin('Выйти')
user1.log_in('Ivan', 12345)
user1.unlogin('Выйти')
user1.print_count_of_logins()
user2 = AdminRule()
user2.info