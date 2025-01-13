# Austin Wiant - Assingment 1.2 - 1/11/2025
'''
Ask the user how many bottles of beer are on the wall.
Pass that input to a function that manages the countdown.
The function should take the input and count backwards to 1 while displaying the number of remaining bottles of beer on the wall.
Once the count is down to 1, change lyrics to show "1 bottle of beer..."
At the end of the countdown, get back to the main program and remind the user to buy more beer.

'''

def bottle_countdown(num_beer):
    for beer in range(num_beer, 0, -1):
        if beer > 1:
            print(f"\n{beer} bottle(s) of beer on the wall, {beer} bottle(s) of beer. ")
            print(f"\nTake one down, pass it around, {beer -1} bottle(s) of beer on the wall")
        else:
            print(f"\n1 last bottle of beer on the wall, 1 last bottle of beer. ")
            print("\nTake it down, pass it around, no more bottle(s) of beer on the wall!\n ")

def main():
    try:
        num_beer= int(input("How many bottles of beer do you have on the wall? "))
        if num_beer <= 0:
            print("Enter a postive number greater than zero")
        else:
            bottle_countdown(num_beer)
            print("Time to buy more beer!\n")
    except ValueError:
        print("Invalid input - Enter a valid number")

main()