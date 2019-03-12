import random
times = 3
secret = random.randint(1,10)
guess = 0
print ('猜猜我是几？',end = "")
while (guess != secret) and (times > 0):
    temp = input()
    guess = int(temp)
    times = times - 1
    if guess == secret:
        print('猜对了')
    else:
        if guess > secret:
            print('bigger')
        else:
            print('smaller')
        if times > 0:
            print('One more try: ',end = '')
        else:
            print('No chance')
print('Game Over')
