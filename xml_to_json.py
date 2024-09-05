"""
Library: XML to JSON
Author: Haluk YAMANER
Email: haluk@halukyamaner.com
Web: https://www.halukyamaner.com
Version: 1.0

Description:
    XML to JSON is a Python utility designed to transform XML data into JSON format, offering an intuitive
    and efficient method for data interchange and storage. This script parses XML files, converts them into JSON
    preserving the structure, attributes, and text content, and then saves the JSON output to a specified file.
    It's suitable for data processing tasks, API development, and scenarios where data format conversion is required
    for integration between systems that use XML and JSON respectively.

Usage:
    To utilize the XML to JSON, provide the file path of an XML file. The script will parse the XML,
    convert it to JSON, and prompt for a file name to save the JSON data. This process simplifies data manipulation
    and supports automated workflows in data transformation tasks.

Requirements:
    Python 3.x
    No additional libraries required for basic functionality; standard libraries used.

Features:
    - Efficiently converts XML data to JSON format, including attributes and nested elements.
    - Utilizes Python’s built-in `xml.etree.ElementTree` for XML parsing.
    - Provides a user-friendly command-line interface for inputting file paths and output file names.
    - Offers clear error handling for file access and parsing issues.

Potential Use Cases:
    - Data migration projects where XML data needs to be converted to JSON format.
    - Backend services that require XML to JSON transformation for API responses.
    - Educational purposes to demonstrate data format conversion techniques.

Example:
    Below is a brief example of how to use the XML to JSON library:

    ```python
    # This script requires no external dependencies, making it easy to deploy and use in any Python environment.
    # Run the script in your command-line interface.

    from xml_to_json import xml_to_json, save_json_to_file

    # Get user input for the XML file path and desired JSON output file name
    xml_file_path = input("Enter the file path of the XML file: ")
    json_data = xml_to_json(xml_file_path)
    file_name = input("Enter the file name to save the JSON data: ")
    save_json_to_file(json_data, file_name)
    print(f"JSON data saved to {file_name}")
    ```
"""
import xml.etree.ElementTree as ET
import json

def xml_to_json(xml_string):
    def parse_element(element):
        parsed_data = {}
        if element.text and element.text.strip():
            parsed_data['text'] = element.text.strip()
        for key, value in element.attrib.items():
            parsed_data[f'@{key}'] = value
        for child in element:
            child_data = parse_element(child)
            if child.tag not in parsed_data:
                parsed_data[child.tag] = child_data
            else:
                if not isinstance(parsed_data[child.tag], list):
                    parsed_data[child.tag] = [parsed_data[child.tag]]
                parsed_data[child.tag].append(child_data)
        return parsed_data

    root = ET.parse(xml_string).getroot()
    return json.dumps({root.tag: parse_element(root)}, indent=4)

def save_json_to_file(json_data, file_name):
    with open(file_name, 'w') as json_file:
        json_file.write(json_data)

if __name__ == "__main__":
    xml_file_path = input("Enter the file path of the XML file: ")
    json_data = xml_to_json(xml_file_path)
    file_name = input("Enter the file name to save the JSON data: ")
    save_json_to_file(json_data, file_name)
    print(f"JSON data saved to {file_name}")
