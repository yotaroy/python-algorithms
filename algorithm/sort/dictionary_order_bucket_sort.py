from collections import deque


def dictionary_order_bucket_sort(arr):
    n = max([len(a) for a in arr])
    m = 9
    q = [deque([]) for _ in range(m+1)]

    ans = [i for i in arr]
    for i in reversed(range(n)):
        for a in ans:
            if len(a) <= i:
                q[0].append(a)
            else:
                q[a[i]].append(a)

        ans = []
        for j in range(m):
            while len(q[j]) > 0:
                ans.append(q[j].popleft())

    return ans


if __name__ == '__main__':
    import random

    x = [[random.randint(1, 9) for _ in range(random.randint(1, 6))] for _ in range(20)]
    print(x)
    print(dictionary_order_bucket_sort(x))
