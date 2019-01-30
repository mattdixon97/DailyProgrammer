def persistence(n, p=1):
    s = 0
    while n:
        s += n % 10
        n //= 10
    if s > 9:
        p += persistence(s,p)
    return p

