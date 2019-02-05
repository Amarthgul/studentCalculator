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

**sciConvert():**

Convert a number into scientific format.

```python
sciConvert(12345)  # returns "123.4500 * 10 ^ 2"
sciConvert(12345, powerBase = 2, power = 10, precision = 6)  # returns "12.055664 * 2 ^ 10"
```
