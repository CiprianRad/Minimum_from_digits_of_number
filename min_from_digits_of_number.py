def get_natural_input():
    while True:
        try:
            n = int(input("Please enter an integer: "))
            if n >= 0:
                return n
            else:
                return abs(n)
        except ValueError:
            print("Invalid input. Please enter a valid integer: ")


def min_number(n):
    number_list = list(str(n))  # We declare a list that will take as elements the digits of a given number in string format
    number_list.sort()  # We sort the list alphanumerically
    number_list = ''.join(number_list)  # We join the elements in the list so that they will take the number form
    return number_list


def main():
    n = get_natural_input()
    print("The minimum number that can be made usign the digits of the number given is: ", min_number(n))


main()
