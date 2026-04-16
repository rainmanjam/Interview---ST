# Package Sorting

A function that dispatches packages to the correct robotic arm stack based on volume and mass.

GitHub repository: [https://github.com/rainmanjam/Interview---ST](https://github.com/rainmanjam/Interview---ST)

## Prerequisites

- Python 3.10 or newer
- Git (only needed if you are cloning the repository)

Check your Python version:

```bash
python3 --version
```

If your system maps Python 3 to `python`, you can use `python` instead of `python3` in all commands below.

## Installation

1. Clone the repository and move into the project directory:

```bash
git clone https://github.com/rainmanjam/Interview---ST
cd Interview---ST
```

1. Create a virtual environment:

```bash
python3 -m venv .venv
```

1. Activate the virtual environment:

macOS/Linux:

```bash
source .venv/bin/activate
```

Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

1. Upgrade pip (optional but recommended):

```bash
python3 -m pip install --upgrade pip
```

This project uses only the Python standard library, so no additional package installation is required.

## Rules

| Condition | Stack |
| --- | --- |
| Not bulky and not heavy | `STANDARD` |
| Bulky **or** heavy (not both) | `SPECIAL` |
| Bulky **and** heavy | `REJECTED` |

- **Bulky**: volume ≥ 1,000,000 cm³ _or_ any single dimension ≥ 150 cm
- **Heavy**: mass ≥ 20 kg

## Usage

The project exposes a function named `sort(width, height, length, mass)` in `sort.py`.

Quick one-line run:

```bash
python3 -c "from sort import sort; print(sort(10, 10, 10, 5))"
```

Run in an interactive Python session:

```bash
python3
```

Then run:

```python
from sort import sort

sort(10, 10, 10, 5)       # 'STANDARD'
sort(100, 100, 100, 10)   # 'SPECIAL'  (bulky by volume)
sort(10, 10, 10, 25)      # 'SPECIAL'  (heavy)
sort(100, 100, 100, 25)   # 'REJECTED' (bulky and heavy)
```

Expected output for the example calls above:

```text
STANDARD
SPECIAL
SPECIAL
REJECTED
```

If you are using a virtual environment, you can use `python` instead of `python3` once it is activated.

## Run Tests

Requires Python 3.10+.

Run all tests:

```bash
python3 -m unittest -v
```

Run only the main test file explicitly:

```bash
python3 -m unittest -v test_sort.py
```

Run a single test method:

```bash
python3 -m unittest -v test_sort.TestSort.test_special_heavy_at_threshold
```

## Expected Output

When all tests pass, you should see output ending with:

```text
Ran 26 tests in ...

OK
```
