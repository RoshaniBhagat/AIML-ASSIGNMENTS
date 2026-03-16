'''Assignment (17/02/2026) 
Assignment Name : Logic Builder Description : Print numbers 1–50 with Fizz/Buzz logic and count occurrences using loops and functions.'''


def fizz_buzz_logic():
    fizz_count = 0
    buzz_count = 0
    fizzbuzz_count = 0
    total_numbers = 0

    print("="*30)
    print(" Number        Result")
    print("="*30)

    for num in range(1, 51):
        total_numbers += 1

        if num % 3 == 0 and num % 5 == 0:
            result = "FizzBuzz"
            fizzbuzz_count += 1
        elif num % 3 == 0:
            result = "Fizz"
            fizz_count += 1
        elif num % 5 == 0:
            result = "Buzz"
            buzz_count += 1
        else:
            result = num

        print(f"{num:<13} {result}")

    print("="*30)

    return fizz_count, buzz_count, fizzbuzz_count, total_numbers


fizz, buzz, fizzbuzz, total = fizz_buzz_logic()

print("\nSummary Report")
print("-"*30)
print("Total Numbers Processed :", total)
print("Fizz Count              :", fizz)
print("Buzz Count              :", buzz)
print("FizzBuzz Count          :", fizzbuzz)