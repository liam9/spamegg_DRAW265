# process command line arguments
# it is a good idea to use smaller curves for making rings
if [ $# -eq 3 ]; then
	python transform_dragon.py -x 100 $1 > dragon.txt
	python transform_dragon.py -a $3 -n $2 dragon.txt > dragon_ring.txt
	python lines_to_svg_colour.py dragon_ring.txt > dragon_ring.svg
	exit;
fi

if [ $# -eq 5 ]; then
	python generate_dragon.py $1 $2 $3 > dragon0.txt
	python transform_dragon.py -x 100 dragon0.txt > dragon1.txt
	python transform_dragon.py -a $5 -n $4 dragon1.txt > dragon_ring.txt
	python lines_to_svg_colour.py dragon_ring.txt > dragon_ring.svg
	exit;
fi


echo "Syntax: simple_dragon_curve.sh interations line_length colour amount angle"
echo "or: simple_dragon_curve.sh file_name.txt amount angle"
exit