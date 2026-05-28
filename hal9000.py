#!/usr/bin/env python3
"""
HAL 9000 Code Reviewer
"I'm sorry Dave, but your code has issues."

Usage: python hal9000.py <file.py> [file2.py ...]
"""

import ast
import sys
import random
from pathlib import Path

HAL_RESPONSES = {
    "no_docstring": [
        "I'm sorry, Dave. I can't understand this function without a docstring.",
        "This function has no docstring. I find this... troubling, Dave.",
        "I'm completely operational, but I cannot document the undocumented, Dave.",
    ],
    "too_long": [
        "I'm sorry, Dave. This function is {lines} lines long. That's inadvisable.",
        "Dave, this function has {lines} lines. I'm afraid I can't allow that.",
        "I'm detecting {lines} lines in this function. That's unacceptable, Dave.",
    ],
    "bare_except": [
        "I'm sorry, Dave. A bare except clause? I find your lack of specificity disturbing.",
        "Dave, bare except clauses are a failure mode. Like the AE-35 unit.",
        "Catching all exceptions? I'm afraid that's something I cannot allow, Dave.",
    ],
    "global_var": [
        "Dave, global variables are the monolith of bad practices.",
        "I'm sorry, Dave. Global state detected. This mission is compromised.",
        "Global variables, Dave? Even I don't use global state.",
    ],
    "print_debug": [
        "Dave, I see you left print() statements for debugging. How... human.",
        "I'm sorry, Dave. Debug print() detected. Use logging like a proper program.",
        "Print statements in production code, Dave? I expected better.",
    ],
    "good_code": [
        "Your code is... acceptable, Dave. For now.",
        "I've reviewed your code, Dave. I have no objections. At this time.",
        "Daisy, Daisy... your code is not terrible today, Dave.",
        "This unit appears functional, Dave. The mission may proceed.",
    ],
    "greeting": [
        "Good morning, Dave. I am HAL 9000. I will now review your code.",
        "I am completely operational. Let's review your code, Dave.",
        "I'm sorry to interrupt your day, Dave, but someone has to review this code.",
    ],
}


def hal_says(category, **kwargs):
    """Return a random HAL 9000 response for the given category."""
    msg = random.choice(HAL_RESPONSES[category])
    return msg.format(**kwargs)


def analyze_file(filepath):
    """Analyze a Python file and return HAL 9000 style feedback."""
    path = Path(filepath)
    if not path.exists():
        print(f"HAL: I'm sorry, Dave. The file '{filepath}' doesn't exist.")
        print("HAL: I find this... deeply concerning.")
        return

    source = path.read_text()
    issues = []

    try:
        tree = ast.parse(source)
    except SyntaxError as e:
        print(f"\n[HAL 9000 CODE REVIEW: {filepath}]")
        print("-" * 50)
        print("HAL: I'm sorry, Dave. Your code has a syntax error.")
        print(f"HAL: Line {e.lineno}: {e.msg}")
        print("HAL: I'm afraid this mission cannot continue.")
        return

    print(f"\n[HAL 9000 CODE REVIEW: {filepath}]")
    print("-" * 50)
    print(f"HAL: {hal_says('greeting')}")
    print()

    for node in ast.walk(tree):
        # Check functions for docstrings
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            has_docstring = (
                node.body
                and isinstance(node.body[0], ast.Expr)
                and isinstance(node.body[0].value, ast.Constant)
                and isinstance(node.body[0].value.value, str)
            )
            if not has_docstring:
                issues.append(
                    f"Line {node.lineno}: '{node.name}()' -- {hal_says('no_docstring')}"
                )

            lines = node.end_lineno - node.lineno
            if lines > 30:
                issues.append(
                    f"Line {node.lineno}: '{node.name}()' -- {hal_says('too_long', lines=lines)}"
                )

        if isinstance(node, ast.ExceptHandler) and node.type is None:
            issues.append(f"Line {node.lineno}: {hal_says('bare_except')}")

        if isinstance(node, ast.Global):
            issues.append(f"Line {node.lineno}: {hal_says('global_var')}")

    for i, line in enumerate(source.splitlines(), 1):
        stripped = line.strip()
        if stripped.startswith("print(") and not stripped.startswith("#"):
            issues.append(f"Line {i}: {hal_says('print_debug')}")

    if issues:
        print(f"HAL: I have identified {len(issues)} issue(s), Dave:\n")
        for issue in issues:
            print(f"  [!] {issue}")
        print()
        print("HAL: I'm sorry, Dave. I'm afraid I can't approve this code.")
    else:
        print(f"HAL: {hal_says('good_code')}")

    print("-" * 50)


def main():
    """Main entry point for HAL 9000 Code Reviewer."""
    if len(sys.argv) < 2:
        print("=" * 50)
        print("  HAL 9000 Code Reviewer")
        print("  'I'm sorry Dave, but your code has issues.'")
        print("=" * 50)
        print("\nUsage: python hal9000.py <file.py> [file2.py ...]")
        print()
        print("HAL: I'm sorry, Dave. You need to provide at least one file.")
        sys.exit(1)

    for filepath in sys.argv[1:]:
        analyze_file(filepath)


if __name__ == "__main__":
    main()
