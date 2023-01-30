# number_list = [9, 7, 3, 3, 3, 15, -14, 9]
# words_list = ['names', 'age', 'morning']
# print(number_list)
# number_list.pop()
# print(number_list)
# print(words_list)
# print(number_list[1])
# print(words_list[1])
# print([words_list[0], words_list[2]])


fruites = {
    "apple": 500,
    "banana": 400,
    "pinapple": 700,
    "watermelon": 300,
    "orange": 600
}

print(fruites)
print(1)

fruites["mango"] = 800
print(fruites)
print(2)
fruites.update({"pear": 100})
print(fruites)
print(3)
del fruites["apple"]
print(fruites)
print(4)

for key in fruites.keys():
    print(key)

for key, value in fruites.items():
    if value >= 500:
        print(value)






