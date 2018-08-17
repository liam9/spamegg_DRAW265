'''
This code is an edited version of rotate_scale_translate.py from assignment 3 of SENG 265

'''
import sys
import copy
import math
import Line_Point

'''
purpose
	parse argv:
		[-a angle] [-f factor] [-n count] [-x delta_x] [-y delta_y] [-c colour_delta] [file(s)]
	if legal
		return dictionary of option/option value pairs
		use None for option value if option not present
		use 'file_names':L
			where L is a list of the file names and [ ] if no files present
	else
		return error message
'''
def colour_options(jump_factor, initial):
	
	all_the_colours = ['AliceBlue', 'AntiqueWhite', 'Aqua', 'Aquamarine', 'Azure', 'Beige', 'Bisque', 'Black', 'BlanchedAlmond', 'Blue', 'BlueViolet', 'Brown', 'BurlyWood', 'CadetBlue', 'Chartreuse', 'Chocolate', 'Coral', 'CornflowerBlue', 'Cornsilk', 'Crimson', 'Cyan', 'DarkBlue', 'DarkCyan', 'DarkGoldenRod', 'DarkGray', 'DarkGrey', 'DarkGreen', 'DarkKhaki', 'DarkMagenta', 'DarkOliveGreen', 'DarkOrange', 'DarkOrchid', 'DarkRed', 'DarkSalmon', 'DarkSeaGreen', 'DarkSlateBlue', 'DarkSlateGray', 'DarkSlateGrey', 'DarkTurquoise', 'DarkViolet', 'DeepPink', 'DeepSkyBlue', 'DimGray', 'DimGrey', 'DodgerBlue', 'FireBrick', 'FloralWhite', 'ForestGreen', 'Fuchsia', 'Gainsboro', 'GhostWhite', 'Gold', 'GoldenRod', 'Gray', 'Grey', 'Green', 'GreenYellow', 'HoneyDew', 'HotPink', 'IndianRed', 'Indigo', 'Ivory', 'Khaki', 'Lavender', 'LavenderBlush', 'LawnGreen', 'LemonChiffon', 'LightBlue', 'LightCoral', 'LightCyan', 'LightGoldenRodYellow', 'LightGray', 'LightGrey', 'LightGreen', 'LightPink', 'LightSalmon', 'LightSeaGreen', 'LightSkyBlue', 'LightSlateGray', 'LightSlateGrey', 'LightSteelBlue', 'LightYellow', 'Lime', 'LimeGreen', 'Linen', 'Magenta', 'Maroon', 'MediumAquaMarine', 'MediumBlue', 'MediumOrchid', 'MediumPurple', 'MediumSeaGreen', 'MediumSlateBlue', 'MediumSpringGreen', 'MediumTurquoise', 'MediumVioletRed', 'MidnightBlue', 'MintCream', 'MistyRose', 'Moccasin', 'NavajoWhite', 'Navy', 'OldLace', 'Olive', 'OliveDrab', 'Orange', 'OrangeRed', 'Orchid', 'PaleGoldenRod', 'PaleGreen', 'PaleTurquoise', 'PaleVioletRed', 'PapayaWhip', 'PeachPuff', 'Peru', 'Pink', 'Plum', 'PowderBlue', 'Purple', 'RebeccaPurple', 'Red', 'RosyBrown', 'RoyalBlue', 'SaddleBrown', 'Salmon', 'SandyBrown', 'SeaGreen', 'SeaShell', 'Sienna', 'Silver', 'SkyBlue', 'SlateBlue', 'SlateGray', 'SlateGrey', 'Snow', 'SpringGreen', 'SteelBlue', 'Tan', 'Teal', 'Thistle', 'Tomato', 'Turquoise', 'Violet', 'Wheat', 'White', 'WhiteSmoke', 'Yellow', 'YellowGreen']
	count = 0
	for x in all_the_colours:
		count = count + 1
		if initial == x:
			break
	
	initial_at = count
	
	while initial_at + jump_factor > len(all_the_colours)-1:
		initial_at = initial_at + jump_factor - len(all_the_colours)-1
		if initial_at < len(all_the_colours)-1:
			return all_the_colours[initial_at]
	
	return all_the_colours[initial_at + jump_factor]
	
		
	
def parse_argv(argv):
	D = { '-a':None, '-f':None, '-n':None, '-x':None, '-y':None, '-c':None,'file_names':[] }

	i = 1
	while i < len(sys.argv) and sys.argv[i][0] == '-':
		# *** duplicate option, illegal option
		if sys.argv[i] in D:
			if D[sys.argv[i]] != None:
				return 'Duplicate option: ' + sys.argv[i]
		else:
			return 'Illegal option: ' + sys.argv[i]

		# *** extract option value
		option = sys.argv[i]
		i = i + 1
		if i >= len(sys.argv):
			return 'Missing option value for: ' + sys.argv[i]
		option_value = sys.argv[i]

		# *** -a option
		if option == '-a':
			try:
				D['-a'] = float(option_value)
			except ValueError:
				return 'Illegal option value: ' + option + ' ' + option_value
		# *** -f option
		elif option == '-f':
			try:
				D['-f'] = float(option_value)
			except ValueError:
				return 'Illegal option value: ' + option + ' ' + option_value
		# *** -x option
		elif option == '-x':
			try:
				D['-x'] = float(option_value)
			except ValueError:
				return 'Illegal option value: ' + option + ' ' + option_value
		# *** -y option
		elif option == '-y':
			try:
				D['-y'] = float(option_value)
			except ValueError:
				return 'Illegal option value: ' + option + ' ' + option_value	
		# *** -c option
		elif option == '-c':
			try:
				D['-c'] = float(option_value)
			except ValueError:
				return 'Illegal option value: ' + option + ' ' + option_value
		# *** -n option: int
		else:
			try:
				D['-n'] = int(option_value)
			except ValueError:
				return 'Illegal option value: ' + option + ' ' + option_value
		

		# advance to next option
		i = i + 1
	
	# add file_names to D
	D['file_names'] = sys.argv[i:]
	if D['file_names'] == [ ]:
		D['file_names'] = None
	
	return D

# ***** apply rotate, scale, translate
def process_lines_file(file_object, options):
	for line in file_object:
		# convert L to a Line object
		L = line.split()
		point0 = Line_Point.Point(float(L[1]), float(L[2]))
		point1 = Line_Point.Point(float(L[3]), float(L[4]))
		line = Line_Point.Line(point0, point1)
		colour = L[5]
		# rotate, scale, translate and write line count times
		for i in range(options['-n']):
			line.rotate(options['-a'])
			line.scale(options['-f'])
			line.translate(options['-x'], options['-y'])
			if options['-c'] > 0.0:
				jump_factor = int(options['-c'])
				oldc = colour
				colour = colour_options(jump_factor,oldc)
			print 'line', line, colour


# *** handle command-line arguments
options = parse_argv(sys.argv)
if type(options) == str:
	print >> sys.stderr, options
	sys.exit()

# *** apply defaults where needed
default_options = { '-a':0.0, '-f':1.0, '-n':1, '-x':0.0, '-y':0.0, '-c':0.0 }
for option in default_options:
	if options[option] == None:
		options[option] = default_options[option]

# *** process each input file

if options['file_names'] == None:
	process_lines_file(sys.stdin, options)
else:
	for file_name in options['file_names']:
		try:
			file_object = open(file_name, 'r')
		except IOError:
			print >> sys.stderr, 'Cannot open file:', file_name
			sys.exit()
		process_lines_file(file_object, options)
