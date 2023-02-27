class Restaraunt():
    """restoran"""
    def __init__(self, tolma, xorovac, xash, jermuk, bjni):
        """menu"""
        self.tolma = tolma
        self.xorovac = xorovac
        self.xash = xash
        self.jermuk = jermuk
        self.bjni = bjni
        self.job_time = 8
        self.table = 22

    def menu(self):
        """inch ka nerka pahin"""
        print('nerka pahin ka ameninch')



    def place(self):
        """nstatexer"""
        print('Tvyal pahin azat en ' + str(self.table) + ' sexan')

    def work_time(self):
        """"ashxatanqi jamer"""
        self.job_time = self.job_time - 1
        print('Asxhatanqi avartin mnacel e ' + str(self.job_time) + ' jam')


    def employees(self, asxhatoxner=20):
        """ashxatoxneri qanaq"""
        print('Restoranum ashxatum en', asxhatoxner, 'hogi')

van = Restaraunt(3000, 4000, 5000, 500, 400)
van.employees()
van.place()
van.work_time()
van.menu()

class Kalyan():
    """kalyani acux"""
    def __int__(self, acux="Serbetli, AlPhaker, Adalya"):
        self.acux = acux


class VipKalyan(Restaraunt):
    """kalyani ankyun restorani mej"""
    def __int__(self, tolma, xorovac, xash, jermuk, bjni):
        super.__init__(tolma, xorovac, xash, jermuk, bjni)
        self.acux = Kalyan()

    def patver(self, sort="AlPhaker"):
        self.acux = sort
        print('Duq patvirel eq ', self.acux)

kalyan = VipKalyan(3000, 4000, 5000, 500, 400)
kalyan.patver()




