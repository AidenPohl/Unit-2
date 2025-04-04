import random

random_num = [5,15,16,20,9,"A","I","D","E","N",39,60,16,45,39]


def random_choice():
    return random.choice(random_num)

def main():
    print("The winning numbers/letters are...")
    for i in range (4):
        print(random_choice())
if __name__ == '__main__':
    main()