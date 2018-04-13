# Divisibility.py
A Python 1 Exception Handling UnitTest Challenge

**Goal:**
----------
You will write a math function that is designed to not only solve a math problem but also handles incorrect inputs (ZeroDivisionErrors, TypeErrors/ValueErrors)

**Inputs:**
----------
* `divisibilty()` receives 2 inputs: (numerator & denominator) and returns one of the following outputs:
 * "divides evenly" - if the numbers divide evenly (like `4 / 2`))
 * "doesn't divide evenly" - if the numerator is not evenly divisible by the denominator (like `5 / 2`)
 * "error" - if the inputs cannot be converted to integers (or floats) OR the denominator is `0` (since you cannot divide by 0)
 * **NOTE**: divisibility() should be able to accept strings provided they can be converted to a number (e.g. `divisibility('10', '3')`)

**Notes/Challenge Opportunity**
-------------
* This function needs to check to make sure the inputs can be converted to a number
* This function needs to handle incorrect input (e.g. strings that can't be converted to numbers, a denominator that is 0)
* This function will need to incorporate Exception Handling in addition to performing the expected function

**Examples:**
inputs => output/s
--------------------------------
* 10 2 => "divides evenly"
* 7 2 => "doesn't divide evenly"
* 20 0 => "error"
* "five" / "two" => "error"
