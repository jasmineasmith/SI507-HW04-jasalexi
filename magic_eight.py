import random

eight_ball = ["Signs point to yes","Yes","Reply hazy try again",
            "Without a doubt","My sources say no","As I see it, yes",
            "You may rely on it","Concentrate and ask again",
            "Outlook not so good","It is decidedly so",
            "Better not tell you now","Very doubtful","Yes definitely",
            "It is certain","Cannot predict now","Most likely",
            "Ask again later","My reply is no","Outlook good","Don't count on it"]
eight_answer = random.choice(eight_ball)
	


while True:
	ask=input("What is your question? (please end in '?')")
	if ask == "quit":
		break
	elif ask.endswith("?")==False:
		print("I’m sorry, I can only answer questions.")
	else:
		print(eight_answer)


