test_settings = {
    'Theme' : 'dark',
    'Notifications': 'enabled',
    'Volume' : 'high'
}

def add_setting(dictionary, pairs):
    key, value = pairs
    key = key.lower()
    value = value.lower()
    if key in dictionary:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        dictionary[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"
def update_setting(dictionary, pairs):
    key, value = pairs
    key = key.lower()
    value = value.lower()
    
    if key in dictionary:
        dictionary[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
def delete_setting(dictionary, key):
    key = key.lower()

    if key in dictionary:
        dictionary.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"
def view_settings(dictionary):
    if dictionary == {}:
        return "No settings available."
    else:
        results = "Current User Settings:"
        for key, value in dictionary.items():
            results += f"\n{key.capitalize()}: {value}"
        return results + '\n'

print(view_settings(test_settings))