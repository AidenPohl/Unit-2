from Unit2HW2 import Restaurant
from Unit2HW2 import User
class IceCreamStand(Restaurant):
    def __init__(self, flavors:str):
        self.flavors = flavors

    def list_flavors(self):
        return f"The flavors we have today are {self.flavors[0]}, {self.flavors[1]}, and {self.flavors[2]}"
    

Menchies = IceCreamStand(["Chocolate","Vanilla","Strawberry"])
print(Menchies.list_flavors())

class Privillages():
    
    def __init__(self, privillages: list):

        self.privillages = privillages


    def show_privillages(self):
        return self.privillages

class Admin(User):
    
    def __init__(self, first_name, last_name, age, likes, login_attempts, privillages):

        self.privillages = privillages

    def __str__(self):
        return f"{', '.join(self.privillages)}"

    
Administrator = Admin('Big','Man',27,'Serving Justice',0,['Can add post','Can delete post','Can ban user'])
Other_Admin = Admin('Small','Man',19,'Kindly telling people to stop',0,['Can add post',"can delete post"])
print(Administrator)
print(Other_Admin)