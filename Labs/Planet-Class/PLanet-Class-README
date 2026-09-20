# Planet Class

A Python class representing a planet, with input validation, a custom method, and a custom string representation — my first object-oriented programming lab.

## What it does

The `Planet` class:
- Validates that `name`, `planet_type`, and `star` are all non-empty strings when an instance is created, raising `TypeError` or `ValueError` with specific messages otherwise
- Has an `orbit()` method that returns a description of the planet orbiting its star
- Has a custom `__str__` method so printing a `Planet` object shows a clean, formatted summary

## Example

```python
planet_1 = Planet('Jupiter', 'Gas Giant', 'Sun')

print(planet_1)
# Planet: Jupiter | Type: Gas Giant | Star: Sun

print(planet_1.orbit())
# Jupiter is orbiting around Sun...
```

Invalid input raises clear errors:
```python
Planet(123, 'Gas Giant', 'Sun')       # TypeError: name, planet type, and star must be strings
Planet('', 'Gas Giant', 'Sun')        # ValueError: name, planet_type, and star must be non-empty strings
```

## What I learned

- Core object-oriented programming concepts: classes, `__init__`, instance attributes
- Dunder methods — specifically `__str__`, and why `print(obj)` automatically calls it instead of needing `obj.__str__()`
- The difference between `try`/`except` (catching an error Python raises on its own) and `raise` (deliberately throwing a custom error based on a condition you check yourself)
- Combining multiple validation checks into a single `if` statement with `or`, instead of repeating near-identical blocks
- "Validate first, assign second" — checking all inputs are valid *before* committing them to instance attributes
