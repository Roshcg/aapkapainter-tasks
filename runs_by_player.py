input_list = [int(i) for i in input('enter comma separated list of runs: ').split(',')]


def calculate_individual_run():
    p1_run = 0
    p2_run = 0
    player1 = True
    for run in input_list:
        if player1:
            p1_run += run
        else:
            p2_run += run
        player1 = not player1 if (run & 1) else player1
    return p1_run, p2_run


if __name__ == '__main__':
    print(calculate_individual_run())
