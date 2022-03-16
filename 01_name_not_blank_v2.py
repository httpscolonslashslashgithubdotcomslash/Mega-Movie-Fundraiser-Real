def not_blank(question, error_message):
    valid = ""
    while not valid:
        response = input(question)
        if not response:
            print(error_message)
        else:
            return response


name = not_blank("Please input a name: ", "You can't leave this blank...")
