import random

answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy', 'try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']

def magic_response():
    while True:
        question = input()
        print ('What would you like to ask the Magic 8-Ball?',question)
        if question == 'goodbye':
            print('goodbye')
            exit()
        else:
            print (answers[random.randint(0, len(answers)-1)] )

magic_response()
