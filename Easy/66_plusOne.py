def plusOne( digits=[6,1,4,5,3,9,0,1,9,5,1,8,6,7,0,5,5,4,3]):
    number = 0
    pw = len(digits)
    for k, v in enumerate(digits):
        number += v* 10 ** (pw-1)
        pw -= 1

    number += 1
    number=str(number)
    print(number)
    numberlist=[]
    for char in number:
        numberlist.append(char)
    return numberlist
def plusOne1( digits=[6,1,4,5,3,9,0,1,9,5,1,8,6,7,0,5,5,4,3,6,1,4,5,3,9,0,1,9,5,1,8,6,7,0,5,5,4,3,6,1,4,5,3,9,0,1,9,5,1,8,6,7,0,5,5,4,3]):
    numbers = [str(x) for x in digits]
    output = str(int("".join(numbers)) + 1)
    return [int(char) for char in output]

def plusOne_BigNumber(digits=[9]):
    carry=1
    for i in range(len(digits)-1,-1,-1):
        temp=digits[i]+1
        d,m=divmod(temp,10)
        if d==0:
            digits[i]=temp
            break
        else:
            digits[i]=m
    if digits[0]==0:
        digits.insert(0,1)
    return digits
if __name__=="__main__":
    print(plusOne_BigNumber())
