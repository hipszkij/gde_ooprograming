# Python Dunder Methods (Magic Methods)

Python dunder methods, also known as magic or special methods, are predefined methods you can use to enrich your classes. They are easy to recognize by their double underscores at the beginning and end of their names (e.g., `__init__`, `__str__`, etc.). These methods allow you to emulate the behavior of built-in types or to implement operator overloading.

## Table of Contents
- [Constructor and Initializer](#constructor-and-initializer)
- [Representational Methods](#representational-methods)
- [Collection Management](#collection-management)
- [Arithmetic Computation Methods](#arithmetic-computation-methods)
- [Comparison Methods](#comparison-methods)
- [Other Useful Methods](#other-useful-methods)

## Constructor and Initializer
- `__init__(self, ...)`: Called after the object has been created to initialize it.
- `__new__(cls, ...)`: Called to create the object, before `__init__`.

## Representational Methods
- `__repr__(self)`: Provides the official string representation of the object, useful for debugging.
- `__str__(self)`: Provides a nicely printable string representation of the object.

## Collection Management
- `__len__(self)`: Returns the length of the collection.
- `__getitem__(self, key)`: Allows access to an element using indexing.
- `__setitem__(self, key, value)`: Sets the value of an element using indexing.
- `__delitem__(self, key)`: Deletes an element using indexing.
- `__iter__(self)`: Returns an iterator for the object.
- `__contains__(self, item)`: Checks if the item is in the object.

## Arithmetic Computation Methods
- `__add__(self, other)`: Defines behavior for the addition operator (`+`).
- `__sub__(self, other)`: Defines behavior for the subtraction operator (`-`).
- `__mul__(self, other)`: Defines behavior for the multiplication operator (`*`).
- `__truediv__(self, other)`: Defines behavior for the division operator (`/`).

## Comparison Methods
- `__eq__(self, other)`: Defines behavior for equality (`==`).
- `__ne__(self, other)`: Defines behavior for inequality (`!=`).
- `__lt__(self, other)`: Defines behavior for less than (`<`).
- `__le__(self, other)`: Defines behavior for less than or equal to (`<=`).
- `__gt__(self, other)`: Defines behavior for greater than (`>`).
- `__ge__(self, other)`: Defines behavior for greater than or equal to (`>=`).

## Other Useful Methods
- `__call__(self, *args, **kwargs)`: Allows the instance to be called as a function.
- `__hash__(self)`: Provides a hash value of the object.
- `__bool__(self)`: Returns a boolean value evaluating the truthiness of the object.

These methods provide a way to use Python classes as if they were built-in types, giving them functionalities that allow them to integrate seamlessly with Python's built-in functions and operators.
