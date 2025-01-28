#%%
def sieve_of_eratosthenes(n):
    """Generate all prime numbers less than n using Sieve of Eratosthenes"""
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    
    return [i for i in range(n) if primes[i]]

def makeArrayIncreasing(nums):
    n = len(nums)
    if n <= 1:
        return True
        
    # Get all possible prime numbers less than 1001
    all_primes = sieve_of_eratosthenes(1001)
    
    # For each index i, store the minimum possible value we can achieve
    # after subtracting a prime number less than nums[i]
    min_possible = nums.copy()
    
    for i in range(n):
        # Find all primes less than nums[i]
        valid_primes = [p for p in all_primes if p < nums[i]]
        if valid_primes:
            # The minimum value we can achieve is by subtracting the largest valid prime
            min_possible[i] = nums[i] - valid_primes[-1]
    
    # Check if we can make the array strictly increasing
    for i in range(n - 1):
        curr_min = min_possible[i]
        next_min = min_possible[i + 1]
        
        # If current minimum value is >= next minimum value,
        # it's impossible to make strictly increasing
        if curr_min >= next_min:
            return False
            
        # If original values are already in strictly increasing order,
        # no need to change them
        if nums[i] < nums[i + 1]:
            min_possible[i] = nums[i]
    
    return True
#%%
# Test cases
test_cases = [
    [4, 9, 6, 10],
    [6, 8, 11, 12],
    [5, 8, 3]
]
#%%
for nums in test_cases:
    result = makeArrayIncreasing(nums)
    print(f"Input: {nums}")
    print(f"Output: {result}\n")
# %%
