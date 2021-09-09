import random

print("Winning rules of the game are as follows\n"
       "Rock vs paper->paper wins\n"
       "Rock vs scissor->rock wins\n"
       "paper vs scissor->scissor wins\n")

def comp_ch(num):
     if num==1:
        return "rock"
     elif num==2:
        return "paper"
     elif num==3:
        return "scissors"

outcomes={"rock":{"rock":"draw","paper":"loss","scissors":"won"},"paper":{"rock":"won","paper":"draw","scissors":"loss"}
          , "scissors":{"rock":"loss","paper":"won","scissors":"draw"} }

round=1

while round <10 :
   random_num=random.randint(1,3)
   computer_choice=comp_ch(random_num)
   user_choice=input(str("Select rock/paper/scissors:"))
   print("user selected:",user_choice)
   print("computer selected:",computer_choice)
   result= outcomes[user_choice][computer_choice]
   if(result==won):
   player_score+=1
   elif(result=loss):
   computer_score+=1

   print("Outcome",result)
   print("")
   break
   print("score made by user",player_score)
   print("score made by computer",computer_score)
   if(player_score>computer_score):
   print("player won")
   else("computer won")