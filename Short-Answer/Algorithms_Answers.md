#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
```python
a = 0 # O(1)
while (a < n * n * n): # O(n^3) 1 2 3 
    a = a + n * n # O(n^2) 9 18 27
```
O(1) + O(n^3)/O(n^2) = `O(n)`

Constant is insignificant in run time so removed.

2nd line: loop with n*n*n = O(n^3)

3rd line: variable with n*n = O(n^2)

Since the while loop stops when a += n^2 reaches n^3
the run time becomes O(n) as n^3/n^2 = n

b)
```python
sum = 0 # O(1)
for i in range(n): # O(n)
    j = 1 # O(1)
    while j < n: # O(n)
        j *= 2 # O(1)
        sum += 1 # O(1)
```
Constants are insignificant in run time so removed.

Nested loops of n and log n thus n * log n

Only `O(n log n)` remains

c)  
```python
def bunnyEars(bunnies): 
    if bunnies == 0: # O(1) True/False
    return 0  # O(1)

    return 2 + bunnyEars(bunnies-1) # O(n)
```
Constants are insignificant in run time so removed.

Only `O(n)` remains

## Exercise II

### Find the highest floor
Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

### Answer
By using binary search, we can minimize the dropped and broken eggs while reaching floor f in an efficient manner.

```python
low = first floor
high = nth floor
target = floor f

while low <= high
    mid floor = (low + high) / 2
    if target > mid floor:
        low = mid # change low floor to middle floor
    elif target < mid floor:
        high = mid # change high floor to middle floor
    else:
        # if target not higher or lower than mid floor then mid is target floor
        return mid 
```
Binary search essentially is figuring out how many times to divide N (floors) by 2 until reaching 1 (target floor).

Thus `1 = N / 2^x` into `x*1 = log N` 
