class Cellphone:
    def __init__(self, color="Space Grey", model = "iPhone 16", weight=250):
        self.color = color
        self.model = model
        self.weight = weight
    
    def __repr__(self):
        return f"This is a {self.color} {self.model} phone that weighs {self.weight} grams"
    
    def __eq__(self, other_phone):
        return self.color == other_phone.color and \
            self.model == other_phone.model and \
                self.weight == other_phone.weight
    
    def text(self,number,message):
        print(f"Sending {message} to {number}")

phone = Cellphone("blue","iPhone 16",250)
phone2 = Cellphone()
phone3 = Cellphone("blue","iPhone 16",250)

print(phone == phone2)
print(phone == phone3)
phone.text(5035758336, "Hello!")

test_list = [1,3,2,4]
#print(test_list.sort()) <- This would print none
test_list.sort()
print(test_list) # These sort it, then print the newly sorted lists.