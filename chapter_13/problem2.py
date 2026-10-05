def divisible5(n):
    if(n%5 ==0):
        return True
    return False

a = [2, 10,32,434,536,64654,7677225,24555,250]

f = list(filter(divisible5,a))
print(f)






