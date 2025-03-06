print('Welcome to TERMINAL ADVENTURE! \nI am Isaac, and I will give as many tips and guildence as I can to facilitise your game. \nIn this game, you will be given a series of choices that will determine your fate. \nAfter the FIVE-night adventure, you will be the winner if you can survive. Good luck!')
name=input("Firstly, please enter your name:")
hp=100
print(f'Well done, {name}({hp})! As you can see, in the brackets is your health points (hp).\n ATTENTION! Once your hp become zero, your game is OVER!\n \nNow, let us begin our adventure!')
print(f'{name}({hp}), welcome to day 1 of your adventure.')
print('Congratulations! You are admitted in to the University of Nottingham Ningbo China (UNNC).')
print('Unfortunately, you are late for your first lecture. \nYou have two choices:')
print('1. Run to the lecture theatre.')
print('2. Skip the lecture and go to the library.')
choice1=input('Please enter your choice:')
if choice1=='1':
    print('You are running to the lecture theatre. \nSuddenly, you see a group of students are fighting. \nYou have two choices:')
    print('1. Join the fight.')
    print('2. Ignore them and keep running.')
    choice2=input('Please enter your choice:')
    if choice2=='1':
        print('You are joining the fight. \nUnfortunately, you are beaten up by the group of students. \nYou lost 50 hp.')
        hp=hp-50
        print(f'Now, your hp is {hp}.')
    elif choice2=='2':
        print('You are ignoring them and keep running. \nYou successfully arrive at the lecture theatre. \nYou are safe. \nYou gain 10 hp.')
        hp=hp+10
        print(f'Now, your hp is {hp}.')
elif choice1=='2':
    print('You are going to the library. \nYou see a group of students are studying together. \nYou have two choices:')
    print('1. Join them.')
    print('2. Ignore them and keep studying.')
    choice3=input('Please enter your choice:')
    if choice3=='1':
        print('You are joining them. \nYou have a great time with them. \nYou gain 10 hp.')
        hp=hp+10
        print(f'Now, your hp is {hp}.')
    elif choice3=='2':
        print('You are ignoring them and keep studying. \nYou successfully finish your study. \nYou gain 5 hp.')
        hp=hp+5
        print(f'Now, your hp is {hp}.')
print(f'{name}({hp}), welcome to day 2 of your adventure.')
print('You are going to the canteen for lunch. \nYou have two choices:')
print('1. Order a burger.')
print('2. Order a salad.')
choice4=input('Please enter your choice:')
if choice4=='1':
    print('You are ordering a burger. \nYou enjoy the burger. \nYou gain 5 hp.')
    hp=hp+5
    print(f'Now, your hp is {hp}.')
elif choice4=='2':
    print('You are ordering a salad. \nYou enjoy the salad. \nYou gain 10 hp.')
    hp=hp+10
    print(f'Now, your hp is {hp}.')
print(f'{name}({hp}), welcome to day 3 of your adventure.')
print('You are going to the gym for workout. \nYou have two choices:')
print('1. Run on the treadmill.')
print('2. Lift weights.')
choice5=input('Please enter your choice:')
if choice5=='1':
    print('You are running on the treadmill. \nYou run for 30 minutes. \nYou gain 5 hp.')
    hp=hp+5
    print(f'Now, your hp is {hp}.')
elif choice5=='2':
    print('You are lifting weights. \nYou lift weights for 30 minutes. \nYou gain 10 hp.')
    hp=hp+10
    print(f'Now, your hp is {hp}.')
print(f'{name}({hp}), welcome to day 4 of your adventure.')
print('You are going to the cinema with your friends. \nYou have two choices:')
print('1. Watch a horror movie.')
print('2. Watch a comedy movie.')
choice6=input('Please enter your choice:')
if choice6=='1':
    print('You are watching a horror movie. \nYou are scared. \nYou lose 5 hp.')
    hp=hp-5
    print(f'Now, your hp is {hp}.')
elif choice6=='2':
    print('You are watching a comedy movie. \nYou are laughing. \nYou gain 5 hp.')
    hp=hp+5
    print(f'Now, your hp is {hp}.')
print(f'{name}({hp}), welcome to day 5 of your adventure.')
print('You are going to the library for study. \nYou have two choices:')
print('1. Study in the silent area.')
print('2. Study in the group study area.')
choice7=input('Please enter your choice:')
if choice7=='1':
    print('You are studying in the silent area. \nYou are focused. \nYou gain 10 hp.')
    hp=hp+10
    print(f'Now, your hp is {hp}.')
elif choice7=='2':
    print('You are studying in the group study area. \nYou are distracted. \nYou lose 5 hp.')
    hp=hp-5
    print(f'Now, your hp is {hp}.')
if hp>0:
    print(f'Congratulations! You have successfully completed the FIVE-night adventure! \nYou are the WINNER! \nYour final hp is {hp}.')
else:
    print('Unfortunately, you have failed the FIVE-night adventure. \nBetter luck next time!')
print('Thank you for playing TERMINAL ADVENTURE! \nI hope you have enjoyed the game. \nGoodbye!')