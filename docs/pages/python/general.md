# General Overview of Language Specific Nuances

## Passing Parameters
  - Python does not support pointers, but objects are passed by reference (i.e. lists)
  - Python is "Call by Object"
    - Mutable and Immutable objects are passed by reference
    - Immutable objects, naturally, cannot be changed
    - Mutable objects, can be changed
    - If you create a local copy of the variable passed by reference, then that local scope is isolated from the rest of the world (even though it was passed by reference)
    - Do not confuse the above line with the idea that setting assigning a variable to a reference will allow that new variable to change the reference, and subsequently, anything else pointing to it
    -  You could always pass a copy of a list to functions using ```func(array[:])```
  - ```func(*args)```
    - This allows n-number of params to be passed
    - They are passed as a tuple
    - If not provided, an empty tuple is passed
    - Positional args must be be passed first (i.e. ```func(city, *other_cities)```)
    - Do NOT confuse this with the double ```**```
  - ```func(**kwargs)```
    - This allows for n-number named arguments
    - i.e. ```func(x=1, y=2, z=3)```
    - You can combine this functionality together with the single ```*```
  - Resources:
    - [Passing Arguments](https://www.python-course.eu/passing_arguments.php)
    - [Pointers in Python](http://qa.geeksforgeeks.org/1540/qa.geeksforgeeks.org/1540/does-python-support-pointers-like-c.html)