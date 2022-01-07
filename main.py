# Write a Python Program to convert decimal to binary using recursion 
def dtb(n):
    if n > 1:
        dtb(n//2)
    print(n%2, end = "")


number = int(input())
dtb(number)
