def fizzbuzz_plus(n):
    for x in range(1, n ):
        if x % 3 == 0 and x % 7 == 0:
            print("FizzSeven")
        elif x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        elif x % 7 == 0:
            print("Seven")
        else: 
            print(x)

        
fizzbuzz_plus(22)