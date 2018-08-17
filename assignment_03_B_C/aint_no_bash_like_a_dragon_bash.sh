# process command line arguments
if [ $# -ne 4 ]; then
	echo "Syntax: bash aint_no_bash_like_a_dragon_bash.sh interations line_length colour"
	exit
fi


# generate dragon
python generate_dragon.py $1 $2 $3 | python lines_to_svg_colour.py > bashdragon.svg

# replicate dragons in transform_dragons

