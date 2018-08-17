# process command line arguments
if [ $# -ne 4 ]; then
	echo "Syntax: bash dragonbash_rings.sh number_of_rings dragon_height branch_angle branch_factor"
	exit
fi

number_of_dragons=$1
iterations=$2
line_length=$3
colour=$4

# generate dragon
python generate_dragon.py $iterations $line_length $colour > dragon.txt
python rotate_scale_translate.py -x 0 -y 250.0 dragon.txt > dragon0.txt
python rotate_scale_translate.py -f 0.7 dragon0.txt > dragon1.txt
python rotate_scale_translate.py -x 0 -y -60.0 dragon1.txt > dragon2.txt

# replicate dragon in rings
python dragon_rings.py $number_of_dragons < dragon2.txt > dragon_rings.txt
python lines_to_svg_colour.py dragon_rings.txt > dragon_rings.svg
