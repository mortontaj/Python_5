Happy = input('Enter three numbers separated by a comma ",": ')
# print(Happy)
# print(type(Happy))
# print(type(Happy[0]), type(Happy[1]), type(Happy[2]))
# print()
# print("**" * 40)

Happy = Happy.split(",")

# print()

# print("After split method")
# print(type(Happy))
# print(type(Happy[0]), type(Happy[1]), type(Happy[2]))
# print("**" * 40)

for index in range(len(Happy)):
    Happy[index] = int(Happy[index])

print(Happy[0] + Happy[1] - Happy[2])
# print("**" * 40)

# print()
# print("After split method, After int conversion")
# print(type(Happy))
# print(type(Happy[0]), type(Happy[1]), type(Happy[2]))