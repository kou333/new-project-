print("Welcome to my computer quiz!")

playing = input("DO you want to play ? ")

if playing.lower() !="yes":
    quit()

print("Okay! let's play:)" )

score = 0


answer=input("what does cpu stand for? ")
if answer.lower() == "central processing unit":
    print("correct")
    score+=1
else:
    print("Incorrect!")
    
answer=input(" what does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("correct")
    score+=1
else:
    print("Incorrect!")

answer=input(" What does ram stand for")
if answer.lower() == "random access memory":
    print("correct")
    score+=1
else:
    print("Incorrect!")

answer=input("What does Psu stand for ")
if answer.lower() == "power supply unit":
    print("correct")
    score+=1
else:
    print("Incorrect!")
    
print(" you got   "   +   str(score) +    "questions correct")
print(" you got   "   +   str((score/4)*100) +    "%.")



    
    