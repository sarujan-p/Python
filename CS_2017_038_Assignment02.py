#CS/2017/038
import random

number = random.randint(1, 100)

print("----------------------------------", number, "------------------------------------")
print("--------------------------------------------------------------------------")
print('|','\t','\t','\t','\t','\t','\t','\t','\t','\t','|')
print('|','\t','\t','\t','\t','\t','\t','\t','\t','\t','|')
print("------------------------Guessing Game Challenge---------------------------")
print("-------------------Written By: Sarujan P(CS/2017/038)---------------------")
print("--------------------------------------------------------------------------")
print('|','\t','\t','\t','\t','\t','\t','\t','\t','\t','|')
print('|','\t','\t','\t','\t','\t','\t','\t','\t','\t','|')

print("---------------------------Details Of Game!-------------------------------")
print('|','\t','\t','\t','\t','\t','\t','\t','\t','\t','|')
print('|','\t','\t','\t','\t','\t','\t','\t','\t','\t','|')

print('|','\t','\t',"01)I have a number in mind that is between 1 and 100",'\t','|')
print('|','\t','\t',"02)Guess <= 1 OR Guess >= 10 OUT OF BOUNDS",'\t','\t','|')
print('|','\t','\t',"03)If you are within 10 I will scream WARM",'\t','\t','|')
print('|','\t','\t',"04)If you are 10 or more away from the number COLD",'\t','|')
print('|','\t','\t',"05)If you get closer I will scream WARMER",'\t','\t','|')
print('|','\t','\t',"06)If you get farther away I will scream COLDER",'\t','|')

print('|','\t','\t','\t','\t','\t','\t','\t','\t','\t','|')
print('|','\t','\t','\t','\t','\t','\t','\t','\t','\t','|')
print("--------------------------------------------------------------------------")
print('|')
print('|')


guesses = [0]
    
while True:
    print("CS-2017-038~$----------Guess The Number")
    print("|")
    print("|")
    guess = int(input("CS-2017-038~$----------> "))
    
    while guess < 1 or guess > 100:
        if guess < 1 or guess > 100:
            print("|")
            print("|")
            print("CS-2017-038~$----------OUT OF BOUNDS")
            print("|")
            print("|")
            guess = int(input("CS-2017-038~$----------> "))
    
    if guess == number:
        if len(guesses) == 1:
            print("|")
            print("|")
            print("--------------------------------------------------------------------------")
            print('|','\t','\t','\t','\t','\t','\t','\t','\t','\t','|')
            print('|','\t','\t','\t','\t','\t','\t','\t','\t','\t','|')
            print("----------------------------Congratulations!------------------------------")
            print("-------------------", f'Your Guesed Number {number} is Correct----------------------')
            print("----------------------------Guessing Time:", f'{len(guesses)}------------------------------')
            print('|','\t','\t','\t','\t','\t','\t','\t','\t','\t','|')
            print('|','\t','\t','\t','\t','\t','\t','\t','\t','\t','|')
            print("------------------------------Game Over!----------------------------------")

        else: 
            print("|")
            print("|")
            print("--------------------------------------------------------------------------")
            print('|','\t','\t','\t','\t','\t','\t','\t','\t','\t','|')
            print('|','\t','\t','\t','\t','\t','\t','\t','\t','\t','|')
            print("----------------------------Congratulations!------------------------------")
            print("-------------------", f'Your Guesed Number {number} is Correct----------------------')
            print("----------------------------Guessing Times:", f'{len(guesses)}------------------------------')
            print('|','\t','\t','\t','\t','\t','\t','\t','\t','\t','|')
            print('|','\t','\t','\t','\t','\t','\t','\t','\t','\t','|')
            print("------------------------------Game Over!----------------------------------")
            
        break

    guesses.append(guess)
    
    if guesses[-2]:
        if abs(number - guess) < abs(number - guesses[-2]):
            print("|")
            print("|")
            print("CS-2017-038~$----------WARMER")
        else: 
            print("|")
            print("|")
            print("CS-2017-038~$----------COLDER")
                      
    if abs(number - guess) <= 10:
        print("|")
        print("|")
        print("CS-2017-038~$----------WARM")
        print("|")
        print("|")
    else: 
        print("|")
        print("|")
        print("CS-2017-038~$----------COLD")
        print("|")
        print("|")