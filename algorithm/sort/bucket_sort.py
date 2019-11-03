from collections import deque


def bucket_sort(arr):
    n = len(arr)
    m = max(arr)
    q = [deque([]) for _ in range(m+1)]

    for i in range(n):
        q[arr[i]].append(arr[i])

    ans = []
    for j in range(m):
        while len(q[j]) > 0:
            ans.append(q[j].popleft())

    return ans

if __name__ == '__main__':
    import random

    x = [random.randint(1, 30) for _ in range(100)]
    print(x)
    print(bucket_sort(x))
