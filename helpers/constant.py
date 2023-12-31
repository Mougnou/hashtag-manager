import os
import sys 
import json   
# Get the path of the executable
exe_path = sys.executable

# Get the directory of the executable
exe_dir = os.path.dirname(exe_path)

# Define the new directory path
json_dir = os.path.join(exe_dir, 'json')

# Create the new directory
os.makedirs(json_dir, exist_ok=True)
#create the two json files


HASHTAG_LIST_JSON_PATH = os.path.join(json_dir, 'hashtag_list.json')
SETTING_JSON_PATH = os.path.join(json_dir, 'setting.json')

# Create 'hashtag_list.json' if it doesn't exist
if not os.path.exists(HASHTAG_LIST_JSON_PATH):
    content = {
        "hashtags": [
            {
                "name": "The French Dad",
                "hashtag_list": [
                    "#France",
                    "#BAGUETTE",
                    "#fromage"
                ]
            }
        ]
    }
    with open(HASHTAG_LIST_JSON_PATH, 'w') as f:
        json.dump(content, f)  # Initialize with an empty list

# Create 'setting.json' if it doesn't exist
if not os.path.exists(SETTING_JSON_PATH):
    content = {
    "timeToWait": "",
    "cursorPosition": {
        "x": "",
        "y": ""
    }
}
    with open(SETTING_JSON_PATH, 'w') as f:
        json.dump(content, f)  # Initialize with an empty dictionary