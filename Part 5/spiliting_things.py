panagram = """The quick brown
fox jumps\tover
the lazy dog"""

words = panagram.split()
print(words)

numbers = "9,223,372,036,854,775,807"
print(numbers.split(","))

print()
print("***" * 30)
print()

generated_list = ['9', ' ',
                  '2', '2', '3', ' ',
                  '3', '7', '2', ' ',
                  '0', '3', '6', ' ',
                  '8', '5', '4', ' ',
                  '7', '7', '5', ' ',
                  '8', '0', '7']
values = "".join(generated_list)
print(values)

print()
print("***" * 30)
print()

values_list = values.split()
print(values_list)

new_numbers = []
for char in values_list:
    new_numbers.append(int(char))

print(new_numbers)

## replace the values in place
for index in range(len(values_list)):
    values_list[index] = int(values_list[index])

print(values_list)