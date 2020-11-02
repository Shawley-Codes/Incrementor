#6/5/2019
#Scott Hawley

#imports
import time

#Incrementor
#Class holds 2 functions
class incrementor:
    
    #Score
    #increment score based on current increment amount over time, then print
    def scoreInc(score, increment):
        score += increment
        print("Score: ", score)
    #Money
    #increment money based on current increment amount over time, then print
    def moneyInc(money, increment):
        money += increment
        print("Money: ", money)

#Money Management
#class holds 3 functions
class manageMoney:
    #Use data structures to return multiple values to program
	#experiment 1: arrays
	
    #Buy
    #takes in target name and current money
    #decreases money if successful purchase, changes increment amounts
    #print on unsuccessful purchase
    #def buy(target, money, incrementMoney, incrementScore):
    def buy(target, tracker):
        targetPrice = tracker[0]
        if target == "Score":
            targetPrice = 30
        elif target == "Money":
            targetPrice = 50
        if tracker[0] >= targetPrice:
            tracker[0] -= targetPrice
            print("\nSuccessful purchase")
            if targetPrice == 50:
                tracker[3] += 5
                tracker[4] += 10
                return tracker
                #incrementScore += 10
                #incrementMoney += 5
            elif targetPrice == 30:
                tracker[3] += 1
                tracker[4] += 20 
                return tracker
                #incrementScore += 20
                #incrementMoney += 1
        else:
            print("\nYou did not have enough money")
            return tracker
            
    #Save
    #takes in amount to store, current money, currently stored
    #decreases money if successful store, increase amount stored
    #print on unsuccessuful storage
    #print amount in bank
    #use tracker instead
    def save(store, tracker):
        if tracker[0] >= store:
            tracker[0] -= store
            tracker[2] += store
        else:
            print("You tried to store more money than you have!")
        print("\nYou currently have $", tracker[2], " stored in the bank.")
        return tracker
        
    #Withdraw
    #takes in amount to withdraw, current money, currently stored
    #increase money on successful withdraw, decrease amount stored
    #print on unsuccessful withdraw
    #print amount in bank
    def withdraw(draw, tracker):
        if draw <= tracker[2]:
            tracker[0] += draw
            tracker[2] -= draw
        else:
            print("You tried to withdraw more money thank you have stored.")
        print("You currently have $", tracker[2], " stored in the bank.")
        return tracker

#Play Loop
playAgain = "yes"

#Reset Game variables
while playAgain == "yes":
    
    #experiment 1: arrays
    #add all values to array "tracker" 
    tracker = [100,0,0,1,0,.1]
    #money = 100
    #score = 0
    #bank = 0
    #incrementMoney = 1
    #incrementScore = 0
    #incrementBank = .1
    roundNum = 1

    #Main Game Loop
    #Commands: Buy, Withdraw, Save, Wait
    #Get input on number of rounds
    print("Welcome to the incrementor game!\n")
    rounds = input("Please enter the amount of rounds(recommended 30): ")
    
    #input validation
    correctRounds = False
    while correctRounds == False:
        try:
            val = int(rounds)
            if val < 0:
                rounds = input("Invalid. Please enter a positive number: ")
            else:
                correctRounds = True
        except ValueError:
            rounds = input("Invalid. Please enter the amount of rounds: ")
    for num in range(0, int(rounds)):

        #Print round number, then get user input/validate
        print("\nRound ", roundNum)
        command = input("Please enter a command(Buy, Save, Withdraw, Wait): ")
        while command != "Buy" and command != "Save" and command != "Withdraw" and command != "Wait":
            command = input("Invalid! Please enter a command(Buy, Save, Withdraw, Wait): ")

        #run commands
        #buy command, print available options for purchase, get input, validate
        #call class function, Buy 
        if command == "Buy":
            print("\nCurrently available to purchase:\nScore Earner: $30\nMoney Earner: $50")
            target = input("\nPlease enter which to purchase(Score or Money): ")
            while target != "Score" and target != "Money":
                target = input("Please enter which to purchase(Score or Money): ")
            #manageMoney.buy(target, money, incrementMoney, incrementScore)
	    #give in target, and tracker values
            tracker = manageMoney.buy(target, tracker)

        #validate by try except
        elif command == "Withdraw":
            print("Welcome to the bank! Your savings is: $", tracker[2])
            draw = input("Please enter the amound you wish to withdraw: $")
            correctDraw = False
            #input validation
            while correctDraw == False:
                try:
                    val = int(draw)
                    if val < 0:
                        draw = input("Invalid. Please enter a positive number: $")
                    else:
                        correctDraw = True
                except ValueError:
                    draw = input("Invalid. Please enter the amount you wish to withdraw: $")

            tracker = manageMoney.withdraw(int(draw), tracker)

            
        elif command == "Save":
            print("Welcome to the bank! Your savings is: $", tracker[2])
            print("Your are currently holding: $", tracker[0])
            store = input("Please enter the amount you wish to save: $")


            #Validation for input of int
            #create loop for continous check
            #check wether value causes Value error or is negative, let out if neither
            correctStore = False
            while correctStore == False:
                try:
                    val = int(store)
                    if val < 0:
                        store = input("Invalid. Please enter a positive number: $")
                    else:
                        correctStore = True
                except ValueError:
                    store = input("Invalid. Please enter the amount you wish to save: $")
            #officially cast as int then send into function
            tracker = manageMoney.save(int(store), tracker)

            
        else:
            print("You decided to wait!")
        
        #increment numbers and print data
	#use array to print data
        tracker[0] += tracker[3]
        tracker[1] += tracker[4]
        tracker[2] = (tracker[2]*tracker[5]) + tracker[2]
	
        print("\nScore: ", tracker[1])
        print("Money: ", tracker[0])
        print("Stored: ", tracker[2])
		
		
	#money += incrementMoney
        #score += incrementScore
        #bank = (bank*incrementBank) + bank
        
        #print("\nMoney: $", money)
        #print("Score: ", score)
        #print("Stored: $", bank)
        
        roundNum = roundNum + 1
    playAgain = input("\n\nDo you want to play again (yes or no): ")    
        

        
