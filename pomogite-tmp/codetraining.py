# CODE TRAINING

# high and low
def high_and_low(numbers):
    numbers = numbers.split()
    numbers = [int(i) for i in numbers]
    return str(max(numbers))+" "+str(min(numbers))

#high_and_low("1 2 3 4 5")  # return "5 1"


# playing with digits
def dig_pow(n, p):
    num = str(n)
    total = sum([int(num[i]) ** (p + i) for i in range(len(num))])
    return total / n if (total % n) == 0 else -1

# dig_pow(89, 1) #should return 1 since 8¹ + 9² = 89 = 89 * 1



# tribbonacci seq
def tribonacci(signature, n):
    if n == 0:
        return []
    if n < 3:
        return [signature[i] for i in range(0,n)]
    res = signature[:]
    for i in range(3,n):
        res.append(res[i-1] + res[i-2] + res[i-3])
    return res
# other version
'''def tribonacci(signature,n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))
    
    return signature[:n]'''

# tribonacci([1, 1, 1], 10), [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]



# Regex validate PIN code
import re
def validate_pin(pin):
    if re.fullmatch("\d{4}|\d{6}", pin):
        return True
    else:
        return False
'''
def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()'''

'''
def validate_pin(pin):
    if len(pin) in (4, 6):
        try:
            pin = int(pin)
            return True
        except:
            return False
    else:
        return False'''

# validate_pin("12345"),False, "Wrong output for '12345'"



# find the odd int
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
# find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5

