# Lesson 8 (week 8) for PYTHON210B, Autumn 2018 (November 28, 2018)

## Logistics

* Attendance check (TA)
* Lightning talks after the first break
* Office hours
  * Instructor: Tuesday 7:30-9pm online only through [Zoom](https://washington.zoom.us/my/python2018)
  * TA: Optional or TBA
* Due dates for week 8
  * Lesson 8 Activities by 11:59pm, Friday, Nov. 30, 2018 (No points, no submissions)
    * Sparse Array (container protocol exercise): https://canvas.uw.edu/courses/1231462/modules/items/8759021
  * Lesson 8 Assignment by 11:59pm, Tuesday, Dec. 4, 2018 (5 points, Canvas submission of your source files and a GitHub PR for the assignment required)
    * Circle class (properties, class method, various magic methods): https://canvas.uw.edu/courses/1231462/modules/items/8759022

## [Static and Class Methods](https://uwpce-pythoncert.github.io/PythonCertDevel/modules/StaticAndClassMethods.html)

* [Python Is Not Java](http://dirtsimple.org/2004/12/python-is-not-java.html)! Static methods and class methods are different.
* [Static methods](https://uwpce-pythoncert.github.io/PythonCertDevel/modules/StaticAndClassMethods.html#static-methods): Better use module-level global functions. Doesn't get ``self`` or ``cls``.
  * ``@staticmethod`` decoration tells Python runtime that this method doesn't get ``self`` or ``cls`` (thus the number of arguments equals the number of parameters).
* [Class methods](https://uwpce-pythoncert.github.io/PythonCertDevel/modules/StaticAndClassMethods.html#class-methods): ``cls`` is auto-filled by runtime, and it's a class object, not an instance.
  * A class method is applied to the class, not to an instance
  * Class methods are friendly to subclassing
  * Common use case: [Alternate constructors](https://uwpce-pythoncert.github.io/PythonCertDevel/modules/StaticAndClassMethods.html#alternate-constructors)
    * You'll create one in the Circle class assignment

## [Special Methods & Protocols](https://uwpce-pythoncert.github.io/PythonCertDevel/modules/SpecialMethodsAndProtocols.html)

* "Dunder" (double underscore) methods, like ``__init__``
* Many dunder methods with predefined meanings:
  * ``object.__str__``: Like Java's ``Object.toString()`` method
    * But Python also has ``object.__repr__``, which should satisfy ``eval(repr(something)) == something``
  * Numerics protocol: Like operator overloading in C++ or C#
    * Use [``fraction.py``](../examples/fraction.py) and [``test_fraction.py``](../examples/test_fraction.py) for example
  * Container protocol: Still related to operator overloading, but mostly for indexing operator (``[]``)
    * The sparse array exercise is for this
    * See [``index_slicing.py``](../examples/index_slicing.py) for example

## [Properties](https://uwpce-pythoncert.github.io/PythonCertDevel/modules/Properties.html)

* No getters or setters in Python!
  * Use ``@property`` and ``@p.setter`` decorations instead
  * See [``properties_example.py``](../examples/properties_example.py)
  * You should use this for the Circle class assignment
    * Both for ``radius`` and ``diameter``, but you should remember only one (``radius``) and derive the other from their relationship
