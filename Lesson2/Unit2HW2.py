"""
Name: Aiden Pohl
Date: 3/6/2025
Description: Unit 2 HW 2
"""
class Restaurant:

    def __init__(self, restaurant_name: str, cuisine_type: str, number_served: int) -> None:
        '''
        Args:
            restaurant_name (str): Name of restaurant
            cuisine_type (str): Type of food
            number_served (int): Number of customers served
        
        '''
        
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    #Describes Restaurant
    def describe_restaurant(self) -> None:
        print(f"Welcome to {self.restaurant_name}. We specialize in {self.cuisine_type}.")
    
    #Says that a restaurant is open
    def open_restaurant(self) -> None:
        print(f"{self.restaurant_name} is now open!")
    
    #Sets the number of customers served to a specific number
    def set_number_served(self,customers) -> None:
        self.number_served = customers
    
    #A. Checks to make sure that you aren't trying to decrease the customer counter
    #B. Increments the customer counter by a certain amount
    def increment_number_served(self,more_customers) -> None:
        if more_customers >= 0:
            self.number_served += more_customers
        else:
            print("Stop trying to mess with the system, the customer counter only goes up")

class User:
    '''
        Args:
            first_name (str): First Name of User
            last_name (str): Last Name of User
            age (int): Age of User
            likes (str): Likes / Hobbies of User
            login_attempts (int): Login Attempts for User's account
        
        '''
    def __init__(self, first_name: str, last_name: str, age: int, likes: str, login_attempts: int) -> None:

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.likes = likes
        self.login_attempts = 0
    
    #Describes the traits of the User
    def describe_user(self) -> None:
        print(f"Name: {self.first_name} {self.last_name}, Age: {self.age}, Likes: {self.likes}")
    
    #Formally greets the User
    def greet_user(self) -> None:
        print(f"Hello {self.first_name} {self.last_name}. How are you?")

    #Increments the login attempts by a specific amount
    def increment_login_attempts(self,attempts) -> None:
        self.login_attempts += attempts
    
    #Resets the login attempts
    def reset_login_attempts(self) -> None:
        self.login_attempts = 0

#Main Function

def main():

    #Instances of Restaurant and User
    resturant = Restaurant("Chipotle", "Mexican Food", 0)
    user = User("Aiden", "Pohl", "15", "Drawing", 0)

    #Sets the number of served customers to 5
    print(f"{resturant.number_served}")
    resturant. number_served = 5
    print(f"{resturant.number_served}")

    #Sets the number of served customers to 9
    resturant.set_number_served(9)
    print(resturant.number_served)

    #Sets the number of served customers to 10
    resturant.set_number_served(10)
    print(resturant.number_served)

    #Increments the number of served customers by 25
    resturant.increment_number_served(25)
    print(resturant.number_served)

    #Tries to decrease the customer counter by 5, but gets a message saying you can't do that
    resturant.increment_number_served(-5)
    print(resturant.number_served)

    #Prints the final customer counter total
    print()

    #Increments the login attempts by 1
    user.increment_login_attempts(1)
    print(user.login_attempts)
    
    #Increments the login attempts by 4
    user.increment_login_attempts(4)
    print(user.login_attempts)

    #Resets the login attempts
    user.reset_login_attempts()
    print(user.login_attempts)



if __name__ == '__main__':
    main()