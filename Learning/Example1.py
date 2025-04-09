def factorial(n):
    """
    Calculate the factorial of a number using recursion.
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def main():
    try:
        num = int(input("Enter a positive integer: "))
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            print(f"The factorial of {num} is {factorial(num)}")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()