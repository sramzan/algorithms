# List Fun!

## Append vs Extend
  - [Good StackOverflow Explanation](https://stackoverflow.com/questions/252703/difference-between-append-vs-extend-list-methods-in-python)
  - Append adds to the array, while extend will try to take items from the iterable it's passed and insert them into the original
  - `a = [1,2,3]`
  - `a.append([4,5]) # [1,2,3,[4,5]]`
  - `a.extend([4,5]) # [1,2,3,4,5]`
  - ** Extend mutates the original array
  - ** Something such as `a + [4, 5]` will give you a new array assigned to a