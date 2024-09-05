# XML to JSON

## Overview
The XML to JSON is a Python utility designed to convert XML files into JSON format. This tool parses an XML file and transforms it into a structured JSON document, preserving the hierarchical relationship of the XML elements.

## Features
- **XML Parsing**: Efficiently parses XML data and extracts attributes, tags, and text.
- **JSON Conversion**: Converts the parsed XML data into a well-structured JSON format.
- **File Handling**: Allows users to specify both the source XML file and the destination JSON file through the command line.

## Requirements
- Python 3.x
- `xml.etree.ElementTree` module for XML parsing
- `json` module for JSON formatting

## Usage
To convert an XML file to JSON, run the script from the command line. You will be prompted to enter the path of the XML file and the desired name for the resulting JSON file.

```bash
python xml_to_json.py
