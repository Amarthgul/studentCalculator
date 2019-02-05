def factorial(input):
    result = 1;
    for i in reversed(range(input)):
        result *= (i + 1);
    return result;

def permu(k, n): 
    '''Permutation. Select k from n, with order. '''
    return factorial(n) / factorial(n - k);
def comba(k, n):
    '''Combination. Select k from n, without order. '''
    return factorial(n) / (factorial(n - k) * factorial(k));

def bino(x, n, p):
    '''Binomial porbablity'''
    return comba(x, n) * p ** x * (1 - p) ** (n - x)
def pois(x, mu, useMathPkg = False):
    '''Poisson distributation'''
    if useMathPkg: import math;
    E = 2.718281828459045 if not useMathPkg else math.exp(1);
    return E ** (-mu) * mu ** x / factorial(x)



def sciConvert(num, powerBase = 10, power = 2, precision = 4):
    '''Convert a number into scientific format. 
num: number to be converted;
powerBase: the base of power;
power: just power... generally _powerBase_ to the power of _power_;
precision: if there's float point, then count number after the float point.
    '''
    result = ""
    base = str(num / (powerBase ** power)) + "0" * precision
    if base.find("."):
        base = base[0: base.find(".") + precision + 1]
    else: base = base[: precision]
    result += base + " * " + str(powerBase) + " ^ " + str(power)
    return result
