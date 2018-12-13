# Lesson 10 (week 10, last week) for PYTHON210B, Autumn 2018 (December 12, 2018)

## Logistics

* Attendance check (TA)
* We are all done with lightning talks!
* Office hours
  * No more scheduled office hours (yesterday was the last one)
  * Email me for any appointment requests
* No assignments, no due dates for week 10
* **Important:** End-of-quarter deadlines
  * 12/14 (Friday) for submissions of all assignments for TA grading
  * If you miss this deadline and/or your total percentage score is still below 80% as of 12/17 (Monday), you may be given an I (incomplete) grade.
    * Your firm late submission deadline (to be considered for an S (satisfactory) grade change) is 12/26 (Wed.).
      * Only Canvas submissions will be graded. Github PRs may be still used for asking reviews and providing feedback, but you must explicitly request my review by email (because most of you don't address my comments anyway, and I can't keep track of unrelated commits all the time). I'll not review github PRs without any explicit requests for review.
      * Resubmissions of earlier assignments are allowed, to boost your total percentage score.
      * All submissions after 12/14 will be graded by instructor.
    * After 12/26, no more late submissions can be accepted.
    * Your I grade will be changed to either S or U after 12/26, based on your achieved final total percentage score (80% or above for S, U otherwise).
    * You need an S grade in this course, in order to continue to PY220 in the next (or a later) quarter.
      * PY220 in the next quarter starts on 1/9/2019.
      * You can enroll in PY220 only after you receive an S in this course (PY210).

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
