import argparse
parser = argparse.ArgumentParser()
parser.add_argument('i', type=str, help='Input file')
parser.add_argument('o', type=str, help='Output file')

args=parser.parse_args()

input_file = args.i
output_file = args.o

with open(input_file, "r") as f_in:
	with open(output_file, "w") as f_out:
		for line in f_in:
			spaces = ""
			for char in line:
				if char == " ":
					spaces += char
				else:
					num_tabs = (len(spaces) + 3) // 4
					tabs = "\t" * num_tabs
					new_line = tabs + line[len(spaces):]
					f_out.write(new_line)
					break
