# Lesson 7 (week 7) for PYTHON210B, Autumn 2018 (November 14, 2018)

## Logistics

* Attendance check (TA)
* Lightning talks after the first break
* Office hours
  * Instructor: Tuesday 7:30-9pm online only through [Zoom](https://washington.zoom.us/my/python2018)
  * TA: Optional or TBA
* Due dates for week 7
  * Lesson 7 Assignment by 11:59pm, Tuesday, Nov. 27, 2018 (15 points, Canvas submission of your source files and a GitHub PR for the assignment required)
    * HTML Renderer: https://canvas.uw.edu/courses/1231462/modules/items/8759017
    * This project is pretty big and nontrivial. Also it's due in 2 weeks, not because of its difficulty, but because there's no class next week (Thanksgiving eve).
    * Make sure to follow all the instructions and also check out the [HTML renderer tutorial](https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/html_renderer_tutorial.html)

## Object-Oriented Paradigm Overview

* [Good read in our course material by our course creator](https://uwpce-pythoncert.github.io/PythonCertDevel/modules/ObjectOrientationOverview.html)
* This discussion is always abstract anyway, so we can continue to the Python specifics.

## [Python Classes](https://uwpce-pythoncert.github.io/PythonCertDevel/modules/PythonClasses.html)

* Class attributes vs. instance attributes: Go over [our course material on this](https://uwpce-pythoncert.github.io/PythonCertDevel/modules/PythonClasses.html#class-attributes)
  * A class attribute is shared by all instances of the class.
    * The proper way to access a class attribute is through the class name: ``Class1.cls_attr1``.
    * However, it may be accessed as ``self.cls_attr1`` inside the class definition *as long as* there's no instance attribute with the name ``cls_attr1`` (which is bad, but still doable). This can lead to some serious confusion.
      * But this is also needed and critical, when the attributes are overridden in an inheritance hierarchy (in the next subsection).
    * Also, outside the class definition, it may be accessed as ``inst1.cls_attr1`` *as long as* the ``inst1`` instance doesn't have instance attribute named `cls_attr1` (which is bad, but still possible).
  * ``self.any_attr`` in class definition: Looks up the instance itself for the attribute ``any_attr``, and access it if it exists. If not, looks up the class definition for the class attribute ``any_attr``, and access it if it exists. If not, it goes up the ladder (inheritance hierarchy).
    * This is Python's built-in name resolution scheme with classes. It can get quite confusing (especially together with multiple inheritance)...
* ``self``: This is NOT a keyword! It can be any name, but we better/should stick with ``self``!
  * To access any instance attribute ``inst_attr1``, you must prefix it with ``self.``!
    * Just entering ``inst_attr1`` is to access a *local* variable named ``inst_attr1``, which is not what we want.
      * This is different from Java or any such OO languages.
  * ``self`` in methods
    * For an example class and an instance of it:
      ``` Python
      class C:
          def method1(self, p1, p2):
              pass
      inst = C()
      ```
    * The following function calls are equivalent:
      ``` Python
      # Instance method syntax
      inst.method1(a1, a2)
      # Class method syntax, with the instance added as the first argument
      C.method1(inst, a1, a2)
      ```
    * In fact, Python runtime converts any method call on an object (that is, ``inst.method1(a1, a2)``) to the class method call syntax (that is, ``C.method1(inst, a1, a2)``), and the ``self`` parameter in ``def method1(self, p1, p2)`` is matched with the first argument (``inst``) in this class method call syntax.

## [Inheritance](https://uwpce-pythoncert.github.io/PythonCertDevel/modules/SubclassingAndInheritance.html)

* Extending an existing class (e.g., adding new attributes/methods)
    ``` Python
    class A:
        def methodA(self):
            ...
    class B(A):
        def methodB(self):
            ...
    b = B()
    b.methodA()  # b (a B instance) now has both A's methods and B's methods)
    b.methodB()
    ```

* Overriding some parts of an existing class (replace the superclass definition)
    ``` Python
    class A:
        def method1(self):
            print('method1 in class A')
    class B(A):
        def method1(self):
            print('method1 in class B')
    b = B()
    b.methodA()  # Will print 'method1 in class B'. A.method1() is overriden (hidden) by B.method1()
    ```
  * Must be the same signature (same method name, same parameter list)
  * Can call the overriden superclass method from the overriding subclass method:
    ``` Python
    class A:
        def method1(self):
            print('method1 in class A')
    class B(A):
        def method1(self):
            A.print(self)
            print('method1 in class B')
    b = B()
    b.methodA()  # Will print 'method1 in class A\nmethod1 in class B'. A.method1() is called from B.method1()
    ```
  * There's a complicated method resolution scheme that'll be covered in Lesson 9.

* Inheritance may be overrated or abused
  * ["Is a" vs "Has a"](https://uwpce-pythoncert.github.io/PythonCertDevel/modules/SubclassingAndInheritance.html#is-a-vs-has-a)
  * Use inheritance only for "Is a" relationships
  * In the HTML renderer assignment, there are lots of "Is a" relationships, so inheritance is natural (forming a hierarchy).