def foods_file():
    f = open("foods.txt","r")
    foods = [line for line in f.read().splitlines()[1:] if line.strip()] # Remove blank spaces
    f.close()
    food_list = []

    for food in foods:
        food = ''.join('' if letter == '&' else letter for letter in food)
        food = ''.join('' if letter.isnumeric() else letter for letter in food)

        food_list.append(food.title())

    return food_list


def high_fiber_file():
    f = open("highfiber.txt","r")
    fibers = [line for line in f.read().splitlines()[1:] if line.strip()] # Remove blank spaces
    f.close()
    fiber_list = []

    for fiber in fibers:
        if fiber == "23314":
            fiber == 'yes'
        fiber = ''.join('o' if letter == '0' else letter for letter in fiber)
        fiber = ''.join('' if letter == ' ' else letter for letter in fiber)
        fiber = ''.join('' if letter.isnumeric() else letter for letter in fiber)
        fiber_list.append(fiber.title())

    return fiber_list

print(len(high_fiber_file()))
print(len(foods_file()))