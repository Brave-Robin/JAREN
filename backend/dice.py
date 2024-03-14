import random

# baff, debaff, none
# blessed, cursed, none

def baff_revisor(status, sides, relict):
    if relict == 'blessed':
        if status == 'baff':
            result = cube_roll(sides)
            result2 = cube_roll(sides)
            print(status, result, result2)
            if result == 1:
                result = sides
            if result2 == 1:
                result2 = sides
            if result > result2:
                return result
            else:
                return result2
        elif status == 'debaff':
            result = cube_roll(sides)
            result2 = cube_roll(sides)
            print(status, result, result2)
            if result == sides:
                result = 1
            if result2 == sides:
                result2 = 1
            if result > result2:
                return result
            else:
                return result2
    elif relict == 'cursed':
        if status == 'baff':
            result = cube_roll(sides)
            result2 = cube_roll(sides)
            print(status, result, result2)
            if result == 1:
                result = sides
            if result2 == 1:
                result2 = sides
            if result < result2:
                return result
            else:
                return result2
        elif status == 'debaff':
            result = cube_roll(sides)
            result2 = cube_roll(sides)
            print(status, result, result2)
            if result == sides:
                result = 1
            if result2 == sides:
                result2 = 1
            if result < result2:
                return result
            else:
                return result2
    else:
        return cube_roll(sides)


def cube_roll(sides):
    return random.randint(1, sides)


print(baff_revisor('debaff', 10, 'cursed'))
# d4,6,8,10,12,20, 10-граней