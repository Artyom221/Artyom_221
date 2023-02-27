class Site():
    """sayti class"""

    def __init__(self, login, password):
        """atributner"""
        self.login = login
        self.password = password
        self.count = 0

    def mutq(self, log_in, pass_word):
        """"mutqeri qanaq"""
        if self.login == log_in and self.password == pass_word:
            print('Welcome in account ' + self.login.title())
            self.count = self.count + 1
        else:
            print('Login or pssword error')

    def elq(self, exit):
        """elq"""
        if exit == "Durs gal":
            print('hajoxutyun ' + self.login.title())

    def calc(self):
        """mutqeri hashvich"""
        print(self.count)

class AdminRule():
    def __int__(self, privilege="King"):
        self.privilege = privilege

    def info(self):
        """admini iravunqner"""
        print("Admin is a " + self.privilege)

class Admin(Site):
    """administrar"""
    def __int__(self, login, password):
        """admini atributner"""
        super().__init__(login, password)
        self.privilege = AdminRule()
        print('Admin is a ', self.privilege )




user1 = AdminRule()
user1.info()
















