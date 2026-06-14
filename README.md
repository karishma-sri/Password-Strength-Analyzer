# Password Strength Analyzer

## Overview

Password Strength Analyzer is a Python-based GUI application built with Tkinter that evaluates the strength of user passwords. The program analyzes passwords based on length, character variety, common password detection, repeated characters, and sequential patterns, then provides feedback and suggestions for improvement.

## Features

* Checks password length (minimum 8 characters recommended)
* Detects lowercase letters
* Detects uppercase letters
* Detects numbers
* Detects special characters
* Identifies common passwords
* Detects repeated characters
* Detects sequential patterns such as:

  * 12345
  * qwerty
  * abcdef
* Calculates a password score out of 5
* Classifies passwords as:

  * Weak
  * Medium
  * Strong
  * Highly Strong
* Provides warnings and improvement suggestions
* User-friendly graphical interface using Tkinter

## Technologies Used

* Python 3
* Tkinter (GUI Library)

## Installation and Usage

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Password-Strength-Analyzer.git
```

### 2. Navigate to the project directory

```bash
cd Password-Strength-Analyzer
```

### 3. Run the application

```bash
python password_analyzer.py
```

## Example

### Input

```
Password123
```

### Output

```
Password Score: 4/5
Strength: Strong

Suggestions:
• Add special characters
```

## Password Evaluation Criteria

| Criteria                    | Score |
| --------------------------- | ----- |
| Length ≥ 8 characters       | +1    |
| Contains lowercase letters  | +1    |
| Contains uppercase letters  | +1    |
| Contains numbers            | +1    |
| Contains special characters | +1    |

Maximum Score: 5/5

## Future Improvements

* Password visibility toggle (Show/Hide Password)
* Password generator
* Entropy-based strength calculation
* Dark mode interface
* Database of leaked passwords
* Progress bar for strength visualization

## Author

Karishma

## License

This project is open source and available under the MIT License.
