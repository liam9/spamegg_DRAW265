import sys
import math
import Line_Point
big_count = 0
'''
purpose
	write to stdout a dragon curve with i iterations, line length l, colour c, spiral(optional) s, and rotation angle(optional) r  preconditions
	i and l are positive non-zero ints and floats (respectively)
	c is a string
'''
def next_line(root, i, turn, r):
	# copy root
	new_line = Line_Point.Line(root.point0, root.point1)

	# translate to origin
	new_line.translate(-root.point0.x, -root.point0.y)

	# rotate and scale
	if turn[i-1] == 'R':
		new_line.rotate(r)
	else:
		new_line.rotate(-r)

	# translate back
	new_line.translate(root.point0.x, root.point0.y)

	# translate tail to head of root
	new_line.translate(root.point1.x - root.point0.x, root.point1.y - root.point0.y)

	return new_line

##### i = iterations, l = line_length, c = colour, t = turn r = rotation_angle
def recursive_draw(root, i, l, c, t, r):
	# end recursion if base case reached
	if (i == 0):
		return

	# print root
	print 'line', root, c

	# continue with recursion
	recursive_draw(next_line(root,i,t), i-1, l, c, t, r)

	
	
##### i = iterations, c = colour, s = total segments, sl = segments left to draw, t = total number of lines
def special_colour(i, c, s, sl, tl, c1, c2, c3):
	palette = ['AliceBlue', 'AntiqueWhite', 'Aqua', 'Aquamarine', 'Azure', 'Beige', 'Bisque', 'Black', 'BlanchedAlmond', 'Blue', 'BlueViolet', 'Brown', 'BurlyWood', 'CadetBlue', 'Chartreuse', 'Chocolate', 'Coral', 'CornflowerBlue', 'Cornsilk', 'Crimson', 'Cyan', 'DarkBlue', 'DarkCyan', 'DarkGoldenRod', 'DarkGray', 'DarkGrey', 'DarkGreen', 'DarkKhaki', 'DarkMagenta', 'DarkOliveGreen', 'DarkOrange', 'DarkOrchid', 'DarkRed', 'DarkSalmon', 'DarkSeaGreen', 'DarkSlateBlue', 'DarkSlateGray', 'DarkSlateGrey', 'DarkTurquoise', 'DarkViolet', 'DeepPink', 'DeepSkyBlue', 'DimGray', 'DimGrey', 'DodgerBlue', 'FireBrick', 'FloralWhite', 'ForestGreen', 'Fuchsia', 'Gainsboro', 'GhostWhite', 'Gold', 'GoldenRod', 'Gray', 'Grey', 'Green', 'GreenYellow', 'HoneyDew', 'HotPink', 'IndianRed', 'Indigo', 'Ivory', 'Khaki', 'Lavender', 'LavenderBlush', 'LawnGreen', 'LemonChiffon', 'LightBlue', 'LightCoral', 'LightCyan', 'LightGoldenRodYellow', 'LightGray', 'LightGrey', 'LightGreen', 'LightPink', 'LightSalmon', 'LightSeaGreen', 'LightSkyBlue', 'LightSlateGray', 'LightSlateGrey', 'LightSteelBlue', 'LightYellow', 'Lime', 'LimeGreen', 'Linen', 'Magenta', 'Maroon', 'MediumAquaMarine', 'MediumBlue', 'MediumOrchid', 'MediumPurple', 'MediumSeaGreen', 'MediumSlateBlue', 'MediumSpringGreen', 'MediumTurquoise', 'MediumVioletRed', 'MidnightBlue', 'MintCream', 'MistyRose', 'Moccasin', 'NavajoWhite', 'Navy', 'OldLace', 'Olive', 'OliveDrab', 'Orange', 'OrangeRed', 'Orchid', 'PaleGoldenRod', 'PaleGreen', 'PaleTurquoise', 'PaleVioletRed', 'PapayaWhip', 'PeachPuff', 'Peru', 'Pink', 'Plum', 'PowderBlue', 'Purple', 'RebeccaPurple', 'Red', 'RosyBrown', 'RoyalBlue', 'SaddleBrown', 'Salmon', 'SandyBrown', 'SeaGreen', 'SeaShell', 'Sienna', 'Silver', 'SkyBlue', 'SlateBlue', 'SlateGray', 'SlateGrey', 'Snow', 'SpringGreen', 'SteelBlue', 'Tan', 'Teal', 'Thistle', 'Tomato', 'Turquoise', 'Violet', 'Wheat', 'White', 'WhiteSmoke', 'Yellow', 'YellowGreen']
	
	if(c == 'Pieces'):
		num = i - (2**s)
		if(num > (2*tl/3)):
			colour = palette[c1]
		elif(num > (tl/3)):
			colour = palette[c2]
		else:
			colour = palette[c3]
		
	elif(c == 'Growing_Pieces'):
		if(sl % 3 == 0):
			colour = palette[c1]
		elif(sl % 3 == 1):
			colour = palette[c2]
		elif(sl % 3 == 2):
			colour = palette[c3]
		
	elif(c == 'Combine'):
		if(i % 100 < 35):
			colour = palette[c1]
		elif(i % 100 < 70):
			colour = palette[c2]
		elif(i % 100 < 100):
			colour = palette[c3]
			
	elif(c == 'Mix'):
		if(i % 3 == 0):
			colour = palette[c1]
		elif(i % 3 == 1):
			colour = palette[c2]
		elif(i % 3 == 2):
			colour = palette[c3]
	
	

	return colour
	
	
##### i = iterations, s = total segments to draw, sl = segments left to draw, l = line_length, c = colour, t = turn r = rotation_angle
def iterative_draw(root, i, s, sl, l, c, t, r):
	count = 0
	pair = 0
	total = (i - 2**s)
	c1 = int(s*l*r)
	c2 = c1+2
	c3 = c2+3
	
	special_colours = ['Mix','Combine','Pieces','Growing_Pieces','Spray']
	while count < i:
		if c in special_colours:
			if(i-2**s < 2**(sl)):
				sl = sl - 1
			colour = special_colour(i, c, s, sl, total, c1, c2, c3)
		else:
			colour = c
		count = count + 1
		print 'line', root, colour
		root = next_line(root,i,t,r)
		i = i - 1
		
##### i = iterations, l = line_length, c = colours in list, t = turn r = rotation_angle
def iterative_draw_c(root, i, l, c, t, r):
	count = 0
	pair = 0
	while count < i:
		if count%100 == 0:
			pair = pair + 1
			if pair == c:
				pair = 0
		count = count + 1
		print 'line', root, colours[pair]
		root = next_line(root,i,t,r)
		i = i - 1	

		
#### not usable past 8 iterations, python caps at 999 iterations
def recursive_map(map, i):
	if i == 0:
		return map
	else:
		map.append('R')
		offset = len(map)
		for x in reversed(map[:offset-1]):
			if x == 'R':
				map.append('L')
			else:
				map.append('R')
		return recursive_map(map, i-1)
#### usable past 8 iterations

def iterative_map(map, i):
	count = 0
	while count < i:
		count = count + 1
		map.append('R')
		offset = len(map)
		for y in reversed(map[:offset-1]):
			if y == 'R':
				map.append('L')
			else:
				map.append('R')
	return map	

# ********** process the command line arguments
if ((len(sys.argv) != 5) and (len(sys.argv)!= 4)):
	print >> sys.stderr, 'Requires command line input: ' + sys.argv[0] + ' iterations line_length colour rotation_angle'
	sys.exit(1)
try:
	iterations = int(sys.argv[1])
	line_length = float(sys.argv[2])
	colour = str(sys.argv[3])
	####if no rotation angle is not provided in the command line then the standard pi/2 rotation is used
	if len(sys.argv) == 4:
		rotation_angle = float((math.pi)/2)
	elif len(sys.argv) == 5:
		rotation_angle = float(sys.argv[4])
	if (rotation_angle < 1.45) or (rotation_angle > 1.63):
		print >> sys.stderr, 'To resemble the standard dragon curve the rotation angle should be  1.45 < r < 1.63'
		print >> sys.stderr, 'Rotation angle r can go out of the recommended range for experimentation'
		print >> sys.stderr, 'Inorder to make the imager clearer as the rotation angle increases the line length should increase'
		print >> sys.stderr, 'Inorder to keep the image in the frame as the rotation angle decreases the line length should decrease'
		
except ValueError:
	print >> sys.stderr, 'Requires command line input: ' + sys.argv[0] + ' iterations(int > 0) line_length(float > 0) colour(String)'
	sys.exit(2)
if iterations < 1 or line_length < 1:
	print >> sys.stderr, 'Requires command line input: ' + sys.argv[0] + ' iterations(int > 0) line_length(float > 0) colour(String)'
	sys.exit(3)
# colour scheme idea
colours = ['AliceBlue', 'AntiqueWhite', 'Aqua', 'Aquamarine', 'Azure', 'Beige', 'Bisque', 'Black', 'BlanchedAlmond', 'Blue', 'BlueViolet', 'Brown', 'BurlyWood', 'CadetBlue', 'Chartreuse', 'Chocolate', 'Coral', 'CornflowerBlue', 'Cornsilk', 'Crimson', 'Cyan', 'DarkBlue', 'DarkCyan', 'DarkGoldenRod', 'DarkGray', 'DarkGrey', 'DarkGreen', 'DarkKhaki', 'DarkMagenta', 'DarkOliveGreen', 'DarkOrange', 'DarkOrchid', 'DarkRed', 'DarkSalmon', 'DarkSeaGreen', 'DarkSlateBlue', 'DarkSlateGray', 'DarkSlateGrey', 'DarkTurquoise', 'DarkViolet', 'DeepPink', 'DeepSkyBlue', 'DimGray', 'DimGrey', 'DodgerBlue', 'FireBrick', 'FloralWhite', 'ForestGreen', 'Fuchsia', 'Gainsboro', 'GhostWhite', 'Gold', 'GoldenRod', 'Gray', 'Grey', 'Green', 'GreenYellow', 'HoneyDew', 'HotPink', 'IndianRed', 'Indigo', 'Ivory', 'Khaki', 'Lavender', 'LavenderBlush', 'LawnGreen', 'LemonChiffon', 'LightBlue', 'LightCoral', 'LightCyan', 'LightGoldenRodYellow', 'LightGray', 'LightGrey', 'LightGreen', 'LightPink', 'LightSalmon', 'LightSeaGreen', 'LightSkyBlue', 'LightSlateGray', 'LightSlateGrey', 'LightSteelBlue', 'LightYellow', 'Lime', 'LimeGreen', 'Linen', 'Magenta', 'Maroon', 'MediumAquaMarine', 'MediumBlue', 'MediumOrchid', 'MediumPurple', 'MediumSeaGreen', 'MediumSlateBlue', 'MediumSpringGreen', 'MediumTurquoise', 'MediumVioletRed', 'MidnightBlue', 'MintCream', 'MistyRose', 'Moccasin', 'NavajoWhite', 'Navy', 'OldLace', 'Olive', 'OliveDrab', 'Orange', 'OrangeRed', 'Orchid', 'PaleGoldenRod', 'PaleGreen', 'PaleTurquoise', 'PaleVioletRed', 'PapayaWhip', 'PeachPuff', 'Peru', 'Pink', 'Plum', 'PowderBlue', 'Purple', 'RebeccaPurple', 'Red', 'RosyBrown', 'RoyalBlue', 'SaddleBrown', 'Salmon', 'SandyBrown', 'SeaGreen', 'SeaShell', 'Sienna', 'Silver', 'SkyBlue', 'SlateBlue', 'SlateGray', 'SlateGrey', 'Snow', 'SpringGreen', 'SteelBlue', 'Tan', 'Teal', 'Thistle', 'Tomato', 'Turquoise', 'Violet', 'Wheat', 'White', 'WhiteSmoke', 'Yellow', 'YellowGreen']

fun = False
if colour == 'Fun':
	fun = True

# root: length line_length, in middle of canvas
point0 = Line_Point.Point(0.0,0.0)
point1 = Line_Point.Point(0.0,0.0 + line_length)
root = Line_Point.Line(point0, point1)
map = ['R']
new_map = iterative_map(map, iterations)
its = len(new_map)
cs = len(colours)


if fun:
	iterative_draw_c(root,its,line_length,cs,new_map,rotation_angle)
else:
	iterative_draw(root,its,iterations,iterations,line_length,colour,new_map,rotation_angle)
