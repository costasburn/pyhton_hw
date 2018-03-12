def chess_reward():
    total_reward = 1
    above_1mil = 0
    for i in range(1, 64):
        total_reward += 2 ** i
        if total_reward >= 1e6:
            above_1mil = i+1
            break
    return above_1mil, total_reward


print(chess_reward())
