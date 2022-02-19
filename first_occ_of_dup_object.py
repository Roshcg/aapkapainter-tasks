unique_list = []
input_list = input('enter comma separated list elements: ').split(',')


def first_duplicate():
    for item in input_list:
        if item in unique_list:
            return item
        unique_list.append(item)


if __name__ == '__main__':
    print(first_duplicate())
