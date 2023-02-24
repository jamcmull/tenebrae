import sys
import math

with open(sys.argv[1], 'r', encoding="utf-8") as latin:
	latin_lines = latin.readlines()
	
# first character of first line is garbage
latin_lines[0] = latin_lines[0][1:]

with open(sys.argv[2], 'r') as english:
	english_lines = english.readlines()

# latin files only have verses on odd lines
num_lines = math.ceil(len(latin_lines) / 2)

if num_lines != len(english_lines):
	print("The Latin and English files have a different number of lines.")

with open(sys.argv[3], 'w', encoding="utf-8") as table:
	table.write("\\begin{longtable}{p{10cm} | p{6cm}}\n")
	
	for i in range(num_lines):
		latin_line = latin_lines[i*2]
		latin_line = latin_line.replace("+", "\\GreDagger\\")
		latin_line = latin_line.replace("ǽ", "\\'{\\ae}")
		latin_line = latin_line.replace("Ǽ", "\\'{\\AE}")
		latin_line = latin_line.replace("œ", "\\oe")
		latin_line = latin_line.replace("Œ", "\\OE")
		
		english_line = english_lines[i]
		# remove verse numbers
		english_line = english_line.split(" ", 1)[1]
		
		table.write("%s & \\textit{\\small %s}\\\\\n" % (latin_line, english_line))

	table.write("\\end{longtable}")
