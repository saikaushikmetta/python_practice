class student:
    def __init__(self,vehicle):
        self.vehicle=vehicle
        print(self.vehicle)
    def display(self):
        print("The vehicle name is:Alto k10")
#creating object
s=student("alto k10")
s.display()