import random 

# Check if a number is prime.
def is_prime(num: int):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+ 1):
        if num % i == 0:
            return False
    return True

# Generate a prime. 
def generate_prime(start: int, end: int):
    while True:
        num = random.randint(start, end)
        if is_prime(num):
            return num

#TODO: Implement Euclidian extended algo here. 
def gcd_extended(a: int, b: int):
    pass 


# Generate d, the modular inverse of e mod phi(n).
def modular_inverse(e: int, phi: int):
    #TODO: Use gcd_extended to find modular inverse. 
    pass


# TODO: Check such that p and q cannot be equal. 
p = generate_prime(2,10**6)
q = generate_prime(2,10**6)

# Generate n, e(Public key) and d(Private key).
n = p * q 

e = 65537

# Private key 


# Calculate n and Euler's totient of n. 
phi_of_n = (p - 1) * (q - 1)

print(f"p: {p}, q: {q}")
print(f"n: {n}")
print(f"Eulers Totient: {phi_of_n}")



    
