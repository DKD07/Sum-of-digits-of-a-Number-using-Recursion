def Sum_of_digits(n):
    if n<10:
        return n
    else:
        return n%10 + Sum_of_digits(n//10)
x=int(input("Enter the non-negative number: "))
print("The sum of non-negative integer is: ",Sum_of_digits(x))
