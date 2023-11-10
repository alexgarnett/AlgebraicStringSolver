# AlgebraicStringSolver
This module solves an algebraic expression entered as a string, and returns the answer as a string with two decimal precision.

# Installation
```
git clone https://github.com/alexgarnett/AlgebraicStringSolver
```

# Usage
```
from AlgebraicProblemSolver.src.solver import *
answer = solve('12 - 4 * 2')
```
The input must be entered as a string. Numbers can be integers or floats. Correct format is number followed by operator, followed by number, and so on. There must be a single space on each side of an operator. There must be a digit at the first and last index of the string.

# Output
```
'4.00'
```

# Testing
From command line:
```
python3 -m unittest
```