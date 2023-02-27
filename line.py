class Cylinder():
    def __init__(self, height, radius):
        self.height = height
        self.radius = radius

    def volume(self,):
        return self.height*3.14*(self.radius)**2


    def surface_arena(self):
        top = 3.14 * (self.radius)**2
        return (2*top) + (2*3*self.radius*self.height)


cyl = Cylinder(20, 34)
print(cyl.volume())
print(cyl.surface_arena())





