import random,math
def game(start,end):
    #generating random number in between of start and end
    random_number = random.randint(start,end)

    #How many of chance to users find a number
    maximum_chance = round(math.log2(end-start+1))

    #show the chance to user
    print('\n\t"You\'ve only',maximum_chance,'attempts to guess the number!"')

    #loop run
    count = 0
    while count < maximum_chance:
        count += 1

        #taking guessing number
        guessing_number = int(input("\n\tGuess a number:"))

        #conditions testing
        if guessing_number == random_number:
            print("\n\tYour guessing number", guessing_number,"is correct,Congratulations!")

            #find the guessing number loop will be end
            break
        elif guessing_number > random_number:
            print("\n\tYour guessing number is too high")
            print("\tremaining chance",maximum_chance-count)
        elif guessing_number < random_number:
            print("\n\tYour guessing number is too low")
            print("\tremaining chance", maximum_chance - count)

    #if user reach a chance show the answer
    else:
        print("\n\tThat number is",random_number,"Betterluck next time")

try:
    #Taking inputs
    #if user inputs non integer values
    start = int(input("Enter a starting range value:"))
    end = int(input("Enter a ending range value:"))
except:
    #informed to user strictly enter integer values
    print("\nPlease enter a whole number")
else:
    #no mistake in users side else block will be executed
    #game function called
    game(start,end)