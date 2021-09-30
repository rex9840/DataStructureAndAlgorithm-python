### Definition and Usage: 
 
**The assert keyword lets you test if a condition in your code returns True, if not, the 
program will raise an AssertionError than is written by us.**

 
***Syntax*** :

> **assert {condition}, {message}**

####Examples: 
``Create a sequence of numbers from 0 to 6, and print each item in the sequence:``


```py
# Python assert Keyword
x = 2
assert x < 1, 'x is not less than 1'

```

> The output is: 
AssertionError: x is not less than 1 
Because the condition here (x<1) is not met, so it raises error. 

