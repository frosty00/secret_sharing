import os
import sympy
import functools
import operator
import math
import random

random = random.SystemRandom()

SHARED_SECRETS = 2
TOTAL_SECRETS = 5

# https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt
WORDLIST_FILENAME = 'bip-0039.txt'

# https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-4.pdf
# Curve P-384
prime_field = (2 ** 384) - (2 ** 128) - (2 ** 96) + (2 ** 32) - 1

with open(WORDLIST_FILENAME, 'r') as f:
    WORDLIST = f.read().split('\n')

SIZE = int(math.log2(len(WORDLIST)))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({hex(self.x)[2:]}, {hex(self.y)[2:]})'


def encode_secret(secret_indexes: list[int], shared_secrets: int, total_secrets: int) -> list[Point]:
    assert shared_secrets <= total_secrets
    # encode secret as an integer
    as_bits = ''.join(bin(index)[2:].rjust(SIZE, '0') for index in secret_indexes)
    secret_integer = int(as_bits, base=2) % prime_field
    points = []
    # generate a random equation that is at most of degree shared_secrets - 1
    degree = shared_secrets - 1
    random_bytes = os.urandom(degree * 32)
    equation = []
    for i in range(0, len(random_bytes), 32):
        equation.append(int.from_bytes(random_bytes[i:i+32], 'big'))
    equation.append(secret_integer)
    for _ in range(1, total_secrets + 1):
        x = random.randrange(0, prime_field)
        # apply the equation on each point
        y = sum(x ** (degree - i) * coefficient for i, coefficient in enumerate(equation))
        points.append(Point(x, y % prime_field))
    return points


def decode_secret(secrets: list[Point]):
    def reduce(variable, xs):
        return functools.reduce(operator.mul, [variable - value for value in xs])
    secrets_by_x = {}
    for secret in secrets:
        assert secret.x > 0
        secrets_by_x[secret.x] = secret.y
    x_symbol = sympy.Symbol('x')
    equation = 0
    for x, y in secrets_by_x.items():
        copy = secrets_by_x.copy()
        del copy[x]
        equation = equation + reduce(x_symbol, copy) * sympy.invert(reduce(x, copy), prime_field) * y
    # solution_equation = sympy.simplify(equation)
    integer_solution = int(equation.subs(x_symbol, 0)) % prime_field
    bytes_solution = bin(integer_solution)[2:].rjust(SIZE * 24, '0')
    indexes = [int(bytes_solution[i:i + SIZE], base=2) for i in range(0, len(bytes_solution), SIZE)]
    private_key_array = [WORDLIST[i] for i in indexes]
    private_key = ' '.join(private_key_array)
    return private_key


if __name__ == '__main__':

    indexes = random.sample(range(len(WORDLIST)), k=24)
    private_key_array = [WORDLIST[i] for i in indexes]
    private_key = ' '.join(private_key_array)

    print('PRIVATE KEY:')
    print(private_key, '\n')

    print(f'encoding private_key as a shared secret {SHARED_SECRETS} of {TOTAL_SECRETS}')

    encoded = encode_secret(indexes, SHARED_SECRETS, TOTAL_SECRETS)

    print(f'encoded private key as {len(encoded)} points on a polynomial')

    print('\n---\n')
    print(*encoded, sep='\n\n\n\n')
    print('\n---\n')

    print(f'selected {SHARED_SECRETS} points to recover the private key')
    print('\n---\n')
    recovered_points = random.sample(encoded, SHARED_SECRETS)
    print(*recovered_points, sep='\n\n\n\n')
    print('\n---\n')

    decoded = decode_secret(recovered_points)
    print('RECOVERED KEY:')
    print(decoded)
