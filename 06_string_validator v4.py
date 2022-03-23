def get_choice(question, valid_choices):
    choice_error = "Sorry, that is not a valid choice"
    choice = input(question).lower()
    for item in valid_choices:
        if choice in item:
            choice = item[0].title()
            return choice

    print(choice_error)
    return get_choice(question, valid_choices)


ask_for_snacks = "What snack do you want - 'x' to stop ordering: "
valid_snacks = [["popcorn", "p", "corn", "1"], ["m&ms", "mms", "m", "2"],
                ["pita chips", "chips", "pc", "pita", "c", "3"],
                ["water", "w", "4"], ["x", "X", "exit", "5"]]
check_snacks = "Do you want snacks? "
valid_yes_no = [["y", "yes"], ["n", "no"]]
snacks_required = get_choice(check_snacks, valid_yes_no)
snack_order = []

getting_snacks = True
while getting_snacks:
    if snacks_required == "N":
        getting_snacks = False
    else:
        option = get_choice(ask_for_snacks, valid_snacks)
        if option != "X":
            snack_order.append(option)
        else:
            getting_snacks = False

if len(snack_order) > 0:
    print("\nThis is a summary of your order:")
    for item in snack_order:
        print(f"\t{item}")
else:
    print("No snacks were ordered.")
