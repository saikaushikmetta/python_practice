#create a class FoodItem with class attribute category="Snacks" and instance attribute("Samosa","GulabJamun")
class FoodItem:
    category="snacks"
    def __init__(self,food1,food2):
        self.food1=food1
        self.food2=food2
        print(self.food1,"\n",self.food2)
f1=FoodItem("samosa")
f2=FoodItem("GulabJamun")