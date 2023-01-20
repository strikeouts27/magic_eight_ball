name = "Andrew"
question = "Will the Dallas Cowboys win the Super Bowl?"
answer = ""
import random
random_number = random.randint(1,24)
# print(random_number)

if random_number == 1:
  answer = "Yes definitely!"
elif random_number == 2:
  answer = "It is decidely so!"
elif random_number == 3:
  answer = "Without a doubt!"
elif random_number == 4:
  answer = "Reply hazyy, try again. I partied too hard last night!"
elif random_number == 5:
  answer = "Ask again later."
  
elif random_number == 6:
  answer = "Better not tell you now"

elif random_number == 7:
  answer = "My sources say no"  
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "You do not have the necessary information to ask the right questions. Seek council from others"
elif random_number == 11:
  answer = "The odds are not in your favor!"
elif random_number == 12:
 answer = "It is possible but the odds are not in your favor!" 
elif random_number == 13:
  answer = "Bro, I am not your therapist."
elif random_number == 14:
  answer = "You are not in a place to listen to what I have told you. You are not willing to hear the truth."
elif random_number == 15:
  answer = "Its time to move on."
elif random_number == 16:
  answer = "I think you need to speak to an expert on this one!"
elif random_number == 17: 
  answer = "Shake me three more times for an answer!"
elif random_number == 18: 
  answer = "I will ask my eight ball network I actually need to talk to my peers please hold. "
elif random_number == 19:
  answer = "You need to remember some key information. After you remember you can ask me the question you need to ask. What you ask right now is not the right question to be asking. "
elif random_number == 20:
  answer = "It is too soon to ask me. Wait for more information."
elif random_number == 21:
  answer = "Everything is going to be okay. Just have faith."
elif random_number == 22:
  "You must be decisive. Pick a path and than stick to it. If you do so, it will be okay."
elif random_number ==23:
  "Your actions are despicable. I will not answer you nor help you."
elif random_number == 24:
  answer = "You do not believe in my powers yet. But someday you will."
else: 
  answer = "Error"
  print(answer)

print(name + " asks: " + question)
print("Magic 8-Ball's answer: " + answer)
if name == "":
  print("Question: " + question)
  print("Magic 8- Ball's answer: " + answer)

if question == "":
  print("Tell me your question and I will give you my best advice.")

# Lines 62 and 67 point out that even after a long if statement you can add conditions to the activation phase as long as you stay in that if statement. 


