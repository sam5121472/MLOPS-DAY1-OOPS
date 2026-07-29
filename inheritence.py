class animal:
    
    def __init__(self, name):
        self.name = name
        
    
        
    def sound(self):
        print(self.name, "makes a sound")
        
a1 = animal("dog")
print(a1.name)
        
    
class dog(animal):
    
    def __init__(self, name):
        super().__init__(name)
        self.behaviour = "friendly"
    
    def sound(self):
        print(self.name, "can bark, he is very ", self.behaviour)
        
d1 = dog("banno")
d1.sound()