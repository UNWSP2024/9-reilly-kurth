#Reilly Kurth
#3/26/2025
#Program 1

def item_counter_file(filename):
    try:
        with open(filename,"r") as file:
            lines = file.readline()
            num_names = len(lines)
            print(f"The file {filename} contains {num_names} names.")
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except:
        print(f'An error occurred')

filename = "name.txt"
item_counter_file(filename)

