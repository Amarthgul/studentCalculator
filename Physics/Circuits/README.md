
**R():**

Calculate Resistance given volt and ampere, return unit in Ohm.

Support `str` and numbers. When using numbers, by default the first number is ampere,and the second is volt.
```python
R('15 mA, 5V')    #return 333.33333333333337
R(15, 5)          #return 0.3333333333333333
R('15a 5v')       #return 0.3333333333333333
```
