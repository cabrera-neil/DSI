---
title: Python List Comprehensions
duration: "1:30"
creator:
    name: Kiefer Katovich
    city: SF
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Python List Comprehensions


### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Understand list comprehensions in Python and what they are useful for
- Use list comprehensions to efficiently manipulate list data
- Use list comprehensions to construct dictionaries


### STUDENT PRE-WORK
*Before this lesson, you should already be familiar with:*
- Python fundamental concepts and data types
- Python control statements
- Python function definitions
- Python arrays and dictionaries
- Python lambda functions


### LESSON GUIDE

- [Introduction](#introduction)
- [List Comprehension Basics](#comprehension_basics)
- [Advanced List Comprehensions](#comprehension_advanced)
- [Dictionary Comprehensions](#dictionary_comprehensions)
- [Independent Practice](#independent_practice)

---

<a id="introduction"></a>
## Introduction: List Comprehensions

Python list comprehensions are a simple and powerful syntax that, once mastered, allow for fast, efficient, and intuitive manipulation of array-like data types.

Though list comprehensions may seem confusing at first, they are easy to get used to and once understood make otherwise complex code readable and concise.

List comprehensions are essentially replacements for iteration control statements. I will explain why this is the case below, and give the non-list-comprehension alternative code to help you understand what they are doing (and make it clear when they might be better).



<a id="comprehension_basics"></a>
## List Comprehension Basics

##### What are list comprehensions?

List comprehensions are statements that perform some kind of operation on each element of a list. Let's start with a simple array of numbers:

```python
numbers = [0,1,2,3,4,5,6,7,8,9]
```

Imagine that we want to add 1 to every element of the list. We could do this a couple of ways without the use of list comprehensions. We could use a for loop:

```python
nums_plus_one = []
for num in numbers:
  nums_plus_one.append(num+1)
```

We could also use Python's "map" with a lambda function. Map iterates over each element of a list and applies a function to it:

```python
nums_plus_one = map(lambda x: x+1, numbers)
```

These solutions each have pros and cons. The for loop is more readable and explicit (if you aren't familiar with how map and lambda works, at least), and the map with lambda is concise but arcane. Luckily list comprehensions combine the best of both worlds:

```python
nums_plus_one = [x+1 for x in numbers]
```

Let's go over how that works in more granular detail.

- Like the map statement, `nums_plus_one` is assigned on the left as a new variable.
- List comprehensions return a list, and the internal statement is wrapped in the list brackets: `[...]`
- Within the brackets these elements are similar to a for loop:
  1. The **operation per element** comes first: `x+1`
  2. Next is the **for loop variable assignment**: `for x`
  3. Last comes the **list of elements to iterate over**: `in numbers`

##### Conditional logic in list comprehensions

List comprehensions can be extended to cover more of the functionality of a for loop than just an operation over elements. Let's say we wanted to "binarize" a variable based on whether the elements are greater or less than the mean over all elements. The for loop could look something like this:

```python
import numpy as np
n = [1, 2, 7, 21, 3, 1, 62, 3, 34, 12, 73, 44, 12, 11, 9]
n_bin = []
n_mean = np.mean(n)
for x in n:
  if x >= n_mean:
    n_bin.append(1)
  else:
    n_bin.append(0)
```

But that's pretty verbose. A list comprehension can do the same thing much easier:
<details>
<summary> 2-A) Binarize numbers:
```python
import numpy as np
n = [1, 2, 7, 21, 3, 1, 62, 3, 34, 12, 73, 44, 12, 11, 9]
n_mean = np.mean(n)
```
</summary>
```python
n_bin = [1 if x >= n_mean else 0 for x in n]
[0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0]
```
</details>


We can even do chained conditionals! This returns swaps 1s to 0s and vice versa in a list, otherwise sets the items to none:

<details>
<summary> 2-B) Swap 1s & 0s
```python
n = [0, 1, 0, 1, 2, 3, 5, 2, 1, 0]
```
</summary>
```python
bin_or_none = [0 if x == 1 else 1 if x == 0 else None for x in n]
[1, 0, 1, 0, None, None, None, None, 0, 1]
```
</details>

<a id="comprehensions_advanced"></a>
## Advanced List Comprehensions

##### Nested List Comprehensions

As some of you may have suspected by now, we can embed list comprehensions within other list comprehensions for even more power.

For example, let's say we want the square and the square root for every non-negative element in a list:

<details>
<summary> 3-A) Square and square roots
```python
import numpy as np
n = [0, 1, 50, -23, -1, 75, -3]
```
</summary>
```python
math_pairs = [[x**2, np.sqrt(x)] for x in [y for y in n if y >= 0]]
[[0, 0.0], [1, 1.0], [2500, 7.0710678118654755], [5625, 8.6602540378443873]]
```
</details>

Note that the if statement in the embedded list comes _after_ the in statement in this example. When your condition is meant to be a filter the conditional comes after.

##### List Comprehensions with Functions

We can also do operations on multiple lists. I often use the **zip** and **enumerate** functions in combination with list comprehensions. First let's go over what each of the functions does.

**zip** goes through each element of two lists iteratively at the same time:
```python
a = ['a','b','c','d']
z = ['z','y','x','w']

zipped = []
for a_i, z_i in zip(a, z):
  zipped.append([a_i, z_i])

[['a', 'z'], ['b', 'y'], ['c', 'x'], ['d', 'w']]]
```

**Check** Do this as a list comprehension.

**enumerate** keeps track of the index of each element of a list:
```python
a = ['a','b','c','d']

enumerated = []
for i, a_i in enumerate(a):
  enumerated.append([i, a_i])

[[0, 'a'], [1, 'b'], [2, 'c'], [3, 'd']]
```

**Check** Do this as a list comprehension.


Keep note that that with enumerate the index is returned first and the element second.

Let's multiply the element of the first list by the index, then divide that by the element of the second list:

<details>
<summary> 4-C) Comprehensions, enumerate, and zip
```python
list_one = [10, 15, 20, 25, 40]
list_two = [1, 2, 3, 4, 5]
```
</summary>
```python
math_comp = [(x*i)/y for i, (x, y) in enumerate(zip(list_one, list_two))]
[0, 7, 13, 18, 32]
```
</details>

##### Nested Loops

Here's a list comprehension that returns syllables (defined by consonants followed by a vowel) in a flattened list:

<details>
<summary> 5-B) Nested list comprehensions
```python
import string
vowels = ['a', 'e', 'i', 'o', 'u']
alphabet = string.ascii_lowercase
```
</summary>
```python
syllables = [s for syls in [[c+v for v in vowels] for c in [x for x in alphabet if x not in vowels]] for s in syls]
syllables[0:12]
['ba', 'be', 'bi', 'bo', 'bu', 'ca', 'ce', 'ci', 'co', 'cu', 'da', 'de']
```
</details>

**Check:** Does anyone understand how this is working?

This is a complicated list comprehension with nested for loops, and brings up one of the more confusing aspects of list comprehensions. To understand let's first write out the comprehension more explicitly:

```python
# simple list comprehension to get non-vowel letters:
consonants = [x for x in alphabet if x not in vowels]

# get all the syllables for each consonant + vowel pair in nested consonant-syllable lists:
syllables = [[c + v for v in vowels] for c in consonants]

syllables = [
  s
  for syls in syllables
  for s in syls
]
```

The trick here is that the nested list comprehension for loops are in the same order as they would be in standard nested for loops, except the retrieved element comes first!

```python
flat_syllables = []
for syls in syllables:
  for s in syls:
    flat_syllables.append(s)
```


<a id="dictionary_comprehensions"></a>
## Dictionary Comprehensions

Comprehensions are not limited to lists. You can also use comprehensions to create dictionaries with key:value pairs.

Below, for example, we can create a dictionary with the integer value of each character in a string with the string as a key (the **ord** function returns the integer value of a character).

<details>
<summary> 6-A) Dictionary comprehensions
```python
keys = ['dog', 'cat', 'bird', 'horse']
```
</summary>
```python
animal_dict = {k:[ord(c) for c in k] for k in keys}
{'bird': [98, 105, 114, 100],
 'cat': [99, 97, 116],
 'dog': [100, 111, 103],
 'horse': [104, 111, 114, 115, 101]}
```
</details>

This can be particularly useful for creating pandas dataframes.

<details>
<summary> 6-B) Dictionary comprehensions and pandas dataframes
```python
import pandas as pd

column_names = ['height','weight','is_male']
values = [[62, 54, 60, 50], [180, 120, 200, 100], [True, False, True, False]]
```
</summary>
```python
records = pd.DataFrame({col:vals for col, vals in zip(column_names, values)})
```
</details>


<a name="independent_practice"></a>
## Independent Practice
- Practice list comprehensions on your own.
- Problems are separated into easy, medium, and hard categories.

[independent practice problems]('./list-comprehensions-practice.ipynb')
