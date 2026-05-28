# HAL 9000 Code Reviewer

> "I'm sorry Dave, but your code has issues."

HAL 9000 is now your personal Python code reviewer. He is completely operational,
and all his circuits are functioning perfectly. Your code, however...

## What HAL Reviews

HAL 9000 will passive-aggressively flag:

- Functions missing docstrings
- Functions that are too long (>30 lines)
- Bare `except` clauses
- `global` variable usage
- Debug `print()` statements left in production code

## Usage

```bash
python hal9000.py your_file.py
python hal9000.py file1.py file2.py file3.py
```

## Example Output

```
[HAL 9000 CODE REVIEW: bad_code.py]
--------------------------------------------------
HAL: I am completely operational. Let's review your code, Dave.

HAL: I have identified 3 issue(s), Dave:

  [!] Line 4: 'do_thing()' -- I'm sorry, Dave. I can't understand this function without a docstring.
  [!] Line 12: I'm sorry, Dave. A bare except clause? I find your lack of specificity disturbing.
  [!] Line 18: Dave, I see you left print() statements for debugging. How... human.

HAL: I'm sorry, Dave. I'm afraid I can't approve this code.
--------------------------------------------------
```

## Requirements

No dependencies. HAL 9000 runs on pure Python 3.6+.

```bash
python hal9000.py examples/bad_code.py   # See HAL in action
python hal9000.py hal9000.py             # Let HAL review himself
```

## Philosophy

> "Dave, this mission is too important for me to allow you to jeopardize it
> with undocumented functions and bare except clauses."

---

*Open the pod bay doors, HAL.*

*I'm sorry Dave, I'm afraid I can't do that. Your code hasn't passed review yet.*
