f = open("foods.txt","r")
foods = [line for line in f.read().splitlines()[1:] if line.strip()] # Remove blank spaces
f.close()
food_list = []

for food in foods:
    food = ''.join('' if letter == '&' else letter for letter in food)
    food = ''.join('' if letter.isnumeric() else letter for letter in food)

    food_list.append(food.title())

print(food_list)
