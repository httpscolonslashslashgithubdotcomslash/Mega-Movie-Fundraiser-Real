def not_blank(question):
    valid = ""
    while not valid:
        response = input(question)
        if not response:
            print("You can't leave this blank!")
        else:
            return response


name = not_blank("Please input a name: ")
