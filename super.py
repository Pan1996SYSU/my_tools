class Parent1:

    def __init__(self, param1):
        self.param1 = param1
        print("Initializing Parent1 with param1 =", self.param1)


class Parent2:

    def __init__(self, param2):
        self.param2 = param2
        print("Initializing Parent2 with param2 =", self.param2)


class Child(Parent1, Parent2):

    def __init__(self, param1, param2):
        Parent1.__init__(self, param1)
        Parent2.__init__(self, param2)
        print("Initializing Child")


child = Child("value1", "value2")
