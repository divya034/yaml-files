import yaml

# Open the YAML file
with open("data.yaml", "r") as f:
    # Load the YAML data
    data = yaml.safe_load(f)

    # Iterate over the data looking for comments
    for key, value in data.items():
        # Check if the value is a string and starts with a "#"
        if isinstance(value, str) and value.startswith("#"):
            # Print the comment
            print(value)