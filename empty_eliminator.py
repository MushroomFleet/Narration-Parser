#!/usr/bin/env python3
"""
empty_eliminator.py

A simple script to remove empty lines from text files.
- Loads a text file
- Removes all empty lines
- Saves the result to a new file with "-cleaned" added to the original filename
- Preserves all non-empty text exactly as it appears in the original
"""

import sys
import os


def remove_empty_lines(input_file):
    """
    Remove empty lines from a text file and save to a new file with "-cleaned" suffix.
    
    Args:
        input_file (str): Path to the input text file
    
    Returns:
        str: Path to the output file
    """
    # Check if file exists
    if not os.path.isfile(input_file):
        print(f"Error: File '{input_file}' not found.")
        return None
    
    try:
        # Read the input file
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # Filter out empty lines (keeping lines with content)
        non_empty_lines = [line for line in lines if line.strip()]
        
        # Create output filename with "-cleaned" suffix
        file_name, file_ext = os.path.splitext(input_file)
        output_file = f"{file_name}-cleaned{file_ext}"
        
        # Write filtered content to output file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.writelines(non_empty_lines)
        
        print(f"Successfully cleaned '{input_file}'")
        print(f"Result saved to '{output_file}'")
        
        return output_file
    
    except Exception as e:
        print(f"Error processing file: {e}")
        return None


if __name__ == "__main__":
    # Check for command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python empty_eliminator.py <filename>")
        print("Example: python empty_eliminator.py my_text.txt")
        sys.exit(1)
    
    # Get input filename from command-line argument
    input_file = sys.argv[1]
    
    # Process the file
    remove_empty_lines(input_file)