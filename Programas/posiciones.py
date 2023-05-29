def main():
    m,n = input().split(",")
    m = int(m)
    n = int(n)
    for i in range(m):
        for j in range(n):
            print(str(i) + "," + str(j), end = " ")
        print()
main()
