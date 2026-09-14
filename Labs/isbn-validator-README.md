# ISBN Validator (Debugging Lab)

A Python program that validates ISBN-10 and ISBN-13 codes by calculating and comparing check digits. Unlike most of my other labs, this one wasn't written from scratch — it was a **debugging exercise**: I was given broken starter code with several intentional bugs and had to find and fix each one to get all tests passing.

## What it does

Prompts the user for an ISBN code and its length (10 or 13), then validates it by:
- Checking the input is properly comma-separated
- Validating the length is numeric and either 10 or 13
- Splitting the code into its main digits and check digit
- Recalculating the expected check digit and comparing it to the one provided
- Handling invalid characters (e.g. hyphens) gracefully instead of crashing

## Bugs I found and fixed

- **TypeError** — `len()` was being called with two arguments instead of one
- **Off-by-one indexing error** — string slicing was grabbing the wrong characters, cutting off the check digit incorrectly (fixed by carefully counting string indices by hand)
- **Unhandled ValueError** — non-numeric characters in the ISBN (like a hyphen) crashed the program instead of printing a clean error message; wrapped the conversion in `try`/`except`
- **IndentationError** — inconsistent indentation inside a function

## Example

```
Enter ISBN and length: 1530051126,10
Valid ISBN Code.
```

```
Enter ISBN and length: 15-0051126,10
Invalid character was found.
```

## What I learned

- How to debug someone else's code methodically instead of writing from scratch
- The difference between a `TypeError` (wrong number/type of arguments) and a `ValueError` (right type, invalid value)
- How to manually trace string indices to catch off-by-one errors
- Using `try`/`except` to handle bad input without crashing
