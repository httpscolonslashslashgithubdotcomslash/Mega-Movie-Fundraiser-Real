error_message = "Please  enter 'Y' or 'N'"
valid_responses = ["y", "yes", "n", "no"]
response = input("Do you want snacks? ").lower()
while response not in valid_responses:
    print(error_message)
    response = input("Do you want snacks? ").lower()


if response == "n" or response == "no":
    print("Valid answer. you don't want snacks")
else:
    print("Valid answer. You do want snacks")
