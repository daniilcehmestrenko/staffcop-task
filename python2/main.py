def main():
    stack = [(1000, 1000)]
    max_digit_sum = 25
    field_covered = set()
    count = 0

    while stack:
        x, y = stack.pop()
        if (x, y) in field_covered:
            continue
        field_covered.add((x, y))
        if sum_digits(x) + sum_digits(y) > max_digit_sum:
            continue
        stack.append((x + 1, y))
        stack.append((x, y + 1))
        stack.append((x - 1, y))
        stack.append((x, y - 1))
        count += 1
    print(count)


def sum_digits(number):
    return sum(map(int, str(number)))


if __name__ == '__main__':
    main()
