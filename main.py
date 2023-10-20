import random
import time
print("-------Chattin\' America-------")

print('Questions to ask Chattin\' America:')
print("What\'s your name?")
print('What sports do you like?')
print('Who is your favorite superhero?')
print('How old are you?')
request = ''
#       0           1           2           3           4       5           6       7           8
sports=['soccer','football','basketball','volleyball','rugby','bowling','tennis','swimming', 'cheerleading']
superheros=['spiderman','iron man','captain america','hulk','ant-man', 'falcon', 'thor','black widow']
age=['I am 21.','I am 19.','I am 18.','None of your business','I\'m really young actually, thanks for asking!', 'Don\'t worry about it', 'You think i\'m old?']
res=['What are you talking about?','I don\'t understand','You just chatting right now.','Try again??','I\'m sorry?']
def printSlowly(str):
    for i in str :
        time.sleep(0.00000001)
        print(i,end='')
    print()
while request != 'bye':
    request=input('Ask me anything:')
    request = request.lower()
    if request == 'what sports do you like?':
        pick = random.randint(0,len(sports)-1)
        printSlowly('Personally, I\'m more of a '+ sports[pick]+ ' type of guy.')
    elif request == 'who is your favorite superhero?':
        pick = random.randint(0,len(superheros)-1)
        printSlowly('Lets be real '+ superheros[pick]+ ' is the best.')
    elif request == 'how old are you?':
        pick = random.randint(0,len(age)-1)
        printSlowly(age[pick])
    elif request == 'what is your name?':
        printSlowly('My name is Chattin\' America')
    elif request == 'bye':
        printSlowly('Ok, it was nice chatting with you!')
    else:
        pick = random.randint(0,len(res)-1)
        printSlowly(res[pick])
