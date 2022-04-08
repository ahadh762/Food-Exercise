def foods_file():
    f = open("foods.txt","r")
    foods = [line for line in f.read().splitlines()[1:] if line.strip()] # Remove blank spaces
    f.close()
    food_list = []

    for food in foods:
        if '&' in list(food):
            food = ""
        food = ''.join('' if letter.isnumeric() else letter for letter in food)

        food_list.append(food.title())

        if food == "":
            food_list.remove(food)        

    return food_list


def high_fiber_file():
    f = open("highfiber.txt","r")
    fibers = [line for line in f.read().splitlines()[1:] if line.strip()] # Remove blank spaces
    f.close()
    fiber_list = []

    for fiber in fibers:
        fiber = ''.join('o' if letter == '0' else letter for letter in fiber)
        fiber = ''.join('' if letter == ' ' else letter for letter in fiber)
        fiber = ''.join('' if letter.isnumeric() else letter for letter in fiber)
        fiber_list.append(fiber.title())
        if fiber == "":
            fiber_list.remove(fiber)

    return fiber_list


def low_glycemic_index_file():
    f = open("low-glycemic-index.txt","r")
    glycemic_index = [line for line in f.read().splitlines()[1:] if line.strip()] # Remove blank spaces
    f.close()
    GI_list = []

    for GI in glycemic_index:
        if len(GI) > 3:
            GI = ""
        GI = ''.join('o' if letter == '0' else letter for letter in GI)
        GI = ''.join('' if letter == ' ' else letter for letter in GI)
        GI = ''.join('' if letter.isnumeric() else letter for letter in GI)
        GI_list.append(GI.title())
        if GI == "":
            GI_list.remove(GI)

    return GI_list

def low_fat_file():
    f = open("low-glycemic-index.txt","r")
    fat_amount = [line for line in f.read().splitlines()[1:] if line.strip()] # Remove blank spaces
    f.close()
    low_fat_list = []

    for fat in fat_amount:
        if len(fat) > 3:
            fat = ""
        fat = ''.join('o' if letter == '0' else letter for letter in fat)
        fat = ''.join('' if letter == ' ' else letter for letter in fat)
        fat = ''.join('' if letter.isnumeric() else letter for letter in fat)
        low_fat_list.append(fat.title())
        if fat == "":
            low_fat_list.remove(fat)

    return low_fat_list

print(len(high_fiber_file()))
print(len(foods_file()))
print(len(low_glycemic_index_file()))
print(len(low_fat_file()))