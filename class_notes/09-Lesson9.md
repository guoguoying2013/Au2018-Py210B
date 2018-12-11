# Lesson 9 (week 9) for PYTHON210B, Autumn 2018 (December 5, 2018)

## Logistics

* Attendance check (TA)
* Lightning talks after the first break
* Office hours
  * Instructor: Tuesday 7:30-9pm online only through [Zoom](https://washington.zoom.us/my/python2018)
  * TA: Optional or TBA
* Due dates for week 9
  * Lesson 9 Assignment by 11:59pm, Tuesday, Dec. 11, 2018 (15 points, Canvas submission of your source files and a GitHub PR for the assignment required)
    * Object-oriented mailroom: https://canvas.uw.edu/courses/1231462/modules/items/8759026
* **Important** Past assignments (sessions 7 & 8) should be all submitted by next Monday (12/10).
  * Final letter grading due is coming soon, so we need to expedite assignment submissions so that grading can start!

## [Multiple Inheritance & Mix-ins](https://uwpce-pythoncert.github.io/PythonCertDevel/modules/MultipleInheritance.html#multiple-inheritance)

* See [`examples/multiple_inheritance/object_canvas.py`](../examples/multiple_inheritance/object_canvas.py) (You should have this file in your cloned repo once you run `git pull upstream master`) and follow the demonstration (in iPython)
  * `run object_canvas.py`
  * `c = Circle(center=(1,2), diameter=4, fill_color='Red', line_color='Yellow', line_width=1)`
  * `c.__dict__`
* Inheriting from more than one classes can be useful, and this is multiple inheritance

## [Method Resolution Order and `super()`](https://uwpce-pythoncert.github.io/PythonCertDevel/modules/MultipleInheritance.html#python-s-multiple-inheritance-model)

* Multiple inheritance can be useful, but can be confusing, especially when the [diamond problem](https://uwpce-pythoncert.github.io/PythonCertDevel/modules/MultipleInheritance.html#the-diamond-problem) occurs
  * See [`examples/multiple_inheritance/diamond.py`](../examples/multiple_inheritance/diamond.py) and note that `A.do_your_stuff()` is called twice when `D.do_your_stuff()` is called.
* MRO (Method Resolution Order) through `super()`
  * A mechanism to uniquely define the traversal order of any attribute in an inheritance hierarchy
  * Complex linearization algorithm, given an inheritance hierarchy: [C3 linearization](https://en.wikipedia.org/wiki/C3_linearization)
    * No need to know this. Just consider this a consistent topological ordering result
      * What is a topological order? Linearization of nodes in a directed-acyclic graph (any valid inheritance hierarchy) that doesn't violate the directions
  * `Class.mro()` shows such an ordering
    * See [`examples/multiple_inheritance/mro.py`](../examples/multiple_inheritance/mro.py) and [`examples/multiple_inheritance/invalid_mro.py`](../examples/multiple_inheritance/invalid_mro.py) for example
  * All the participating methods (same name, same signature) must call `super()` to get the MRO's benefit
    * Otherwise, the chain is broken and desired outcome is not achieved. See [this](https://uwpce-pythoncert.github.io/PythonCertDevel/modules/MultipleInheritance.html#what-does-super-do) for what `super()` does
      * See [`examples/multiple_inheritance/super_test.py`](../examples/multiple_inheritance/super_test.py) for such example
  * See [`examples/multiple_inheritance/diamond_super.py`](../examples/multiple_inheritance/diamond_super.py) for how the diamond problem is solved using `super()`

## [Assignment: OO Mailroom]

* Has nothing to do with multiple inheritance
* Object-oriented modeling and design, applied to the mailroom application
* You are given example classes: `Donor`, `DonorCollection` (or `DonorDB`), ...
* For `Donor` class, what attributes and methods would you put?
  * Always consider "encapsulation" and "information hiding". Use `@property` as appropriate
* What about `DonorCollection`?
* Test-driven development becomes easier with encapsulation
  * For each method you define in a class, make sure to add a test case before implementing the method!
* There's no single right/correct design!
  * But there are definitely many good/bad designs. Try to think about what is consdered a good design or a bad design.
