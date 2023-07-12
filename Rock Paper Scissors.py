import random

l=['rock','paper','scissors']
print("Welcome to the Game!!")
print('''Enter Your Choice: 
1. Play
2. Exit''')
c=int(input("Enter choice in number: "))
while c!=2:
    a=input("Enter element[rock,paper,scissors]: ")
    b=random.choice(l)
    print('You: ',a,'Me: ',b)
    if a==b:
        print('SAME!!!')
    elif a=='rock':
        if b=='paper':
            print('You Lose!')
        else:
            print('You Win!!')
    elif a=='paper':
        if b=='scissors':
            print('You Lose!')
        else:
            print('You Win!!')
    elif a=='scissors':
        if b=='rock':
            print('You Lose!')
        else:
            print('You Win!!')
    c=int(input("Enter choice in number: "))
