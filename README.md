# GPT-Tab-Fix
## Python script to convert spaces to tabs

This Python script reads a file line by line, detects the number of spaces used for tab indents, and replaces the appropriate amount of tabs into their place.

## Usage

1. Make sure you have Python 3 installed on your system.
2. Place the script in the same directory as the file you want to convert.
3. Open a terminal or command prompt and navigate to the script directory.
4. Run the script by typing `python tab-fix.py`.
5. Follow the prompts to enter the name of the input file


## Notes

- The script assumes that each tab indent is equivalent to 4 spaces. If your code uses a different number of spaces per tab, you will need to adjust the script accordingly.
- The script will replace spaces with tabs only at the beginning of each line. If you have spaces in the middle of a line that you want to replace with tabs, you will need to do so manually.
