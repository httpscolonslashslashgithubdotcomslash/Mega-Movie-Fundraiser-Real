def integer_checker(question, low_num, high_num):
    error = f"Please enter an integer that is between {low_num} and {high_num}"
    valid = False
    while not valid:
        try:
            number_to_check = int(input(question))
            if low_num <= number_to_check <= high_num:
                return number_to_check
            else:
                print(error)
        except ValueError:
            print(
                "\nPlease enter an integer (ie a whole number - no decimals)")


age = integer_checker("\nPlease enter the age of the ticket holder: ", 12, 110)
print(f"Age = {age}")
