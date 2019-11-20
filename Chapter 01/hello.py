# This program says hello and asks for the user's name and the user's age.

print('Hello World!')

print('\nWhat is your name?')
myName = input()
print('\nIt is good to meet you, ' + myName)

print('The length of your name is: ' + str(len(myName)))

print('\nWhat is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' years old soon.')
