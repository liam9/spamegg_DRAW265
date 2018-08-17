#process command line arguments
if [ $# -ne 1 ]; then
	echo "Syntax: simple_dragon_curve.sh interations"
	exit
fi



# generate dragons and transform the colours and positions
python generate_dragon.py $1 100 Growing_Pieces 3.0 > dragon.txt

#convert to svg
python lines_to_svg_colour.py dragon.txt > hand_fan.svg
