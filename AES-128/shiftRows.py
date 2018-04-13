nb = 4   # count of rows


def left_shift(state, count):
    return state[count % len(state):len(state)] + state[:count % len(state)]


def right_shift(state, count):
    return state[len(state) - (count % len(state)):] + state[:len(state) - (count % len(state))]


def shift_rows(state, inv=False):
    count = 1

    if not inv:  # encrypting
        for i in range(1, nb):
            state[i] = left_shift(state[i], count)
            count += 1
    else:  # decryption
        for i in range(1, nb):
            state[i] = right_shift(state[i], count)
            count += 1

    return state
