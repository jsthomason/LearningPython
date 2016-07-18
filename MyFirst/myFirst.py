class Mammal:

    __instance = None

    # Static Methods
    @staticmethod
    def getInstance():
        return Mammal.__instance

    def __init__(self,mammal_type):
        self.mammal_type = mammal_type
        Mammal.__instance = self

    def type(self,mammal_type = None):
        if mammal_type:
            self.mammal_type = mammal_type
        return self.mammal_type



m = Mammal("Cat")

print(Mammal.getInstance())

print(m)

print(m.type())

print(m.type("Dog"))

del m



