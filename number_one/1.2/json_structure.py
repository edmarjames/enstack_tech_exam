import json

# load data from the JSON file
with open("section_a.json", "r") as file:
    section_a = json.load(file)

# remove leading or trailing spaces from each key and value
section_a = [{key.strip(): value.strip() for key, value in item.items()}
             for item in section_a]

# build hierarchical structure
tree = {}
for item in section_a:
    manager = item.get("manager_name", "")
    employee = item.get("login_name", "")

    if manager not in tree:
        tree[manager] = {"name": manager, "subordinate": []}
    if employee not in tree:
        tree[employee] = {"name": employee, "subordinate": []}

    tree[manager]["subordinate"].append(tree[employee])

# find top-level managers, those never listed as subordinates
top_level_managers = set(tree.keys()) - {item.get("login_name") for item in section_a}

# function to clean up empty 'subordinate' lists
def clean_tree(node):
    if not node["subordinate"]:
        del node["subordinate"]
    else:
        node["subordinate"] = [clean_tree(sub) for sub in node["subordinate"]]
    return node

# transform tree to required format
section_b = [clean_tree(tree[manager]) for manager in top_level_managers]

# print final output into JSON
print(json.dumps(section_b, indent=4))