from random import randrange
number = randrange(0, 100)

while True:
    i = int(input('Inter a Number: '))
    if i == number:
        print('Ok! The Number is ' + str(i))
        break
    elif i < number:
        print('Your Number Lower Than Our Number')
    else:
        print('Your Number Greater Than Our Number')
