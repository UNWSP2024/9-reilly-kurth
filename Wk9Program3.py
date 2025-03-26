#reilly Kurth
#3/26/2025
#program #3

def calculate_total(filename):
    try:
        with open(filename, 'r') as file:
            total = 0
            for line in file:
                try:
                    number = int(line.strip())
                    total += number
                except ValueError:
                    print(f"Invalid data found and skipped: {line.strip()}")
            print(f"The total of all integers in '{filename}' is: {total}")
    except IOError:
        print(f"An error occurred when trying to read the file.")


def main():
    filename = "numbers.txt"
    calculate_total(filename)

if __name__ == "__main__":
    main()
