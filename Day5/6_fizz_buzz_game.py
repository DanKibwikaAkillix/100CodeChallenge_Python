total = 0
for i in range(1,101):
    total =i

    if i % 5 ==0 and i % 3==0:
        i = "FizzBuzz"
    elif i % 3 ==0:
        i = "Fizz"
    elif i % 5 == 0:
        i = "Buzz"
    else:
        i = i
    print(i)