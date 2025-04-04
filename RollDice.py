import random

class Die:
    def __init__(self,sides: int):
        self.sides = sides

    def roll_die(self):
        return(random.randint(1,self.sides))

    def roll_die_multiple(self):
        print(random.randint(1,self.sides))



def main():
    six_sides = Die(6)
    d10 = Die(10)
    d20 = Die(20)
    print(f"You rolled a {six_sides.roll_die()}")
    print("Rolling 10 dice...")
    for i in range(10):
        six_sides.roll_die_multiple()
    print(f"You rolled a {d10.roll_die()}")
    print(f"You rolled a {d20.roll_die()}")

if __name__ == '__main__':
    main()