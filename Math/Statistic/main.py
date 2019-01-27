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

def sciConvert(num, powerBase = 2, power = 10, precision = 4):
    '''Convert a number into scientific format. 
num: number to be converted;
powerBase: the base of power;
power: just power... generally _powerBase_ to the power of _power_;
precision: if there's float point, then count number after the float point.
    '''
    result = ""
    base = str(num / (powerBase ** power)) + "0" * precision
    if base.find("."):
        base = base[base.find("."): base.find(".") + precision + 1]
    else: base = base[: precision]
    result += base + " * " + str(powerBase) + " ^ " + str(power)
    return result
