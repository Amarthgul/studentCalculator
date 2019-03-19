import math
import pandas as pd
import pickle

def loadPickle():
    with open('chart.pkl', 'br') as f:
        dataSet = pickle.load(f)
    return dataSet


def factorial(input):
    '''Compute factorial of a non-negtative number'''
    if input < 0: return 0;
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

class unifDist():
    def __init__(self, start = 0, end = 1):
        self.__start = start;
        self.__end = end;
        self.__prob = 1 / (end - start);
    def probBetween(self, start, end):
        start = start if (start >= self.__start) else self.__start;
        end = end if (end <= self.__end) else self.__end;
        return (end - start) * self.__prob
    def probAbove(self, num):
        if num >= self.__end: return 0;
        else: return (self.__end - num) * self.__prob;
    def probBelow(self, num):
        if num <= self.__start: return 0;
        else: return (num - self.__start) * self.__prob;
    def expectation(self):
        return (self.__end + self.__start) / 2;
    def variance(self):
        return (self.__end - self.__start)**2 / 12;
    def stdev(self):
        return math.sqrt(self.variance())

def normalDist(z, closest = True):
    if z < -4.0: return 0 
    chart = loadPickle();
    pt1 = round(z, 1);
    if closest:
        pt2 = round(z % 0.1, 2) + 0.01 if (round(z % 0.1, 3) > 0.05) else round(z % 0.1, 2);
    else:
        pt2 = round(z % 0.1, 2)
    return chart.loc[[pt1]][[pt2]]
