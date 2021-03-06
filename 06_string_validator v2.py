def get_choice(question, valid_choices):
    choice_error = "Sorry, that is not a valid choice"

    choice = input(question).lower()
    for item in valid_choices:
        if choice in item:
            choice = item[0].title()
            return choice

    print(choice_error)
    return get_choice(question, valid_choices)


ask_for_snack = "What snack do you want: "
valid_snacks = [["popcorn", "p", "corn", "1"], ["m&ms", "mms", "m", "2"],
                    ["pita chips", "chips", "pc", "pita", "c", "3"],
                    ["water", "w", "4"]]
for test in range(6):
    print(f"You have chosen {get_choice(ask_for_snack, valid_snacks)}")
