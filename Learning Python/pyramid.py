def printTriangle():
    row = int(input("Enter the number of rows: "))
    if(row>=10 or row <= 3):
        print("Enter a Value less than 10 and Greater than 3")
    else: 
        for i in range(row, 0, -1):
            for k in range(row - i):
                print(" ", end="")
            for j in range(i):
                print(f"{chr(65+j)} ", end="")
                # chr() is used to iterate/loop/skip over character encoding.
            print()

printTriangle()