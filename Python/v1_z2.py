n = int(input())

if 100 <= n < 1000:
    print("troznamenkast")
else:
    print("nije troznamenkast")
    if n % 2 == 0:
        print("paran")
    else:
        print("neparan")
