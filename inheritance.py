class animal:
    def sound(self):
        print("animal makes sound")
class dog(animal):
    def sound1(self):
        print("dog barks!!")
d=dog()#object of child
d.sound()#parent method becuase it has inherited from animal 
d.sound1()#child method