#to create a conversational AI assitant using python's core logic-string matchin,funtions,dictionaries,and loops
#in this project we will build a mini Ai chatbot like "hello","motivate me",or "python"and respond with friendly,intelligent answers
#this is a rule-based chatbot,it doesnt use real AI models yet,but it behaves intelligently using python logic
#it is minor project
import datetime
import time
#greeting the user according to their time
print("-----Hello And Welcome To Your Personal AI Chat Bot-----")
name=input("enter your name")
presentHour=datetime.datetime.now().hour
if 5<= presentHour <=11:
    time.sleep(1)
    print('good morning',name)
elif 11<= presentHour <=17:
    time.sleep(1)
    print("good afternoon",name)
elif 17<= presentHour <=20:
    time.sleep(1)
    print("good evening",name)
else:
    time.sleep(1)
    print("good night")
#main program 
print("You Can Ask me basic quesstion,an to exit type'bye'")

#Chatebot memory creation{dictionary of responses}
responses={
        "hello":"hi welcome how can i help you",
        "how are you":"i am very fine thank you",
        "who are you":"i am smart  Ai chatbot",
        "motivate me":"keepgoing consistency breaks motivation",
        "i am happy":"ooh! glad to here that",
        "i am sad":"ooh! sad to hear what can i do to make you happy",
        "what are functions":"funtions are block of code which is easy to use again and again without writing the same code again and again"
}
#function to give response of user
def getResponseOfBot(user):
    for eachkey in responses:
        if eachkey in user:
            return responses[eachkey]
        time.sleep(1)
    return ("I am not able to tell that,I am still in training mode")
    

#take user input

while True:
    user = input("Please ask your question or type bye to exit: ").lower()
    time.sleep(1)
    if "bye" in user:
        print("Thanks for using the chatbot!")
        break
    reply = getResponseOfBot(user)
    print("Bot Response:", reply)

       
