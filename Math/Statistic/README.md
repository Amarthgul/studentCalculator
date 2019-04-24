# Intro #
This is a summary for the `Probability and Statistics for Engineering` course. Contains contents covered in my class (OSU STAT 3470), as some of the basic concepts are relatively easy, I skipped part of them. 

# Probability #

The **Sample Space** of an experiment, denoted by `S`, 
is the set of all possible outcomes of that experiment.  

An **Event** is any collection (subset) of outcomes contained in the sample space `S`. 
An event is simple if it consists of exactly one outcome and compound if it consists of more than one outcome.

1. The **Complement** of an event `A`, denoted by `A'`, is the set of all outcomes in `S` that are not contained in `A`.
2. The **Union** of two events `A` and `B`, denoted by `A U B` and read “A or B,” is the event consisting of all outcomes that are either in `A` or in `B` or in both events (so that the union includes outcomes for which both `A` and `B` occur as well as outcomes for which exactly one occurs)—that is, all outcomes in at least one of the events.
3. The **Intersection** of two events `A` and `B`, denoted by `A ∩ B` and read “A and B” is the event consisting of all outcomes that are in both A and B. 

When an _intersection results in no outcome_, we call it **Mutually Exclusive**. Note that mutually exclusive events _never happens together_, and mutually exclusive _does not mean dependent_. 

**factorial(n):**  
Calculate factorial of `n`  
```python  
factorial(6) # returns 720
```

**Permutation.**  
`permu(k, n)`: select `k` from `n`, with order.    
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/2_pm.gif">  
```python
permu(2, 10)  # returns 90
```

**Combination**  
`comba(k, n)`: select `k` from `n`, without order.    
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/2_cb.gif">  
```python
comba(2, 10)  # returns 45
```

**sciConvert(num):**  
Convert a number into scientific format. Not in any STAT textbook.  
```python
sciConvert(12345)  # returns "123.4500 * 10 ^ 2"
sciConvert(12345, powerBase = 2, power = 10, precision = 6)  # returns "12.055664 * 2 ^ 10"
```

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

**Expected Value**   
That Greek character is pronounced as `mu`.  
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/3_exp.gif"> 

**Variance**   
The expectation of the squared deviation of a random variable from its mean. That character is pronounced as `sigma`   
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/3_vr.gif"> 

**Standard Deviation (SD)**   
Is a measure that is used to quantify the amount of variation or dispersion of a set of data values. Calculated from the square root of variance.    
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/3_stdev.gif"> 

**Binomial Distributation**   
`bino(x, n, p)`: `x`: number of succeed; `n`: total number of trials; `p`: probability.   
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/binomial.gif">  
```python
bino(2, 4, 0.8) # returns 0.15359999999999996
```

**Poisson distributation**   
`pois(x, mu, useMathPkg = False)`   
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/possion.gif">   
```python
pois(0, 3) #returns 0.04978706836786395
```

**Uniform Distribution**   
Class of `unifDist`  
```python
a = unifDist(0.5, 2)         # starts at 0.5, ends at 2
a.probBetween(0.75, 1.25)    # returns 0.3333333333333333 
a.probAbove(0.75)            # returns 0.8333333333333333
a.probBelow(0.75)            # returns 0.1666666666666666
a.probBelow(0.25)            # returns 0
```

**Normal Distribution**  
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/2_nmd.gif" width="100">  

**Standard Normal Distribution**   
`normalDist(z, closest = True)`: return the standard normal distribution value. `closest` controls whether to round down or find the cloest vlaue  
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/3_nd.gif" width="150">    
Where as:  
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/3_z.gif" width="75">    
```python
normalDist(0.236)                   # rounded as 0.24, returns 0.59483
normalDist(0.236, closest = False)  # rounded to 0.23, returns 0.59095
```
# Joint Probability Distributions and Random Samples #

**Marginal Probability Mass Function of X**  
Applies for two discrete random Variables:  
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/5_pxx.gif" width="200">  

**Marginal Probability Mass Function of Y**  
Applies for two discrete random Variables:  
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/5_pyy.gif" width="200">  

**Covariance**  
When two random variables X and Y are not independent, the covariance is defined as:  
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/5_cov.gif" width="250">   
&nbsp; &nbsp; For **discrete** RV, covariance is calculated by:   
&nbsp; &nbsp; <img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/5_covd.gif" width="250">   
&nbsp; &nbsp; For **continuous** RV, covariance is calculated by:   
&nbsp; &nbsp; <img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/5_covc.gif" width="300">   
&nbsp; &nbsp; The simplified verison of covariance formula is:  
&nbsp; &nbsp; <img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/5_covSimp.gif" width="250">   

**Correlation Coefficient**  
For RV `X` and `Y`, the correlation coefficient is defined as the covariance divided by the product of 2 RVs' variance:    
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/5_corr.gif" width="250">  
That character is pronounced as `rho`.     
Note that:
1. `-1 <= ρ <= 1`, two variables are said to be **uncorrelated** when `ρ = 0`.  
2. If `X` and `Y` are _independent_, then `ρ = 0`, but `ρ = 0` _does not imply independence_.  
3. `ρ = 1` or `-1` iff `Y = aX + b` for some numbers `a` and `b` with `a != 0`. aka. `ρ = 1` or `-1` indicates linear relationship.  

A **Statistic** is any quantity whose value can be calculated from sample dat. 

**The Central Limit Theorem (CLT)**  
Let `X1, X2, ..., Xn` be a random sample from a distribution with mean `μ` and variance `σ^2`. Then if `n` is sufficiently large:  
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/5_clt.gif" width="100">    

**Linear Combination**  
Given a collection of n random variables `X1, ..., Xn` and `n` numerical constants `a1, ..., an`, the linear combination of the Xi is defined as:  
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/5_lnrc.gif" width="250">    
&nbsp; &nbsp; The **Expectation** of `Xi`, _no matter they are independent or not_, is defined as:  
&nbsp; &nbsp; <img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/5_lnrexp.gif" width="350">   
&nbsp; &nbsp; The **Variance** of `Xi`, _only if they are independent_, is defined as:  
&nbsp; &nbsp; <img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/5_lnev.gif" width="350">   

# Point Estimation #  

A **point estimate** of a parameter `θ` is a single number that can be regarded as a sensible value for `θ`. It is obtained by selecting a suitable statistic and computing its value from the given sample data. The selected statistic is called the **point estimator of θ**. 

A point estimator <img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/6_tht.gif" width="10"> is said to be an **Unbiased Estimator** of `θ`  if <img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/6_unb1.gif" width="65"> for every possible value of `θ`. If <img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/6_tht.gif" width="10"> is not unbiased, the difference <img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/6_unb2.gif" width="65"> is called the **Bias** of <img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/6_tht.gif" width="10">.

# Statistical Intervals #

**Confidence Interval**   
`CI(precent, sigma, n, xHat)`: Find the confidence interval with given conditions. Note that although the 1st parameter is called `precent`, it requires a number in [0, 1].  
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/CI.gif">  
```python
CI(0.99, 3.3, 100, 52.2)            # returns [51.348600000000005, 53.0514]
```

**Number of Samples Needed**  
`sampleNeedForCI(precent, sigma, w)`: Complute number of samples needed for a certain CI.  
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/sampleNeeded.gif">  
```python
sampleNeedForCI(0.99, 3.3, 1)      # returns 289.95278399999995
```

**Population Proportion Confidence Interval**  
`propCI(n, passed, precent)`: CI for a population proportion `p`  
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/popuPropCI.gif">

**t-distribution Confidence Interval**    
`TCI(precent, stdev, n, mean, tCritical)`: CI for t-distribution. Currently need the user enter t-critical value.  
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/TCI.gif">  

**Prediction Interval**  
`PI(precent, stdev, n, mean, tCritical)`: Currently need the user enter t-critical value.      
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/PI.gif">  

# Simple Linear Regression and Correlation #

**Model equation**  
Simple Linear Regression Model equation:  
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/12_1_1.gif">  
```python
# initlize a linear regression model
lnrModel = linearReg([1, 2, 3, 4, 5], [0.92, 2.03, 2.94, 4.10, 5.01]);
```

**Sxx**  
`self.Sxx()`: Sum of the squares of the difference between each `x` and the _mean_ `x` value.  
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/12_sxx.gif" width="200">  
```python
lnrModel.Sxx()            # returns 10.0 in this case
```

**Syy**  
`self.Syy()`: Sum of the squares of the difference between each `y` and the _mean_ `y` value.   
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/12_syy.gif"> 
```python
lnrModel.Syy()            # returns 10.520 in this case
```

**Sxy**  
`self.Sxy()`: Sum of the product of the difference between `x` its _means_ and the difference between `y` and its _mean_.  
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/12_sxy.gif">    
```python
lnrModel.Sxy()            # returns 10.25 in this case
```

**The x Coefficient**  
`self.betaH1()`   
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/12_bh1.gif">  
```python
lnrModel.betaH1()            # returns 1.025 in this case
```

**The Constant Coefficient**   
 `self.betaH0()`   
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/12_bh0.gif">    
```python
lnrModel.betaH0()            # returns -0.0750 in this case
```

**SSE**  
**E**rror sum of squares:    
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/12_sse.gif" width="150">    

**SST**  
**T**otal sum of squares:   
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/12_sst.gif" width="200">    

**SSR**  
**R**egression sum of squares:  
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/12_ssr.gif" width="250">    

**r**
Coefficient of determination. `0 <= r^2 <= 1`, it describes the linear relationship between y and x.   
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/12_r2.gif" width="200">  

**Variance of beta1**  
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/12_var.gif" width="150"> 

**Estimated Standard Deviation**  
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/12_sbh1.gif" width="100"> 

**T**  
The assumptions of the simple linear regression model imply that the standardized variable `T` has a t distribution with `n - 2` df.   
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/12_t.gif" width="200"> 

**CI for Slope**  
A `100(1 - α)%` CI for the slope `β1` of the true regression line is:   
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/12_cib1.gif" width="150"> 

# Model Adequacy and Goodness-of-Fit #

**Standardized Residuals**  
Calculated by subtracting the mean value (zero) and then dividing by the estimated standard deviation.  
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/14_res.gif" width="200">  

**Null Hypothesis:**  
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/14_h0.gif" width="200">  

**Alternative Hypothesis:**  
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/14_ha.gif" width="300">  

**Test Statistic Value** `chi`:  
<img src="https://github.com/Amarthgul/studentCalculator/blob/master/Resources/14_tsv.gif" width="400">   



