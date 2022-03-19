
class Hello:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def say(self):
        print("Hello,", self.name)
        print("You are {} years old".format(self.age))
