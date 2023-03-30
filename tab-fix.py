input_file = input("Enter input file name: ")
output_file = "new_" + input_file

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
