class computer:

    wheels = 5     # class variable     To access class variable we need
    brand = "macbook pro"

    def __init__(self, cpu, ram):

        self.ram = ram  # Instance variable
        self.cpu = cpu

    def config(self):
        print("config is", self.cpu, "&", self.ram)

    def compare(self, other_object):

        if self.cpu == other_object.cpu:
            return True
        else:
            return False

    @classmethod
    def class_info(cls):
        return computer.brand


com1 = computer("i5", 8)
com2 = computer('i7', 5)

computer.wheels = 7
# print(computer.wheels)


com1.ram = 9


# print(id(com1))  # Memory of Com1 is stored in Heap where heap store all the objects


if com1.compare(com2):
    print("They are same")
else:
    print("They are not same")


print(computer.class_info())

# print(type(com1))


# This is how we call the method of a class in python where com1 is the  object a class we are calling the com1 object
# computer.config(com1)


com1.config()  # This is how we use the code in real world where com1 is an object of computer calling its method will make the object com1 to pass into the method


# a = 5
# a.bit_length()


# print("Shanaar")


# Topics


# Type of Vaiable 1) Class/Static Variable 2)Instance Variable
# Type of Methos 1) Instance Methos 2) Class  method 3) Static Method
