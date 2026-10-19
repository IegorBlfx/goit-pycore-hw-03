import random

def get_numbers_ticket(min : int, max : int, quantity : int):
    if min > 0 and quantity > 0 and 1000 >= max >= min and quantity <= (max - min + 1): # checking if the input values are valid
        lottery_numbers = random.sample(range(min, max + 1), quantity)
        lottery_numbers.sort() # sorting the generated lottery numbers in ascending order
        print(f"Your lottery numbers are: {lottery_numbers}") # printing the generated lottery numbers
        return lottery_numbers
    else:
        print("Invalid input values. Please ensure all parameters are positive integers and the quantity does not exceed the range.") # printing an error message if the input values are invalid
        return []
    

try:
    get_numbers_ticket(int(input("Enter the minimum number: ")), 
                       int(input("Enter the maximum number: ")), 
                       int(input("Enter the quantity of numbers to generate: "))) # calling the function with user input
except ValueError:
    print("Invalid input. Please enter valid integers.")