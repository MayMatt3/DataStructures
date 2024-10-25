def get_input():
    s1 = input("Enter the first string: ")
    s2 = input("Enter the second string: ")
    return s1, s2


def uncommonConcat(s1, s2):
    set1 = set(s1)
    set2 = set(s2)

    set3 = set1.intersection(set2)

    result = []

    for char in s1:
        if char not in set3:
            result.append(char)

    for char in s2:
        if char not in set3:
            result.append(char)

    return ''.join(result)


def main():
    s1, s2 = get_input()
    result = uncommonConcat(s1, s2)
    print("Results:", result)


main()
