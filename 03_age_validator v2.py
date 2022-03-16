def number_checker(text):
    valid = False
    while not valid:
        try:
            number_to_check = int(input(text))
            if isinstance(number_to_check, int):
                valid - True
                return number_to_check
        except ValueError:
            print(
                "\nPlease enter an integer (ie a whole number - no decimals)")


age = number_checker("Please enter the age of the ticket holder: ")
while not 12 <= age <= 110:
    age = number_checker("\nPlease enter an integer between 12 and 110: ")
print(f"Age = {age}")
