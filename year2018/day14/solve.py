def run(improve):
    cutoff = improve + 10
    board = [3, 7]
    bl = 2
    e0p = 0
    e1p = 1

    while bl < cutoff:
        e0s = board[e0p]
        e1s = board[e1p]
        combine = e0s + e1s

        if combine < 10:
            board.append(combine)
            bl += 1
        else:
            board.extend(divmod(combine, 10))
            bl += 2

        e0p = (e0p + e0s + 1) % bl
        e1p = (e1p + e1s + 1) % bl

    print("".join(str(x) for x in board[improve : improve + 10]))


run(880_751)
