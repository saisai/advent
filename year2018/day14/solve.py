def run(puzzle):
    improve = None
    improve_start = int(puzzle)
    improve_end = improve_start + 10
    appear = None
    digits = tuple(int(c) for c in puzzle)
    digit_gen = iter(digits)
    board = [3, 7]
    board_length = 2
    e0p = 0
    e1p = 1

    while improve is None or appear is None:
        e0s = board[e0p]
        e1s = board[e1p]
        combine = e0s + e1s

        if combine < 10:
            values = (combine,)
        else:
            values = divmod(combine, 10)

        for x in values:
            n = next(digit_gen, None)

            if n is None:
                appear = board_length - len(digits)
            elif n != x:
                digit_gen = iter(digits)

            board.append(x)
            board_length += 1

        e0p = (e0p + e0s + 1) % board_length
        e1p = (e1p + e1s + 1) % board_length

        if improve is None and board_length >= improve_end:
            improve = "".join(str(x) for x in board[improve_start:improve_end])

    print(improve)
    print(appear)


run("880751")
