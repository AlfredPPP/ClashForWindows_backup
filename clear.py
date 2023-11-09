import os
import json

def clear_data(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                with open(os.path.join(root, file), 'w') as json_file:
                    json.dump({}, json_file)

if __name__ == "__main__":
    clear_data('tasks')
