import datetime
import time


def Health_Management_System():
    """
    THIS IS A HEALTH MANAGEMENT SYSTEM. It's main  purpose is to track the health of a person.
    """
    try:

        def user_name_input():
            name = input("Enter your name: ")
            return name

        def current_time():
            # # Will return the current time on the system
            localTime = datetime.datetime.now()
            formatted_time = localTime.strftime("%a, %b %d, %Y %I:%M:%S")
            return formatted_time

        def pause(sec):
            # # Will pause the program for the input seconds
            return time.sleep(int(sec))

        def welcome_bot():
            # # Will print a welcome message to the user.
            print("Welcome to the Health Management System!")

        def path_chooser():
            print("[1] for dealing with food info!\n[2] for dealing with exercise info!")
            pause(1)
            user_input = input("Enter here: ")
            if user_input == "1":
                # FOOD SECTION
                print("What do you want to do?")
                pause(1)
                print("[1] Check your daily food intake.\n[2] Add what you ate today.")
                food_input = int(input("Enter here: "))

                if food_input == 1:
                    with open(f"Foods.{global_name}.txt") as file:
                        output = file.read()
                        print(output)

                elif food_input == 2:
                    user_ate = input("What did you eat?: ")
                    with open(f"Foods.{global_name}.txt", "a") as file:
                        file.write(
                            f"{global_name}, ate {user_ate}. Time: {current_time()}\n")
                else:
                    print(
                        "Something went wrong in the food section of path chooser function.")

            elif user_input == "2":
                # EXERCISE SECTION
                print("What do you want to do?")
                pause(1)
                print("[1] Check your daily exercise routine.\n[2] Add what you did today.")
                workout_input = int(input("Enter here: "))

                if workout_input == 1:
                    with open(f"Workouts.{global_name}.txt") as file:
                        output = file.read()
                        print(output)

                elif workout_input == 2:
                    workout_ = input("What did you do?: ")
                    with open(f"Workouts.{global_name}.txt", "a") as file:
                        file.write(f"{global_name}, did {workout_}. Time: {current_time()}\n")
                else:
                    print(
                        "Something went wrong in the food section of path chooser function.")
                pass
            else:
                print("Something went wrong in the main path chooser function!")

        def sign_in():

            # # Will do the sign in process.
            name = global_name
            with open("userdata.txt") as file:
                users = []
                for line in file:
                    # # Will extract the user's data from the database, and check if the user already exists.
                    users.append(line.strip())
                if name.lower() in users:
                    print(f"Welcome, back {name}!")
                    pause(1)
                    print("What would you like to do for today?")
                    pause(1)
                    # This function will redirect the program path to the path_chooser() function that will further decide the intent of the user at that time to use the system.
                    path_chooser()
                else:
                    print(f"Sorry, we couldn't find any user named {name}!")
                    print(f"Please either check your input, or sign up!")
                    pause(1)
                    print("Enter [1] to sign up!\nEnter [2] to sign in!")
                    user_intent = input("Enter here: ")
                    if user_intent == "1":  # SIGN UP
                        print("Please enter your name:")
                        user_name = input("Enter here: ")
                        if user_name.isalpha():
                            users.append(user_name)
                            print(
                                f"\nWelcome, {user_name}! You have successfully signed up.")
                        pass
                    elif user_intent == "2":  # SIGN IN
                        sign_in()
                    else:
                        pass

        welcome_bot()
        global_name = user_name_input()
        sign_in()

    # # Error handling
    except Exception as e:
        print("Something went wrong in the main function!")


if __name__ == "__main__":
    Health_Management_System()
