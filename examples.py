# RUN THIS FILE TO INTERACT WITH IT
# Accepting input from the user in the form of a string, or using input() normally.

name = input('who are you? ')
print('hello, ' + name + ', it is pleasure to meet you. my name is dot.\n')

color = input('what is your favorite color? ')
print(color + ' is a wonderful color, i happen to be a fan of cyan.\n')

animal = input('do you have a favorite animal? ')
print(animal + '? personally i don\'t really like them, but to each their own.\n')

print(
    'unfortunately i do not have access to most of my functions now,\n' +
    'but i can do a few things!\n'
)

# Casting input from the user in the form of a number.

num = int(input('enter a whole number! '))

print(num, 'squared is', num ** 2)
input('\nimpressive right? ')
print('>_< i know it\'s not, but, i can do a few other things!\n')

print('i can find area of a rectangle!\n')

width = float(input('what is the width of this hypothetical rectangle? '))
height = float(input('and the height? '))
area = width * height

print()

# Casting back to a string to attach '...\n' to the end
print('a rectangle with a width of', width, 'and height of', height, 'has an area of', str(area) + '...\n')
units = input('uh... what are the units? inches? centimeters? ')
print('thank you!\n')

print('a rectangle with a width of', width, units, 'and height of', height, units, 'has an area of', area, units)

print('\ni can also make shapes!')

char = input('enter a symbol: ')
num = int(input('and a size: '))
print()


def draw_rect(symbol, size):
    print((symbol * size + '\n') * size)


draw_rect(char, num)


print('\nthat\'s all for now, thank you for running me!')