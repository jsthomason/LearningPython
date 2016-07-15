class Mammal:

    def __init__(self,mammal_type):
        self.mammal_type = mammal_type

    def type(self,mammal_type = None):
        if mammal_type:
            self.mammal_type = mammal_type
        return self.mammal_type



m = Mammal("Cat")

print(m)

print(m.type())

print(m.type("Dog"))

del m



