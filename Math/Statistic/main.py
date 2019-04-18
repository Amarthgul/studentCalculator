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
    pt2 = (round(z % 0.1, 3) - round(z % 0.01, 4));
    if closest: pt2 = (round(z % 0.1, 2))
    return chart.loc[[pt1]][[pt2]]

def cutPrecision(num, digAfterPt):
    '''My implementation of `round()`'''
    strVer = str(num)
    for i in range(len(strVer)):
        if strVer[i] == ".": index = i;
    strVer = strVer[:index + digAfterPt + 1]
    num = float(strVer)
    return num
    
def normalDist(z, closest = True):
    '''Standard normal distribution'''
    if z < -4.0: return 0 
    elif z == 0: return 0.5
    chart = loadPickle();
    pt1 = cutPrecision(z, 1)
    pt2 = abs((cutPrecision(Decimal(str(z)) % Decimal('0.1'), 2)))
    if closest and cutPrecision(Decimal(str(z)) % Decimal('0.01'), 3) > Decimal('0.05'):
        pt2 += 0.01;
    pt2 = float(pt2)
    return chart.loc[[pt1]][[pt2]].values[0][0]
    
def revNormalDist(prob, low = -3.99, high = 3.99, mid = 0):
    '''Reversed std normal distribution, given probablity, calculate z'''
    if (normalDist(mid + 0.01) > prob) and (normalDist(mid - 0.01) < prob):
        return cutPrecision(mid, 2)
    if (normalDist(mid) > prob):
        high = mid
    elif (normalDist(mid) < prob):
        low = mid 
    mid = (low + high) / 2;
    return revNormalDist(prob, low, high, mid)
    
def CI(precent, sigma, n, xHat):
    '''Confidence interval
Note that `precent` need to be samller than 1
    '''
    uniPart = revNormalDist((1 - precent)/2) * sigma / math.sqrt(n)
    return sorted([xHat - uniPart, xHat + uniPart])

def sampleNeedForCI(precent, sigma, w):
    '''Number of sample need for certain CI'''
    return (2 * revNormalDist((1 - precent)/2) * sigma / w) ** 2

def propCI(n, passed, precent):
    ''' CI for a population proportion p '''
    pHat = passed / n;
    zHalf = revNormalDist((1 - precent)/2)
    left = (pHat + zHalf**2 / (2*n)) / (1 + zHalf**2 / n)
    right = zHalf * (math.sqrt(pHat*(1-pHat)/n + (zHalf**2)/(4*n**2) ) / (1 + zHalf**2 / n))
    return sorted([left - right, left + right])

def propCIPlusFour(n, passed, precent):
    ''' CI Alternate version '''
    zHalf = revNormalDist((1 - precent)/2)
    p = (passed + 2) / (n + 4)
    right = zHalf * math.sqrt((p * (1-p)) / (n))
    return sorted([p - right, p + right])

def TCI(precent, stdev, n, mean, tCritical):
    ''' CI for T distribution '''
    right = tCritical * (stdev / math.sqrt(n))
    return sorted([mean - right, mean + right])

def PI(precent, stdev, n, mean, tCritical):
    ''' Prediction Interval '''
    right = tCritical * stdev * math.sqrt(1 + 1/n)
    return sorted([mean - right, mean + right])


class linearReg():
    def __init__(self, inDataX = [1, 2, 3, 4, 5], inDataY = [0, 1, 2, 3, 4]):
        self.dataX = np.array(inDataX);
        self.dataY = np.array(inDataY);
        self.meanX = np.average(self.dataX);
        self.meanY = np.average(self.dataY);
        self.n = len(self.dataX);
        self.__Sxx = self.Sxx();
        self.__Syy = self.Syy();
        self.__Sxy = self.Sxy();
        self.__betaH1 = self.betaH1();
        self.__betaH0 = self.betaH0();
        self.__yH = self.yH();
        self.__b1 = self.__betaH1; # alias of betaH1
        self.__b0 = self.__betaH0; # alias of betaH1
        self.__SSE = self.SSE();
        self.__SST = self.SST();
        self.__SSR = self.SSR();
        self.__sigmaH2 = self.sigmaH2();
        self.__s2 = self.s2();
        self.__r2 = self.r2();
        self.__vBetaH1 = self.vBetaH1();
        self.__stdBetaH1 = self.stdBetaH1();
        self.__r = self.r();
        self.__T = self.T();
    
    def Sxx(self):
        return sum((self.dataX - self.meanX) ** 2);
    def Syy(self):
        return sum((self.dataY - self.meanY) ** 2);
    def Sxy(self):
        return sum((self.dataY - self.meanY) * (self.dataX - self.meanX));
    
    def r(self):
        return self.__Sxy / (np.sqrt(self.__Sxx) * np.sqrt(self.__Syy));
    def betaH1(self):
        return self.__Sxy / self.__Sxx;
    def betaH0(self):
        return self.meanY - self.__betaH1 * self.meanX;
    def yH(self):
        return self.__betaH0 + self.__betaH1 * self.dataX;
    def yHi(self, i, enableRange = False):
        '''y value at position i'''
        if enableRange and (i > max(self.dataX) or i < min(self.dataX)):
            raise Exception("Cannot predict because out of range. ");
        return self.__betaH0 + self.__betaH1 * i;
    
    def SSE(self):
        '''Error sum of squares'''
        return sum((self.dataY - self.__yH) ** 2);
    def SST(self):
        '''Total sum of squares'''
        return self.__Syy;
    def SSR(self):
        '''Regression sum of squares'''
        return self.__SST - self.__SSE;
    def sigmaH2(self):
        return self.__SSE / (self.n - 2);
    def s2(self):
        return self.__sigmaH2;
    def r2(self):
        '''Coefficient of determination'''
        return 1 - self.__SSE / self.__SST;
    def r(self):
        '''Sample correlation coefficient'''
        return self.__Sxy / np.sqrt(self.__Sxx * self.__Syy)
    def vBetaH1(self):
        '''Variance of beta hat 1'''
        return self.__sigmaH2 / self.__Sxx;
    def stdBetaH1(self):
        '''Standard deviation of of beta hat 1'''
        return np.sqrt(self.__sigmaH2 / self.__Sxx)
    def T(self):
        return (self.__r*np.sqrt(self.n-2)) / (np.sqrt(1 - self.__r2))
    def CI(self, tValue):
        return [self.__betaH1 - tValue * self.__stdBetaH1, 
               self.__betaH1 + tValue * self.__stdBetaH1]
