import itertools

if __name__ == '__main__':
    n = itertools.product('0123456789', repeat=9)
    count = 0
    for i in n:
        count += 1
    print(count)
