print("Pattern-1 Star Triangle")
for r in range(1,6):
    for c in range(0,r):
        print("*",end="")
    print()


print("Pattern-2 Number Triangle")
n=5
for row in range(1,n+1):
    for col in range(row):
        print(col,end="")
    print()


print("Pattern-3 Inverted Star Triangle")
for r in range(6,0,-1):
    for c in range(0,r):
        print("*",end="")
    print()


print("Pattern-4 Pyramid")
for row in range(1,n+1):
    for col in range(n-row):
        print(" ",end="")
    for col in range(2*row-1):
        print("*",end="")
    print()