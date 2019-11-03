# 最大公約数を求める
def gcd(x, y):
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    return gcd(y, x % y)

# 再帰を使わないバージョン
def gcd2(x, y):
    if x < y:
        x, y = y, x
    while y != 0:
        r = x % y
        x = y
        y = r
    return x


if __name__ == '__main__':
    problems = [(60, 36), (1085, 1015)]
    print('最大公約数を求めるアルゴリズム')

    for a, b in problems:
        print('{}と{}の最大公約数は{}'.format(a, b, gcd(a, b)))
        print('{}と{}の最大公約数は{}'.format(a, b, gcd2(a, b)))
