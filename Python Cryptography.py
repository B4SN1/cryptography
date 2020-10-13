
# Code Source: https://stackoverflow.com/a/8539470/11786261
# I do not claim the code.


import random


# Prime Generator
# (Just a sample, replace with a more sophisticated algorithm)
def generate_prime(N=10**8, bases=range(2,20000)):
    p = 1
    while any(pow(base, p-1, p) != 1 for base in bases):
        p = random.SystemRandom().randrange(N)
    return p


# Multiplicative Inverse
# http://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
def multinv(modulus, value):
    x, lastx = 0, 1
    a, b = modulus, value
    while b:
        a, q, b = b, a // b, a % b
        x, lastx = lastx - q * x, x
    result = (1 - lastx * modulus) // value
    return result + modulus if result < 0 else result


# Key Generator
# http://en.wikipedia.org/wiki/RSA
def generate(N):
    prime1 = generate_prime(N)
    prime2 = generate_prime(N)
    totient = (prime1 - 1) * (prime2 - 1)
    return prime1 * prime2, multinv(totient, 65537)
# Return: [Public Key, Private Key]


# Encrypt with public key
def encrypt(msg, pubkey):
    return pow(msg, 65537, pubkey)

# Decrypt with private key
def decrypt(coded, privkey, pubkey):
    return pow(coded, privkey, pubkey)



if __name__ == "__main__":
    public, private = generate(2**64)

    msg = 0xcafe

    print(hex(msg))
    # 0xcafe


    coded = encrypt(msg, public)
    decoded = decrypt(coded, private, public)

    print(msg == decoded)
    # True

    print(hex(decoded))
    # 0xcafe
