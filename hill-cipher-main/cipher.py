from matrix import *
from utils import *

def encrypt(plaintext: str, K : list[list[int]], m: int = 26):
    n = len(K)
    ints = pad(text_to_ints(plaintext), n)

    blocks = [ints[i:i+n] for i in range(0, len(ints), n)]
    result = []
    for block in blocks:
        col = [[x] for x in block]
        enc_block = mat_mul_mod(K, col, m)
        result.extend([row[0] for row in enc_block])

    return ints_to_text(result)


def decrypt(ciphertext: str, K: list[list[int]], m: int = 26):
    n = len(K)
    K_inv = mat_inv_mod(K, m)
    ints = pad(text_to_ints(ciphertext), n)

    blocks = [ints[i:i+n] for i in range(0, len(ints), n)]
    result = []
    for block in blocks:
        col = [[x] for x in block]
        dec_block = mat_mul_mod(K_inv, col, m)
        result.extend([row[0] for row in dec_block])

    return ints_to_text(result)

