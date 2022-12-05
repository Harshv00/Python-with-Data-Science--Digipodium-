import random

class MyList(list): # inherits from list
    
    def shuffle(self):
        random.shuffle(self)

    def get_random(self):
        return random.choice(self)
    
#object

a = MyList([12, 121, 3, 12, 3, 54, 21, 22, 66])
a.sort()
print(a)
a.shuffle()
print(a)
print("random item from list = ",a.get_random())

