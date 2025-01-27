# Austin Wiant - Assingment 4.2 - 1/26/2025

# Import libraries
import csv
from datetime import datetime
from matplotlib import pyplot as plt

# Open CSV file from file path
filename = '/Users/austinwiant/Downloads/sitka_weather_2018_simple.csv' 

# Open CSV file and contents
with open(filename) as f:
    reader = csv.reader(f) # Creates a CSV reader object
    header_row = next(reader)

    # Get dates and high temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        low = int(row[6])
        # appends high and low temperatures into their lists   
        highs.append(high)
        lows.append(low)

def plot_data(dates, temps, title, color): # Arguments for dates, temperature, title, color
    plt.figure(figsize=(10, 6)) # sets figure size
    plt.plot(dates, temps, c=color) # plot data with specified color
    plt.title(title, fontsize=20) # set title of plot
    plt.xlabel('Date', fontsize=14) # label x-axis
    plt.ylabel('Temperature (F)', fontsize=14) # label y-axis
    plt.grid() 
    plt.tight_layout()
    plt.show()

# Display menu for high temps, low temps, or to exit program
while True:
    print("\nMenu:")
    print("1. View Highs")
    print("2. View Lows")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    # User's choices 
    if choice == '1':
        plot_data(dates, highs, "High Temperatures - 2018", 'red') # plots high temps
    elif choice == '2':
        plot_data(dates, lows, "Low Temperatures - 2018", 'blue') # plots low temps
    elif choice == '3': # exits program
        print("Thank you for using the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
