# MyLibrary

A simple math and string manipulation library.

## Installation

```sh
pip install mylibrary
```
## Usage

```python
from mylibrary import add, to_uppercase

print(add(5, 3))            # Output: 8
print(to_uppercase("hello"))  # Output: HELLO
```


### **Build the Wheel File**

To build the wheel file, you’ll need `setuptools` and `wheel` installed. You can install them using pip:

```sh
pip install setuptools wheel
python setup.py bdist_wheel
```

### Install the Wheel File Locally
```sh
pip install dist/mylibrary-0.1-py3-none-any.whl
```