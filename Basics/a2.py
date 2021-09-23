a=5
b=10



def addTwoNumbers(a1,a2):
    return a1+a2

def subtractTwoNumbers(a1,a2):
    if (a1>a2):
        return a1-a2
    else:
        return a2-a1

print ("Sum of two given numbers is ",addTwoNumbers(a,b))

print ("Difference of two given numbers is ",subtractTwoNumbers(a,b))