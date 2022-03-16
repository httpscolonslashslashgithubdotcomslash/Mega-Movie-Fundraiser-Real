def number_checker(question):
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print("\nPlease enter an integer(ie a whole number with "
                  "no decimals")


AGE_RANGE = range(12, 111)
age = number_checker("Please enter the age of the ticket holder: ")
while age not in AGE_RANGE:
    age = number_checker("\nPlease enter an integer between 12 and 110: ")

print(f"Age = {age}")