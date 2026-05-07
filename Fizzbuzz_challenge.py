print ("Welcome to FizzBuzz!")
def fizzbuzz(n):
    if n % 3 == 0 and n % 7 == 0:
        return "FizzBuzz"
    elif n % 3 == 0 :
        return "Fizz"
    elif n % 7 == 0 :
        return "Buzz"
    elif "3" in str(n):
        return "Almost Fizz"
    else:
        return f"{n}"
number = int(input())

for i in range (1 , number + 1):
    print (fizzbuzz(i))

