# 📚 Narration Parser Toolkit 📚

## What is this? 🤔

This toolkit contains lightweight Python utilities for processing story text:

### 1️⃣ Narration Parser

A tool that extracts narration from story text by filtering out dialogue! It works by:

- ✨ Preserving all narration text as-is
- 💬 Using double quotes (") as delimiters to identify speech
- 📝 Writing text continuously until dialogue is encountered
- ⏭️ Skipping all text inside quotes (the speech parts)
- 📊 Starting a new line after each speech segment
- 🔄 Processing entire documents from start to finish

Perfect for writers, editors, and text analysts who need to separate narration from dialogue! 🎯

### 2️⃣ Empty Line Eliminator

A complementary tool that removes empty lines from text files:

- 🧹 Loads any text file 
- 🔍 Identifies and removes all empty lines
- 💾 Saves to a new file with "-cleaned" added to the original filename
- ✅ Preserves all non-empty text exactly as it appears

Ideal for cleaning up processed text files and preparing them for analysis! 🧪

### 2️⃣ Empty Line Eliminator

A complementary tool that removes empty lines from text files:

- 🧹 Loads any text file 
- 🔍 Identifies and removes all empty lines
- 💾 Saves to a new file with "-cleaned" added to the original filename
- ✅ Preserves all non-empty text exactly as it appears

Ideal for cleaning up processed text files and preparing them for analysis! 🧪

## Installation 🚀

### Prerequisites
- Python 3.6 or higher 🐍

### Quick Install

1. Clone the repository:
```bash
git clone https://github.com/yourusername/narration-parser.git
cd narration-parser
```

2. No additional dependencies required! 🥳

## How to Use 🛠️

### Basic Usage

1. Place your story text files in the same directory as the script (or specify paths).
2. Run the script using the command line interface.
3. Receive formatted narration with all dialogue removed! 🎉

### Examples

#### Process a file and save the output:
```bash
python narration_parser.py my_story.txt narration_output.txt
```

#### Process a file and display output in console:
```bash
python narration_parser.py my_story.txt
```

### Quick Testing with Batch Files

#### For Narration Parser:
The included `run_narration.bat` file provides a template for quick testing:

1. Edit the batch file to include your file paths
2. Run the batch file to process your stories
3. Check the output files! 📊

#### For Empty Line Eliminator:
The included `test-eliminator.bat` file makes testing easy:

1. Edit the batch file with your text file paths
2. Run the batch file to remove empty lines
3. Check the cleaned files with the "-cleaned" suffix! 🧹

## CLI Usage 💻

### Narration Parser

```
python narration_parser.py input_file [output_file]
```

#### Parameters:
- `input_file`: Path to the story file you want to process 📄
- `output_file`: (Optional) Path where the processed narration will be saved 💾
  - If omitted, output will be displayed in the console

### Empty Line Eliminator

```
python empty_eliminator.py input_file
```

#### Parameters:
- `input_file`: Path to the text file you want to clean 📄
- Output will be saved to `[original_filename]-cleaned[extension]` automatically

## Programmatic Usage 🧩

### Narration Parser:

```python
from narration_parser import parse_narration

# Process a file and get result as string
narration_text = parse_narration("my_story.txt")

# Process a file and save to output file
parse_narration("my_story.txt", "output.txt")
```

### Empty Line Eliminator:

```python
from empty_eliminator import remove_empty_lines

# Process a file and remove empty lines
cleaned_file_path = remove_empty_lines("my_text.txt")
# Result saved to "my_text-cleaned.txt"
```

## Use Cases 🌟

### For Narration Parser:
- 📝 Analyze writing style in narration separately from dialogue
- 🔍 Extract descriptive passages for study or reference
- 🎭 Compare narration-to-dialogue ratios across works
- 🖋️ Focus on narrative techniques without dialogue distractions
- 📚 Create narration-only versions of texts for specific analyses

### For Empty Line Eliminator:
- 🧹 Clean up text files with excessive line breaks
- 🔧 Prepare processed texts for further analysis
- 📊 Standardize text formatting across multiple files
- 📋 Make texts more compact for viewing or printing
- 🔄 Process output from other text tools (like Narration Parser!)

### Combined Workflow:
1️⃣ Extract narration with `narration_parser.py`
2️⃣ Clean up the result with `empty_eliminator.py`
3️⃣ Get perfectly formatted narration-only text! ✨

## Coming Soon ✨

- 🌈 Support for different quote styles in Narration Parser
- 📊 Statistics on narration vs. dialogue percentages
- 🔄 Batch processing improvements for both tools
- 🌐 Web interface for online text processing
- 🔗 Integrated workflow between tools with a single command
- 📱 More text processing utilities to expand the toolkit

## License

This project will be released under the MIT License.

## Enjoy! 🎉

Happy narration parsing! If you find this tool useful, please star the repository! ⭐