#process command line arguments
if [ $# -ne 3 ]; then
	echo "Syntax: dragon_spin.sh interations line_length colour"
	exit
fi



# generate dragons and transform the colours and positions
python generate_dragon.py $1 $2 $3 > dragon.txt
python transform_dragon.py -x -20 -y -20 dragon.txt > dragon_transform.txt

python generate_dragon.py $1 $2 $3 1.5 > dragon2.txt
python transform_dragon.py -x -10 -y -10 -c 1 dragon2.txt > dragon2_transform.txt

python generate_dragon.py $1 $2 $3 1.4 > dragon3.txt
python transform_dragon.py -c 2 dragon3.txt > dragon3_transform.txt

python generate_dragon.py $1 $2 $3 1.3 > dragon4.txt
python transform_dragon.py -x 10 -y 10 -c 3 dragon4.txt > dragon4_transform.txt

python generate_dragon.py $1 $2 $3 1.2 > dragon5.txt
python transform_dragon.py -x 20 -y 20 -c 4 dragon5.txt > dragon5_transform.txt


#convert all dragons to svg
python lines_to_svg_colour.py dragon_transform.txt dragon2_transform.txt dragon3_transform.txt dragon4_transform.txt dragon5_transform.txt > dragon_evolution.svg
