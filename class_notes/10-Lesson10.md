# Lesson 10 (week 10, last week) for PYTHON210B, Autumn 2018 (December 12, 2018)

## Logistics

* Attendance check (TA)
* We are all done with lightning talks!
* Office hours
  * No more scheduled office hours (yesterday was the last one)
  * Email me for any appointment requests
* No assignments, no due dates for week 10
* **Important:** All assignments should be submitted by this Saturday (12/15/2018)
  * This is a firm deadline due to UW PCE's grade submission deadline
  * Please let me know in advance if you can't meet this deadline
  * If your final percentage total doesn't meet the passing threshold (80%) by that time...
    * I'll have to assign you an I (Incomplete) grade, which may keep you from registering for the next course... Let's not let this happen!

## Intro to Functional Programming

* [Our course material on this topic](https://uwpce-pythoncert.github.io/PythonCertDevel/modules/OO_vs_functional.html) gives a good overview of the programming paradigm.
  * Probably the most important key point is that functions are treated just like other values ("first class functions").
    * They can be assigned to variables, passed to other functions as arguments, ...
* Map, filter, and reduce: First such examples treating functions like values
  * [Our course material on this topic](https://uwpce-pythoncert.github.io/PythonCertDevel/modules/MapFilterReduce.html) gives good examples.
  * Another seemingly good Python functional programming intro in [this page](https://maryrosecook.com/blog/post/a-practical-introduction-to-functional-programming)
  * See how `lambda` is used (to define a small function inline, on the fly, without having to define it separately, without giving an explicit name--that is, anonymously).
    * [Another good intro](http://www.cs.rpi.edu/~sibel/csci1100/fall2017/lecture_notes/lec24_functional.html)
  * Note that map/filter can be done with list comprehensions. Try those examples.
  * Reduce can be a bit complicated, depending on whether the operation (function) is commutative or not. Try `reduce(lambda x, y: x - y, [1, 2, 3, 4, 5])` and `reduce(lambda x, y: y - x, [1, 2, 3, 4, 5])`.

* More first class functions examples
  * Decorations are in fact an important usage of this concept. See examples in [this link](https://anandology.com/python-practice-book/functional-programming.html#higher-order-functions-decorators).
    * See example code at [`examples/decoration.py`](../examples/decoration.py)
    * Try `print(fib_a(50))` and think about why it takes so long.
    * See how `trace()` can be used to augment (decorate) behavior of the passed function.
    * Notice that Python's `@` decoration is just a syntactic sugar for this.
    * `memoize()` is a very important technique to avoid unnecessary repeated computation with recursion, and can reduce the running time of the original `fib_a()` greatly. This can be all achieved by a simple decoration, and in fact there are many decorators available in Python library (that you'll learn and use in the next course).
