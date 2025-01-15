# pcep_study_examples.py

# Example: Using a for loop to print numbers
for i in range(5):
    print(i)

# Example: Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Test the function
print(is_prime(7))  # Output: True
