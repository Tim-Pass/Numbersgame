
import random






num = random.randint(1, 100)
name = input("what is your name?:  ")
guess = 0
lives = 20
wins = 0
desire = 0
wave = 1
waves = ("you are on round:%d" % wave)
highscores = "numbergame"

accounts = open("accounts", "r")
check = accounts.read().split(",")

username = input("Enter your username:  ")
psswd = input("Enter your password:  ")
print(check)
if (username in check) and (psswd in check):
    admin = 0
else:
    admin = 1




while admin == 0:
    print("Welcome admin")
    choice = input("what would you like todo? viewscores or play:  ")
    if choice == "viewscores":
        sf = open(highscores,'r')
        showscores = sf.read()
        print(showscores)
    elif choice == "play":
        admin = 1






while (desire == 0):
    guess = input("guess:  ")
    if int(guess) == num:
        print("Congrats %s you won!" % name)
        wins = wins + 1
        lives = lives + 10
        print("you have %d wins" % wins)
        playagain = input("do you want to play again?:  ")
        if playagain.lower() == "no":
            sf = open(highscores,"a+")
            sf.write("\n-%s:%s-\n " % (name, wins))
            sf.close()
            desire = desire + 1
            viewscores = input("do you want to see the highscores?  ")
            if viewscores.lower() == "yes":
                sf = open(highscores,'r')
                showscores = sf.read()
                print(showscores)
            else:
                print("Goodbye %s" % name)
        else:
            num = random.randint(1, 100)
            wave = wave + 1
            waves = ("you are on round:%d" % wave)
            print(waves)
    elif guess != num:
        print("try again")
        lives = lives - 1
        print(lives)
        if int(guess) > num:
            print("you are too high")
        elif int(guess) < num:
            print("you are too low")

        