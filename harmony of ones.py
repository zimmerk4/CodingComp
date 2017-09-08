def count(n, m):
    cnt = 0
    while min(n, m):
        cnt += (n & 1) & (m & 1)
        n >>= 1
        m >>= 1
    print(cnt)

with open("harmsub.txt") as harm:
    harm.readline()
    for line in harm:
        n, m = line.split(",")
        count(int(n), int(m))