class employee:
    
    def __init__(self):
        self.id = "abc122"
        self.salaray = 50000.0
        self.designation = "data scientist"
        
    def travel(self, destination):
        print("employee is now traveling to", destination)
    
sam = employee()
print(sam.id)
sam.travel("kerela")