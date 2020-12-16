# INITIAL INPUTS OF ALPHA AND BETA
MAX = 9999
MIN = -9999


def minimax(depth, node_i, max_p, input, alpha, beta):
    # IF LEAF NODE IS REACHED

    if depth == 3:
        return input[node_i]

    if max_p:

        optimal = MIN

        # CHECK FOR LEFT AND RIGHT CHILD
        for i in range(0, 2):

            val = minimax(depth + 1, node_i * 2 + i, False, input, alpha, beta)
            optimal = max(optimal, val)
            alpha = max(alpha, optimal)

            # check for alpha beta pruning
            if beta <= alpha:
                break

        return optimal

    else:
        optimal = MAX

        # CHECK FOR LEFT AND RIGHT CHILD
        for i in range(0, 2):

            val = minimax(depth + 1, node_i * 2 + i, True, input, alpha, beta)
            optimal = min(optimal, val)
            beta = min(beta, optimal)

            # ALPHA BETA PRUNING
            if beta <= alpha:
                break

        return optimal


inputs = []
print('Enter Number of Values:')
n = int(input())
for i in range(0, n):
    print('Enter value {0}'.format(i+1))
    a = int(input())
    inputs.append(a)

print("The final value after alpha beta pruning is :", minimax(0, 0, True, inputs, MIN, MAX))
