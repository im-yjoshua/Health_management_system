import datetime


def current_time():
    today = datetime.datetime.now()
    return today

class HealthManagementSystem:
    def __init__(self): 
        print("\n\t\t\tWelcome to the Health Management System!\n")
        self.name = input("Enter your name: ")

    def sign_in(self):
        with open('data/database.txt') as file:
            for line in file:
                if self.name in line:
                    return True
            print(f"Sorry, we couldn't find the name [{self.name}] in our database. Please, sign up!")
            return False

    def sign_up(self):
        if not self.sign_in():
            self.name = input("Enter your name: ")
            with open('data/database.txt', 'a') as file:
                file.write(f"{self.name}\n")
                return True
        print("Something went wrong in the [sign-up] method!")
        return False
        
    def proceeder(self):
        if self.sign_in() or self.sign_up():
            print("What do you want to do for today?")
            print("Enter [1] for dealing with food!\nEnter [2] for dealing with exercise!")
            self.what_to_do = int(input("Enter here: "))
            if self.what_to_do == 1:
                self.food_management()
            elif self.what_to_do == 2:
                self.exercise_management()
            else:
                print("Please enter a number!")
            return True
        else:
            print("Something went wrong in the [proceeder] method!")
            return False

    def food_management(self):
        print("What do you want to do for today?")
        print("Enter [1] to add what you ate today!\nEnter [2] to retrieve the data you've added so far!")
        self.what_to_do = int(input("Enter here: "))
        if self.what_to_do == 1:
            print("Okay, what did you eat today?")
            self.what_ate = input("Enter here: ")
            with open(f"{self.name}.food.txt", "a") as file:
                file.write(f"{self.name} ate {self.what_ate} at {current_time()}\n")
        elif self.what_to_do == 2:
            print("Okay, here's what you've added so far!")
            with open(f"{self.name}.food.txt", "r") as file:
                print(file.read())
        else:
            print("Please, enter a number!")
    
    def exercise_management(self):
        print("What do you want to do for today?")
        print("Enter [1] to add what exercise you did!\nEnter [2] to retrieve the data you've added so far!")
        self.what_exer = int(input("Enter here: "))
        if self.what_exer == 1:
            print("Okay, what did you do today?")
            self.what_exer = input("Enter here: ")
            with open(f"{self.name}.workout.txt", "a") as file:
                file.write(f"{self.name} did {self.what_exer} at {current_time()}\n")
        elif self.what_exer == 2:
            print("Okay, here's what you've added so far!")
            with open(f"{self.name}.workout.txt", "r") as file:
                print(file.read())
        else:
            print("Please, enter a number!")



if __name__ == "__main__":
    test = HealthManagementSystem()
    test.proceeder()
