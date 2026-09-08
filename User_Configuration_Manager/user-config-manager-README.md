# User Configuration Manager

A small Python module for managing user settings (like theme, language, or notification preferences) stored in a dictionary — built as a freeCodeCamp lab exercise.

## What it does

Implements four core operations on a settings dictionary:

- **`add_setting(dictionary, pair)`** — adds a new key-value pair; returns an error if the key already exists
- **`update_setting(dictionary, pair)`** — updates an existing key's value; returns an error if the key doesn't exist
- **`delete_setting(dictionary, key)`** — removes a key-value pair; returns an error if the key isn't found
- **`view_settings(dictionary)`** — returns a formatted, human-readable string of all current settings

All keys and values are normalized to lowercase on input, and `view_settings` capitalizes keys for display.

## Example

```python
test_settings = {'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}

print(view_settings(test_settings))
```

```
Current User Settings:
Theme: dark
Notifications: enabled
Volume: high
```

## What I learned

- Unpacking tuples into separate variables
- Checking key existence in a dictionary with `in`
- Using f-strings to build dynamic output
- Why `return` exits a function immediately — and how that can silently break loops if placed incorrectly
- Accumulating a multi-line string across a loop using `.items()`

## Possible next steps

- Add a command-line interface (`while` loop + `input()`) so a user can interact with the settings manager directly, instead of calling functions in code
