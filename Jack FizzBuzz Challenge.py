def fizzbuzz_challenge():
    print("Hello and welcome to the fizz buzz challenge!")
    print("First we need to get a range sorted out!")

    start = int(input("Please provide a starting number for the range: "))
    end = int(input("Please enter an end number to this range: "))

    if start > end:
        print("Invalid range, please make sure the start of the range is lower than the end.")

    for num in range(start, end + 1):
        if num % 3 == 0 and num % 5 == 0: 
            print("Fuck me, Fizz Buzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

fizzbuzz_challenge()
