import random

#variable initialization
#Variables for the choices of the user and the computer
user_action =0
possible_actions=0
computer_action=0
#variable for user decisions in continuing the game
user_decision="yes" or "no"
#variables for points of the player 1 and player 2
points_1=0
points_2=0
#variable for the number of games played
gameplay=1
#list to display the winners of each game
results=[]
#variable for the index of the list
i=0


#welcoming the player and giving an introduction
print("--------------------------------------------------------")
print("Welcome to Inky Pinky Polly game Player 1!!")
print("--------------------------------------------------------")
print("Choices : Inky Pinky Polly")

#asking to input the choice of the user 
while(user_decision=="yes"):
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("Game ",gameplay)
    print("---------------------------------------------------------")
    user_action=input("Enter your choice : ")
    print("---------------------------------------------------------")
#Displaying the random choice of the computer 
    possible_actions=["Inky", "Pinky", "Polly"]
    computer_action=random.choice(possible_actions)
    print("Computer's choice : ",computer_action)
    print("---------------------------------------------------------")
#The results when user inputs Inky and computer chooses Pinky and adding the winner to the list
    if(user_action=="Inky") and (computer_action=="Pinky"):
        print("Pinky is stronger than Inky! PLAYER 2 WINS.")
        results.append("Player 2")
        print("Player 2 gets 1 point")
#Adding the points for the computer
        points_2=points_2 + 1
#The results when user inputs Pinky and computer chooses Inky and adding the winner to the list
    elif(user_action=="Pinky") and (computer_action=="Inky"):
        print("Pinky is stronger than Inky! YOU WIN!")
        results.append("Player 1")
        print("Player 1 gets 1 point")
#Adding the points for the user
        points_1=points_1 + 1
#The results when user inputs Inky and computer chooses Polly and adding the winner to the list
    elif(user_action=="Inky") and(computer_action=="Polly"):
        print("Inky is stronger than Polly! YOU WIN!")
        results.append("Player 1")
        print("Player 1 gets 1 point")
#Adding points for the user
        points_1=points_1 + 1
#The results when user inputs Polly and computer chooses Inky and adding the winner to the list
    elif(user_action=="Polly") and (computer_action=="Inky"):
        print("Inky is stronger than Polly! PLAYER 2 WINS.")
        results.append("Player 2")
        print("Player 2 gets 1 point")
#Adding points for the computer
        points_2=points_2 + 1
#The results when user inputs Pinky and computer chooses Polly and adding the winner to the list
    elif(user_action=="Pinky") and (computer_action=="Polly"):
        print("Polly is stronger than Pinky! PLAYER 2 WINS.")
        results.append("Player 2")
        print("Player 2 gets 1 point")
#Adding points for the computer
        points_2=points_2 + 1
#The results when user inputs Polly and computer chooses Pinky and adding the winner to the list
    elif(user_action=="Polly") and (computer_action=="Pinky"):
        print("Polly is stronger than Pinky! YOU WIN!")
        results.append("Player 1")
        print("Player 1 gets 1 point")
#Adding the points for the user
        points_1=points_1 + 1
#Creating an immediate replay when the choice of both the user and the computer are the same
    elif(user_action==computer_action):
        print("Both the players have entered ",user_action," therefore it is a tie!")
        print("Replay again")
        continue
#The results when user inputs invalid choices
    else:
        print("Invalid Choice")
        results.append("Invalid Play")
#Counting the number of game played
    gameplay=gameplay + 1
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
#asking a question in order to either continue or stop the loop
    user_decision=input("Do you want to play again?(yes/no) : ")
    
    

#displaying the points awarded to both the players
print("---------------------------------------------------------")
print("---------------------------------------------------------")
print("---------------------------------------------------------")
print("POINTS AWARDED TO EACH PLAYER")
print("---------------------------------------------------------")
print("---------------------------------------------------------")
print("Points gained by player 1 : ",points_1)
print("---------------------------------------------------------")
print("Points gained by player 2 : ",points_2)
print("---------------------------------------------------------")
print("---------------------------------------------------------")
#displaying message comparing the points gained by the players
if(points_1>points_2):
    print("CONGRATULATIONS!!!!!!! YOU HAVE GAINED MORE POINTS")
else:
    print("OOPS!! the computer gained more points,No worries better luck next time!!")
print("---------------------------------------------------------")
print("---------------------------------------------------------")
#Displaying the winners for each game
print("THE WINNERS FOR EACH GAME")
print("---------------------------------------------------------")
print("---------------------------------------------------------")
for gameplay in range(1,gameplay):
   print("Game ",gameplay," winner is :",end=" ")
   print(results[i])
   i=i+1
   print("--------------------------------------------------------")
   print("--------------------------------------------------------")
    
