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

**sciConvert(num):**

Convert a number into scientific format.

```python
sciConvert(12345)  # returns "123.4500 * 10 ^ 2"
sciConvert(12345, powerBase = 2, power = 10, precision = 6)  # returns "12.055664 * 2 ^ 10"
```

**normalDist(z, closest = True)**

Return the standard normal distribution value. `closest` controls whether to round down or find the cloest vlaue

```python
normalDist(0.236)                   # rounded as 0.24, returns 0.59483
normalDist(0.236, closest = False)  # rounded to 0.23, returns 0.59095
```

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
