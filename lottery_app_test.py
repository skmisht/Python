### Building a simple lottery app ####
import random as rd

def lottery_main():
    #Ask player for numbers
    user_numbers = get_player_numbers()
    #Calculate lottery numbers
    lottery_numbers = create_lottery_numbers()
    #Print out the winning
    matched_numbers = user_numbers.intersection(lottery_numbers)
    print("You matched {}. you won ${}!".format(matched_numbers, 100**len(matched_numbers)))

# User can pick 6 numbers

def get_player_numbers():
    input_csv = input("Enter your 6 numbers, separated by commas: ")
    # Creating a set of integers from this number_csv
    number_list = input_csv.split(",")
    #int_set = [int(i) for i in input_csv.split(",")] #List comprehension
    int_set = {int(i) for i in number_list}
    return int_set

# Lottery calculates 6 random numbers (between 1 and 20)
def create_lottery_numbers():
    set_values = set() # empty set
    while len(set_values) < 6:
    # for index in range(6): # range in [0,1,2,3,4,5]
        set_values.add(rd.randint(1, 20))
    return set_values

lottery_main()





