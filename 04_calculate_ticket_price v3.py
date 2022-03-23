def calculate_ticket_price(age):
    child_age = range(12, 16)
    standard_age = range(16, 65)

    child_price = 7.5
    standard_price = 10.5
    retired_price = 6.5

    if age in child_age:
        ticket_price = child_price
    elif age in standard_age:
        ticket_price = standard_price
    else:
        ticket_price = retired_price
    return ticket_price


test_cases = [["Rangi", 15],["Manaia", 16], ["Talia", 64], ["Arihi", 65]]

for test in test_cases:
    test_name = test[0]
    test_age = test[1]
    print(f"For {test_name} the price is ${calculate_ticket_price(test_age):,.2f}.")

