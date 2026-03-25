# OOPs Quick Revision

Based on:

- `8.1-Class & Objects.ipynb`
- `8.2-Inheritance.ipynb`
- `8.3-Polymorphism.ipynb`
- `8.4-Encapulation.ipynb`
- `8.5-Abstraction.ipynb`
- `8.6-magicmethods.ipynb`
- `8.7-OperatorOverloading.ipynb`

## 1. Classes and Objects

### Core idea

- A class is a blueprint.
- An object is an instance created from that class.

### Key points for revision

- `__init__()` is the constructor used to initialize object state.
- `self` refers to the current object instance.
- Attributes store data, and methods define behavior.
- Instance variables usually differ from object to object.

### Example

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is barking")
```

---

## 2. Inheritance

### Core idea

- Inheritance lets a child class reuse and extend behavior from a parent class.

### Main ideas

- Single inheritance: one parent class
- Multiple inheritance: more than one parent class
- Method overriding: child class provides its own version of a parent method
- `super()` calls parent class behavior

### Example

```python
class Car:
    def drive(self):
        print("Car is driving")

class Tesla(Car):
    def drive(self):
        print("Tesla is driving silently")
```

### Interview note

- Python resolves methods in multiple inheritance using MRO (Method Resolution Order).

---

## 3. Polymorphism

### Core idea

- Polymorphism means the same interface can behave differently for different objects.

### Common forms

- Method overriding in subclasses
- Same method name working differently for different classes

### Example

```python
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Bark")
```

---

## 4. Encapsulation

### Core idea

- Encapsulation bundles data and methods together and controls how object data is accessed.

### Python access styles

- Public: `name`
- Protected by convention: `_name`
- Private with name mangling: `__name`

### Key points for revision

- Python does not enforce access modifiers like some other languages.
- `_name` is a convention that says "internal use".
- `__name` triggers name mangling and is harder to access directly.
- Getters and setters can be used to control updates.

### Interview note

- Python "private" members are not truly inaccessible; they are name-mangled, not completely hidden.

---

## 5. Abstraction

### Core idea

- Abstraction hides implementation details and exposes only the required interface.

### Key points for revision

- Use `ABC` from `abc` for abstract base classes.
- Use `@abstractmethod` to force subclasses to implement required methods.
- Abstract classes define what a subclass must do, not how every detail is done.

### Example

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
```

---

## 6. Magic Methods

### Core idea

- Magic methods are special double-underscore methods that customize object behavior.

### Common ones

- `__init__`: object initialization
- `__str__`: readable string for users
- `__repr__`: official string representation
- `__len__`: behavior for `len(obj)`

### Example

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age}"
```

---

## 7. Operator Overloading

### Core idea

- Operator overloading defines how operators work for custom objects.

### Common methods

- `__add__` for `+`
- `__sub__` for `-`
- `__mul__` for `*`
- `__eq__` for `==`

### Example

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
```

---

## OOP Pillars Summary

| Concept | What it means |
| --- | --- |
| Class and Object | Blueprint and its instance |
| Inheritance | Reuse and extension of parent behavior |
| Polymorphism | Same interface, different behavior |
| Encapsulation | Controlled access to object state |
| Abstraction | Hide complexity behind an interface |

---

## Frequently Asked Interview Questions (Short Answers)

1. **What is the difference between a class and an object?**

- A class is the blueprint; an object is the created instance.

2. **What is method overriding?**

- A subclass provides its own implementation of an inherited method.

3. **What does `super()` do?**

- It gives access to parent class methods and constructors.

4. **What is the difference between `_name` and `__name` in Python?**

- `_name` is a convention; `__name` uses name mangling.

5. **Why use abstract classes?**

- They define a required interface for subclasses.

6. **What is operator overloading?**

- It lets custom objects respond to operators like `+` and `==`.

---

## Last-Minute Revision Checklist

- Revise `class`, `object`, `self`, and `__init__`.
- Practice inheritance and method overriding.
- Remember the four main OOP pillars.
- Know the difference between public, protected, and private naming styles in Python.
- Memorize common magic methods such as `__init__`, `__str__`, and `__add__`.
