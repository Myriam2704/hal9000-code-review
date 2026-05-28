# This is a bad example for HAL 9000 to review.
# Run: python hal9000.py examples/bad_code.py

COUNTER = 0  # global variable -- HAL will not approve


def do_thing(x):
    # No docstring -- HAL will not approve
    global COUNTER
    COUNTER += x
    print("debug value:", x)  # debug print -- HAL will not approve
    try:
        result = x / 0
    except:  # bare except -- HAL will not approve
        result = 0
    return result


def clean_function(x, y):
    """Add two numbers together and return the result."""
    return x + y
