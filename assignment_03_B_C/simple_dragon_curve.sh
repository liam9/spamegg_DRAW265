# process command line arguments
if [ $# -ne 3 ]; then
	echo "Syntax: simple_dragon_curve.sh interations line_length colour"
	exit
fi

# generate dragon curves
python generate_dragon.py $1 $2 $3 > simple_dragon_curve.txt
python lines_to_svg_colour.py simple_dragon_curve.txt > simple_dragon_curve.svg

