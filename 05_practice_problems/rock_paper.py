# import random
# player=input("enter your choice rock ,paper or scissor:")
# computer=random.choices(["rock","paper","scissor"])
# print("computer:",computer)

# if player==computer:
#     print("tie")
# elif player=="rock" and computer=="scissor":
#     print("you win")
# elif player=="paper" and computer=="rock":
#     print("you win")
# elif player=="scisscor" and computer=="paper":
#     print("you win")
# else:
#     print("computer win")

player1=input("enter your choice rock ,paper or scissor:").lower()
player2=input("enter your choice rock ,paper or scissor:").lower()
if player1=="rock" and player2=="paper":
    print("player 2 is winner")
elif player1=="rock" and player2=="scissor":
    print("player 1 is winner")
elif player1=="paper" and player2=="rock":
    print("player 1 is winner")
elif player1=="paper" and player2=="scissor":
    print("player 2 is winner")
elif player1=="scissor" and player2=="rock":
    print("player 2 is winner")
elif player1=="scissor" and player2=="paper":
    print("player 1 is winner")
elif player1==player2:
    print("Tie")
else:
    print("invalid choice")






