class Mammal:

    __instance = None
    __count    = 0

    # Static Methods
    @staticmethod
    def get_instance():
        return Mammal.__instance

    def get_count(self):
        return Mammal.__count

    def __init__(self,mammal_type):
        self.mammal_type = mammal_type
        Mammal.__count += 1
        if Mammal.get_instance():
            Mammal.__instance = Mammal.get_instance()
        else:
            Mammal.__instance = self

    def type(self,mammal_type = None):
        if mammal_type:
            self.mammal_type = mammal_type
        return self.mammal_type



print(Mammal.get_instance())

m = Mammal("Cat")

print(Mammal.get_instance())

print(m.type())

print(m.type("Dog"))

print("m: " + str(m))
print("m type: " + m.type())
print("Obj Cnt: " + str(m.get_count()))

print()

m2 = Mammal("Le Tigra")

print("m2: " + str(m2))
print("m2 type: " + m2.type())
print("Obj Cnt: " + str(m2.get_count()))



del m
del m2



