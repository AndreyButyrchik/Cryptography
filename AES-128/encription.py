from keyExpansion import key_expansion
from addRoundKey import add_round_key
from subBytes import sub_bytes
from shiftRows import shift_rows
from mixColums import mix_columns

nr = 10  # count of rounds
nb = 4   # count of rows


def encrypt(input_bytes, key):
    if 0 < len(input_bytes) < 16:
        empty_spaces = 16 - len(input_bytes)
        input_bytes = bytearray(input_bytes)
        for i in range(empty_spaces - 1):
            input_bytes.append(0)
            input_bytes.append(1)
    state = [[] for i in range(4)]
    for r in range(4):
        for c in range(nb):
            state[r].append(input_bytes[r + 4 * c])

    key_schedule = key_expansion(key)

    state = add_round_key(state, key_schedule)

    rnd = 0
    for rnd in range(1, nr):
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, key_schedule, rnd)

    state = sub_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, key_schedule, rnd + 1)

    output = [0 for i in range(16)]
    for r in range(4):
        for c in range(4):
            output[r + 4 * c] = state[r][c]

    return bytes(output)
