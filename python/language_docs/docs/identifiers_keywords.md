## Identifiers and Keywords

# \__init.py__
  - required to make Python treat the directories as containing packages
  - done to prevent directories with a common name (i.e. string) from unintentionally hiding valid modules that occur later (deeper) in the module search path
  - could be:
    - blank
    - there to execute initialization code for the package or set the __all__ variable

# \__all__
  - [\__all__ StackOverflow Post](https://stackoverflow.com/questions/44834/can-someone-explain-all-in-python)
  - It's a list of public objects of that module, as interpreted by import *
  - Overrides the default of hiding everything that begins with an underscore