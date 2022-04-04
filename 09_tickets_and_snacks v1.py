import pandas

names = ["Rangi", "Manaia", "Talia", "Arihi", "Fetu"]
tickets = [7.5, 10.5, 10.5, 10.5, 6.5]

popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []
snack_lists = [popcorn, mms, pita_chips, water, orange_juice]
movie_data_dict = {
    "Name": names,
    "Ticket": tickets,
    "Popcorn": popcorn,
    "Water": water,
    "Pita Chips": pita_chips,
    "M&Ms": mms,
    "Orange Juice": orange_juice
}

price_dict = {
    "Popcorn": 2.5,
    "Water": 2,
    "Pita Chips": 4.5,
    "M&Ms": 3,
    "Orange Juice": 3.25,
}

test_data = [
    [[2, "Popcorn"], [1, "Pita Chips"], [1, "Orange Juice"]],
    [[]],
    [[1, "Water"]],
    [[1, "Popcorn"], [1, "Orange Juice"]],
    [[1, "M&Ms"], [1, "Pita Chips"], [3, "Orange Juice"]]
]

count = 0
for client_order in test_data:
    for item in snack_lists:
        item.append(0)
    snack_order = test_data[count]
    count += 1

    for item in snack_order:
        if len(item) > 0:
            to_find = item[1]
            amount = item[0]
            add_list = movie_data_dict[to_find]
            add_list[-1] = amount


print()


movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index("Name")

movie_frame["Sub Total"] = \
    movie_frame["Ticket"] + \
    movie_frame["Popcorn"] + price_dict["Popcorn"] + \
    movie_frame["Water"] + price_dict["Water"] + \
    movie_frame["Pita Chips"] + price_dict["Pita Chips"] + \
    movie_frame["M&Ms"] + price_dict["M&Ms"] + \
    movie_frame["Orange Juice"] + price_dict["Orange Juice"]

movie_frame = movie_frame.rename(columns={"Orange Juice": "OJ",
                                          "Pita Chips": "Chips"})

print(movie_frame)
