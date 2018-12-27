# Identifiers and Keywords

## \__init.py__
  - required to make Python treat the directories as containing packages
  - done to prevent directories with a common name (i.e. string) from unintentionally hiding valid modules that occur later (deeper) in the module search path
  - could be:
    - blank
    - there to execute initialization code for the package or set the __all__ variable

## \__all__
  - Credit: [\__all__ StackOverflow Post](https://stackoverflow.com/questions/44834/can-someone-explain-all-in-python)
  - It's a list of public objects of that module, as interpreted by import *
  - Overrides the default of hiding everything that begins with an underscore

## slice notation
  - Credit: [Great StackOverflow post discussing the slice notation](https://stackoverflow.com/questions/509211/understanding-pythons-slice-notation)
  - Common slice operations

      | Code              | Description                                       |
      | :---------------- | :------------------------------------------------ |
      | a[start:end]      | items start through end-1                         |
      | a[start:]         | items start through the rest of the array         |
      | a[:end]           | items from the beginning through end-1            |
      | a[start:end:step] | start through not past end, by step<sup>**</sup>  |
      | a[:]              | a copy of the whole array                         |
      | a[-1]             | last item in the array                            |
      | a[-2:]            | last two items in the array                       |
      | a[:-2]            | everything except the last two items in the array |
      | a[::-1]           | all items in the array, reversed                  |
      | a[1::-1]          | the first two items, reversed                     |
      | a[:-3:-1]         | the last two items, reversed                      |
      | a[-3::-1]         | everything except the last two items, reversed    |

  - ** The key point to remember is that the :end value represents the first value that is not in the selected slice. So, the difference beween end and start is the number of elements selected (if step is 1, the default).