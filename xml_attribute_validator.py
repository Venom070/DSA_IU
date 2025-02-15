import xml.etree.ElementTree as ET

def validate_attribute(key, value):
    """
    Validates an attribute based on custom rules.
    Returns True if the attribute is valid, False otherwise.
    """
    if not value:  # Check if the attribute is empty
        return False
    if any(char in value for char in ['$', '%', '^']):  # Check for invalid characters
        return False
    return True

def find_broken_attributes(node, path="root"):
    """
    Recursively traverses the XML tree and identifies broken attributes.
    Prints and returns the locations and values of broken attributes.
    """
    broken_attributes = []
    
    # Check attributes of the current node
    for key, value in node.attrib.items():
        if not validate_attribute(key, value):
            broken_attributes.append((path, key, value))
            print(f"Broken attribute found at {path}/{key}: {value}")
    
    # Recur for child nodes
    for child in node:
        child_path = f"{path}/{child.tag}"
        broken_attributes.extend(find_broken_attributes(child, child_path))
    
    return broken_attributes

def main():
    """
    Main function to parse the XML document, process it, and identify broken attributes.
    """
    # Sample XML document
    xml_data = """
    <data>
        <user id="123" name="JohnDoe" email="john@doe.com" />
        <user id="124" name="Jane$Doe" email="jane@doe.com" />
        <user id="125" name="Invalid%" email="" />
        <user id="126" name="ValidUser" email="valid@user.com">
            <details age="30" address="123 Main St" />
            <details age="" address="456 Elm St" />
        </user>
    </data>
    """
    
    # Parse the XML document
    root = ET.fromstring(xml_data)
    
    # Find and output broken attributes
    print("Starting recursive traversal to find broken attributes...")
    broken_attributes = find_broken_attributes(root)
    
    print("\nSummary of broken attributes:")
    for path, key, value in broken_attributes:
        print(f"Path: {path}, Attribute: {key}, Value: '{value}'")
    
if _name_ == "_main_":
    main()
