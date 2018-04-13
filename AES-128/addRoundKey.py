nb = 4   # count of rows
nk = 4


def add_round_key(state, key_schedule, round=0):
    for col in range(nk):
        # nb*round is a shift which indicates start of a part of the KeySchedule
        s0 = state[0][col] ^ key_schedule[0][nb * round + col]
        s1 = state[1][col] ^ key_schedule[1][nb * round + col]
        s2 = state[2][col] ^ key_schedule[2][nb * round + col]
        s3 = state[3][col] ^ key_schedule[3][nb * round + col]

        state[0][col] = s0
        state[1][col] = s1
        state[2][col] = s2
        state[3][col] = s3

    return state
