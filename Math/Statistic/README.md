# Intro #
This is a summary for the `Probability and Statistics for Engineering` course. Contains contents covered in my class (OSU STAT 3470), as some of the basic concepts are relatively easy, I skipped part of them. 

# Probability #

The **Sample Space** of an experiment, denoted by `S`, 
is the set of all possible outcomes of that experiment.  

An **Event** is any collection (subset) of outcomes contained in the sample space `S`. 
An event is simple if it consists of exactly one outcome and compound if it consists of more than one outcome.

1. The **Complement** of an event `A`, denoted by `A'`, is the set of all outcomes in `S` that are not contained in `A`.
2. The **Union** of two events `A` and `B`, denoted by `A ø B` and read “A or B,” is the event consisting of all outcomes that are either in `A` or in `B` or in both events (so that the union includes outcomes for which both `A` and `B` occur as well as outcomes for which exactly one occurs)—that is, all outcomes in at least one of the events.
3. The **Intersection** of two events `A` and `B`, denoted by `A U B` and read “A and B” is the event consisting of all outcomes that are in both A and B. 

When an _intersection results in no outcome_, we call it **Mutually Exclusive**. Note that mutually exclusive events _never happens together_, and mutually exclusive _does not mean dependent_. 

# Counting #

**factorial(n):**  
Calculate factorial of `n`  
```python  
factorial(6) # returns 720
```

**permu(k, n):**  
Permutation. Select `k` from `n`, with order.  
```python
permu(2, 10)  # returns 90
```

**comba(k, n):**  
Combination. Select `k` from `n`, without order.  
```python
comba(2, 10)  # returns 45
```

**sciConvert(num):**  
Convert a number into scientific format. Not in any STAT textbook.  
```python
sciConvert(12345)  # returns "123.4500 * 10 ^ 2"
sciConvert(12345, powerBase = 2, power = 10, precision = 6)  # returns "12.055664 * 2 ^ 10"
```

# Probability #

The **Conditional Probability** of `A` given that `B` has occured is:  
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/2_cp.gif">   

**Bayes’ theorem**
Let `A1, A2,…, Ak` be a collection of `k` mutually exclusive and exhaustive events 
with prior probabilities `P(Ai) (i = 1, …, k)`. Then for any other event `B` for
which `P(B) > 0`, the _posterior_ probability of `Aj` given that B has occurred is:  
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/2_cp.gif">   

**Independent**  
&nbsp; Two events `A` and `B` are independent if `P(A|B) = P(A)` and are dependent otherwise.   
&nbsp; `A` and `B` are independent if and only if (iff) `P(A ∩ B) = P(A) • P(B)`  
&nbsp; Verificatio: `P(A ∩ B) = P(A|B) • P(B) = P(A) • P(B)`

# Discrete Random Variables and Probability Distributions #

**Random Variables (rv)** is any rule that associates a number with each outcome in `S`.

Any random variable whose only possible values are `0` and `1` is called a **Bernoulli random variable**.

**bino(x, n, p):**  
Binomial porbablity.  
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/binomial.gif">  
```python
bino(2, 4, 0.8) # returns 0.15359999999999996
```

**pois(x, mu, useMathPkg = False):**  
Poisson distributation.  
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/possion.gif">  
```python
pois(0, 3) #returns 0.04978706836786395
```

**unifDist**  
Class of uniform distribution.  
```python
a = unifDist(0.5, 2)         # starts at 0.5, ends at 2
a.probBetween(0.75, 1.25)    # returns 0.3333333333333333 
a.probAbove(0.75)            # returns 0.8333333333333333
a.probBelow(0.75)            # returns 0.1666666666666666
a.probBelow(0.25)            # returns 0
```

**normalDist(z, closest = True)**  
Return the standard normal distribution value. `closest` controls whether to round down or find the cloest vlaue  
```python
normalDist(0.236)                   # rounded as 0.24, returns 0.59483
normalDist(0.236, closest = False)  # rounded to 0.23, returns 0.59095
```

# Statistical Intervals #

**CI(precent, sigma, n, xHat)**  
Find the confidence interval with given conditions. Note that although the 1st parameter is called `precent`, it requires a number in [0, 1].  
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/CI.gif">  
```python
CI(0.99, 3.3, 100, 52.2)            # returns [51.348600000000005, 53.0514]
```

**sampleNeedForCI(precent, sigma, w)**  
Complute number of samples needed for a certain CI.  
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/sampleNeeded.gif">  
```python
sampleNeedForCI(0.99, 3.3, 1)      # returns 289.95278399999995
```

**propCI(n, passed, precent)**

CI for a population proportion p

<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/popuPropCI.gif">

**TCI(precent, stdev, n, mean, tCritical)**    
CI for t-distribution. Currently need the user enter t-critical value.  
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/TCI.gif">  

**PI(precent, stdev, n, mean, tCritical)**  
Prediction Interval. Currently need the user enter t-critical value.      
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/PI.gif">  

# Simple Linear Regression and Correlation #

**Model equation**  
Simple Linear Regression Model equation:  
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/12_1_1.gif">  
```python
# initlize a linear regression model
lnrModel = linearReg([1, 2, 3, 4, 5], [0.92, 2.03, 2.94, 4.10, 5.01]);
```

**self.Sxx()**  
Sum of the squares of the difference between each `x` and the _mean_ `x` value.  
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/12_sxx.gif">  
```python
lnrModel.Sxx()            # returns 10.0 in this case
```

**self.Syy()**  
Sum of the squares of the difference between each `y` and the _mean_ `y` value.  
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/12_syy.gif"> 
```python
lnrModel.Syy()            # returns 10.520 in this case
```

**self.Sxy()**  
Sum of the product of the difference between `x` its _means_ and the difference between `y` and its _mean_.  
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/12_sxy.gif">    
```python
lnrModel.Sxy()            # returns 10.25 in this case
```

**self.betaH1()**  
The x coefficient  
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/12_bh1.gif">  
```python
lnrModel.betaH1()            # returns 1.025 in this case
```

**self.betaH0()**  
The constant coefficient  
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/12_bh0.gif">    
```python
lnrModel.betaH0()            # returns -0.0750 in this case
```

