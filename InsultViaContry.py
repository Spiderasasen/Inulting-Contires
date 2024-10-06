# imports
import random
import csv

# turing the contries text file into a array
with open('Contries.txt') as x:
    contry = x.read().splitlines()

# turing the insults for every conutry
with open('insluts_for_every_contry.txt') as j:
    insult = j.read().splitlines()

# dictionary for all the differnt contries
Contry_and_Inslut = {}

for i in range(len(contry)-1):
    getContry = contry[i]
    getInslut = insult[i]
    Contry_and_Inslut[getContry] = getInslut

# picks a random contry
# randomConty = random.randrange(0,34)
randomConty = random.randrange(0,len(contry)-1)

# asking the user what if they want one country or all the counties

while True:
    # checking if the user entered a vailed number
    try:
        question = int(input('Please select one\n1. One Country\n2. All the Counties\n'))

        # the user's input will be checked if you chose the right item
        if question == 1:
            print('one country\n')
            # asking the user if they want a random country
            question = input('Do you want a random Country? y/n\n')
            # the user says yes to a random country
            if question.lower() == 'y':
                # prints a random country
                print(f'\nCountry: {contry[randomConty]}, Inslut: {Contry_and_Inslut[contry[randomConty]]}')
            # the user does not want a random country
            else:
                playerChoice = input('\nPlease type the country you want\n')
                # checking that the country that you said is in the list
                if playerChoice in contry:
                    print(f'\nCountry: {playerChoice}, Inslut: {Contry_and_Inslut[playerChoice]}')
                # telling the player the situation of the counties and give them a random country
                else:
                    print(f'\nThe country you have selected is not in my list, or I mispelled it, so here is a random country\nCountry:{contry[randomConty]}, Insult:{Contry_and_Inslut[contry[randomConty]]}')
            break

        # user wants to inslut all the countiers
        elif question == 2:
            # loop that will print all the countiers and inslut them
            for i in range(len(contry)-1):
                print(f'Country: {contry[i]}, Inslut: {Contry_and_Inslut[contry[i]]}')

            # finshing all insluts
            print('\nAll countries are now insluted\n')
            break

        # player chosed a differnt number then 1 or 2
        else:
            print('Please enter a vaild number\n')

    # the user entered a string instead of a int
    except ValueError:
        print('That is not a number, please enter a number\n')
