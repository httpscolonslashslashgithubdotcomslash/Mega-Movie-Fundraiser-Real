def yes_no_response(question):
    error_message = "Please answer 'Y' or 'N'"
    valid_responses = ["y", "yes", "n", "no"]
    response = input(question).lower()
    while response not in valid_responses:
        print(error_message)
        response = input(question).lower()

    if response[0] == "n":
        return False
    else:
        return True


testing = True
while testing:
    snacks_required = yes_no_response("Do you want snacks? ")
    if not snacks_required:
        print("Valid answer. You don't want snacks")
    else:
        print("Valid answer. You do want snacks")
    print()
