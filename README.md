Semantic Version Comparator
----------
 A CLI Python library for comparing semantic version strings.
 
How do I use?
----------
Lets say you have two releases:
+ 1.0.0
+ 1.1.0

Easy enough; but how do I compare them?

```
$ python main.py 1.0.0 1.1.0
```
```
>>> '1.0.0' is less than '1.1.0'
```

How do I install?
----------
Simple!
1. Clone the repo, or copy the main.py script.

This was written in Python 3.5.2 and is currently untested in other Python versions. 

Are there dependencies?
----------
No! This uses the Python standard library.


Whats WIP?
----------
TODO: Add rc, alpha, beta, etc support for string comparison
TODO: Add ~= test operator for pessimistic comparisons