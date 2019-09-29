import random

x=random.choice(["hand","foot","head","leg","arm","mom","dad","hello","the","book","look","this","the","he","she","think"])
count=life=4
print("The amount of letters in the words is")
print(len(x))
while count>0:
    print("guess a letter")
    n=input()
    t=0
    for s in x:
        if n == s:
            t = 1
        if n !=s :
            t=0
    if  t == 1:
        print("you guessed correctly")
        print(n)
    else:
        life -= 1
        print("you guessed incorrectly")
    if life == 0:
        count=0
print("the word was")
print(x)