#!/usr/bin/env python3
"""
narration_parser.py

This script processes a story page into a narration list format by:
- Preserving all text as-is
- Using double quotes (") as delimiters to identify speech
- Writing text on single lines until a quote is reached
- Skipping text inside quotes (speech)
- Starting a new line after each speech segment
- Processing the entire document
"""

def parse_narration(input_file, output_file=None):
    """
    Parse a story file, extracting only narration and skipping speech.
    
    The function copies all text until a quote mark is reached, skips the text
    between quote marks, and then continues copying text after the closing quote
    on a new line.
    
    Args:
        input_file (str): Path to the input story file
        output_file (str, optional): Path to save the output. If None, returns the result as a string.
    
    Returns:
        str: The parsed narration if output_file is None
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
    
    output_lines = []
    current_pos = 0
    
    while current_pos < len(text):
        # Find the next opening quote
        opening_quote = text.find('"', current_pos)
        
        if opening_quote == -1:
            # No more quotes, add the rest of the text
            output_lines.append(text[current_pos:])
            break
        
        # Add text before the opening quote
        output_lines.append(text[current_pos:opening_quote])
        
        # Find the closing quote
        closing_quote = text.find('"', opening_quote + 1)
        if closing_quote == -1:
            # No closing quote found, we're done
            break
        
        # Skip the speech and continue from after the closing quote
        current_pos = closing_quote + 1
    
    # Join all lines with newline characters
    result = '\n'.join(output_lines)
    
    if output_file:
        try:
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(result)
            print(f"Narration saved to {output_file}")
            return None
        except Exception as e:
            print(f"Error writing to file: {e}")
            return result
    else:
        return result

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else None
        result = parse_narration(input_file, output_file)
        if result is not None and not output_file:
            print(result)
    else:
        print("Usage: python narration_parser.py input_file [output_file]")
        print("Example: python narration_parser.py page0_enhanced.txt narration.txt")
