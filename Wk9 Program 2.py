#reilly kurth
#3/26/2025
#Wk9 Program2

import random

def write_random_numbers(filename,count):
    try:
        with open(filename,"w") as file:
            for _ in range(count):
                random_number = random.randint(1, 500)
                file.write(f"{random_number}\n")
        print(f"{count} random numbers were written in {filename}.")
    except:
        print(f'An error occurred')

def main():
    try:
        count = int(input("Enter the number of random numbers to generate (1-1000): "))
        if count < 1 or count > 1000:
            print("Please enter a valid number between 1 and 1000.")
            return
        filename = "random_numbers.txt"
        write_random_numbers(filename, count)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
