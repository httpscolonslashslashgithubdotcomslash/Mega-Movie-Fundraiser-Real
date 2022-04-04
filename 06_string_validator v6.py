import re


def split_order(choice):
    number_regex = "^[1-9]"
    if re.match(number_regex, choice):
        quantity_requires = int(choice[0])
        snack_name = choice[1:]
    else:
        quantity_requires = 1
        snack_name = choice
    snack_name = snack_name.strip()
    return quantity_requires, snack_name


def get_choice(choice, valid_choices):
    choice_error = "Sorry, that is not a valid choice"
    for list_item in valid_choices:
        if choice in list_item:
            choice = list_item[0].title()
            return choice
    print(choice_error)

def collate_order():
    valid_snacks = [["popcorn", "p", "corn", "(1"], ["m&ms", "mms", "m", "(2"],
                    ["pita chips", "chips", "pc", "pita", "c", "(3"],
                    ["water", "w", "(4"], ["orange juice", "oj", "(5"],
                    ["x", "X", "exit", "(6"]]
    valid_yes_no = [["y", "yes"], ["n", "no"]]
    snack_order = []
    max_number_of_snacks = 4
    getting_snacks = True

    while getting_snacks:
        snacks_required = ""
        while snacks_required != "N" and snacks_required != "Y":
            check_snacks = input("Do you want snacks? (Y/N): ").lower()
            snacks_required = get_choice(check_snacks, valid_yes_no)
        if snacks_required == "N":
            getting_snacks = False
            break
        else:
            option = ""
            while option != "X":
                snack = input(
                    "What snack do you want - or 'X' to stop ordering: "
                    ).lower()
                snack = split_order(snack)
                quantity = snack[0]
                if quantity > max_number_of_snacks:
                    snack = None
                    print("Sorry, the maximum number you can order is 4")
                else:
                    snack = snack[1]
                    option = get_choice(snack, valid_snacks)
                    if option == "X":
                        getting_snacks = False
                    elif option is not None:
                        snack_order.append([quantity, option])
    return snack_order


snack_order = collate_order()


if len(snack_order) > 0:
    print("\nThis is a summary of your order: ")
    for item in snack_order:
        print(f"\t{item[0]} {item[1]}")
else:
    print("No snacks were ordered")
