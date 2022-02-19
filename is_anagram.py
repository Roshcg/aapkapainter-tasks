strings = input('enter the strings: ').split()
str1, str2 = strings[0], strings[1]


def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return 'No'
    for i in str1:
        if i in str2:
            str2.replace(i, '')
            continue
        return 'No'
    return 'Yes'


if __name__ == '__main__':
    print(is_anagram(str1.lower(), str2.lower()))
