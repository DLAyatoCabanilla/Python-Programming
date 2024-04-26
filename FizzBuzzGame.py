for fizzBuzz in range(1, 101):
    if fizzBuzz % 3 == 0 and fizzBuzz % 5 == 0:
        print("FizzBuzz")
    elif fizzBuzz % 3 == 0:
        print("Fizz")
    elif fizzBuzz % 5 == 0:
        print("Buzz")
    else:
        print(fizzBuzz)

    # target = 100
    # for number in range(1, target + 1):
    #     if number % 3 == 0 and number % 5 == 0:
    #         print("FizzBuzz")
    #     elif number % 3 == 0:
    #         print("Fizz")
    #     elif number % 5 == 0:
    #         print("Buzz")
    #     else:
    #         print(number)

