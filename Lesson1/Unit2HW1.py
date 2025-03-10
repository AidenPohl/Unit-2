"""
Name: Aiden Pohl
Date: 3/6/2025
Description: Unit 2 HW 1
"""

# Classes go here
class Restaurant:

    def __init__(self, restaurant_name: str, cuisine_type: str) -> None:

        '''Args:
            restaurant_name (str): Name of restaurant
            cuisine_type (str): Type of food
        """
        '''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    #Describes Restaurant
    def describe_restaurant(self) -> None:
        print(f"Welcome to {self.restaurant_name}. We specialize in {self.cuisine_type}.")
    
    #Says that a restaurant is open
    def open_restaurant(self) -> None:
        print(f"{self.restaurant_name} is now open!")
class User:

    def __init__(self, first_name: str, last_name: str, age: int, likes: str) -> None:

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.likes = likes
    
    #Prints full description of a user
    def describe_user(self) -> None:
        print(f"Name: {self.first_name} {self.last_name}, Age: {self.age}, Likes: {self.likes}")
    
    #Prints a greeting towards the user
    def greet_user(self) -> None:
        print(f"Hello {self.first_name} {self.last_name}. How are you?")

        





# main function

def main():

    #Restaurant (Name, Specialty)
    restaurant = Restaurant("Chipotle", "Mexican Food")
    restaurant2 = Restaurant("Panda Express", "Chineese Food")
    restaurant3 = Restaurant("Starbucks", "Coffee")
    print(f"{restaurant.restaurant_name}")
    print(f"{restaurant.cuisine_type}")

    #Describing all 3 and opening the first one, Chipotle
    restaurant.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()
    restaurant.open_restaurant()
    
    #User Instances (First Name, Last Name, Age, Likes)
    user1 = User("Aiden", "Pohl", 15, "Drawing")
    user2 = User("Jackson", "Sheahan", 14, "Gaming")
    user3 = User("Jack", "Gertenrich", 20, "Lifting Weights")

    #Describing all 3 Users
    user1.describe_user()
    user2.describe_user()
    user3.describe_user()

    #Greeting all 3 Users
    user1.greet_user()
    user2.greet_user()
    user3.greet_user()

if __name__ == '__main__':
    main()