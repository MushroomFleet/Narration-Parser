# 📚 Narration Parser 📚

## What is this? 🤔

Narration Parser is a lightweight Python tool that extracts narration from story text by filtering out dialogue! It works by:

- ✨ Preserving all narration text as-is
- 💬 Using double quotes (") as delimiters to identify speech
- 📝 Writing text continuously until dialogue is encountered
- ⏭️ Skipping all text inside quotes (the speech parts)
- 📊 Starting a new line after each speech segment
- 🔄 Processing entire documents from start to finish

Perfect for writers, editors, and text analysts who need to separate narration from dialogue! 🎯

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

### Quick Testing with Batch File

The included `run_narration.bat` file provides a template for quick testing:

1. Edit the batch file to include your file paths
2. Run the batch file to process your stories
3. Check the output files! 📊

## CLI Usage 💻

```
python narration_parser.py input_file [output_file]
```

### Parameters:
- `input_file`: Path to the story file you want to process 📄
- `output_file`: (Optional) Path where the processed narration will be saved 💾
  - If omitted, output will be displayed in the console

## Programmatic Usage 🧩

You can also import the script in your own Python code:

```python
from narration_parser import parse_narration

# Process a file and get result as string
narration_text = parse_narration("my_story.txt")

# Process a file and save to output file
parse_narration("my_story.txt", "output.txt")
```

## Use Cases 🌟

- 📝 Analyze writing style in narration separately from dialogue
- 🔍 Extract descriptive passages for study or reference
- 🎭 Compare narration-to-dialogue ratios across works
- 🖋️ Focus on narrative techniques without dialogue distractions
- 📚 Create narration-only versions of texts for specific analyses

## Coming Soon ✨

- 🌈 Support for different quote styles
- 📊 Statistics on narration vs. dialogue percentages
- 🔄 Batch processing improvements
- 🌐 Web interface

## License

This project will be released under the MIT License.

## Enjoy! 🎉

Happy narration parsing! If you find this tool useful, please star the repository! ⭐
