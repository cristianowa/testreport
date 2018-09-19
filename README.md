# Test Report

Test Report is an extension for unittest which generates reports based on test cases execution




## Motivation

Have you ever had a piece of code consumed by others ? You wish to explain they how to use it, but is hard to keep the code, tests and documentation up-to-date ? Using TDD you can match the tests and the code, but how you keep the documentation up-to-date ? You can use some documentation generation such [TODO] or [TODO], but you still need to handle this.

The idea in this package is to integrate do generated documentation **into** the tests, so when a behavior change, you can update both the test and documentation together.
Moreover, you only exposes the features you have tests written for, hence improving the stability.   

## Getting started

The follow snippet shows how to replace the TestCase with TestReport:
```python
from testreport import TestReport

class TestSuite(TestReport):
    CSV_DIR = "/tmp/"
    

```

## How to use it

TODO

## Supported formats

* HTML
* Latex
* Pdf (requires latex2pdf)
* MarkDown

