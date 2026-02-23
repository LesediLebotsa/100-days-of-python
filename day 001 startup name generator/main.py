# This is a start_up name generator
import random
print("Welcome to the custom start up name generator, please enter the details for your custom name.")
name = input("What is your name?\n")
industry = input("What industry are you in?(eg: Finance, Tech, Mining, etc)\n")
pet_name = input("What is the name of your pet?\n")
keywords = ("Growth" , ".Inc" , "Holdings", "Group")
startup_name1 = name + industry + random.choice(keywords)
startup_name2 = pet_name + industry + random.choice(keywords)
startup_name3 = name + pet_name + random.choice(keywords)
print("Your custom start up names are: ")
print(startup_name1)
print(startup_name2)
print(startup_name3)
