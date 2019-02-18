#!/usr/bin/env python3

from random import SystemRandom
import subprocess

# Modular exponentiation
def mod_exp(x, y, N):
    if N == 1:
        return 0
    result = 1
    x = x % N
    while y > 0:
        if (y % 2 == 1):
            result = (result * x) % N
        y >>= 1
        x = (x * x) % N
    return result

# Generate a cryptographically strong prime p where (p-1)/2 is also prime
def generate_p():
    rounds = 0
    prime_found = False
    while not prime_found:
        rounds += 1
        # Generate 512-bit prime with OpenSSL
        cmd = 'openssl prime -generate -bits 512'
        proc = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, close_fds=True)
        prime = proc.stdout.read().decode("utf-8")
        prime = int(prime[:-1])

        # Calculate p and check for primality with OpenSSL
        p = int ((prime * 2) + 1 )
        is_prime = 0
        cmd = 'openssl prime -checks 20 ' + str(p)
        proc = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, close_fds=True)
        output = proc.stdout.read().decode("utf-8")
        output = output[:-1]
        words = output.split(" ")
        is_prime = words[-2] != 'not'

        # Return p if it is prime
        if is_prime:
            prime_found = True
            #print(rounds)
            return p

# Generate random 512-bit number through os.urandom()
def generate_a():
    return int(SystemRandom().random() * (2**512))

# For debug mode of the passoff
def debug():
    p = generate_p()
    a = generate_a()
    g = 5
    ga = mod_exp(g, a, p)
    print("p:\t", p)
    print("g^a:\t", ga)

    b = 1998286638065473057944506344030256054916203227381748916180906390214373930105605405985818224246280726328877245115163209963634633681313092395058312190549
    gb = mod_exp(g, b, p)
    print("g^b:\t", gb)

    gab = mod_exp(ga, b, p)
    gba = mod_exp(gb, a, p)
    print("g^ab:\t", gab)

    assert(gab == gba)

# Diffie-Hellman passoff routine
def passoff():
    # Generate initial numbers
    a = generate_a()
    print("a:\t", a)
    g = 5
    p = generate_p()
    print("p:\t", p)
    # Caluclate g^a mod p
    ga = mod_exp(g, a, p)
    print("g^a:\t", ga)
    # Read g^b mod p
    gb = input("g^b:\t ")
    gb = int(gb)
    # Calculate secret
    gab = mod_exp(gb, a, p)
    print("g^ab:\t", gab)

passoff()