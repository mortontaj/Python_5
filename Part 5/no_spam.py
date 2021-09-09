menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
]

for list in menu:
    spamless = []
    for item in list:
        if item != "spam":
            spamless.append(item)
    print(", ".join(spamless))

# for dish in menu:
#     for ingredient in dish:
#         if ingredient != "spam":
#             print(ingredient, end=", ")
#     print()

# for meal in menu:
#     for index in range(len(meal) - 1, -1, -1):
#         if meal[index] == "spam":
#             del meal[index]
#
#     print(", ".join(meal))

