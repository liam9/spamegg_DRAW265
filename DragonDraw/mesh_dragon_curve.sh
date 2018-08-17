# process command line arguments
if [ $# -ne 5 ]; then
	echo "Syntax: mesh_dragon_curve.sh interations line_length colour shadow_scale amount"
	exit
fi

# generate dragon curves

# for 1 shadow
if [ $5 -eq 1 ]; then
	python generate_dragon.py $1 $2 $3 > mesh.txt
	python transform_dragon.py -f $4 -c 1 mesh.txt > mesh_shadow.txt
	python lines_to_svg_colour.py mesh.txt mesh_shadow.txt > mesh.svg
	exit;
fi
# for 2 shadow
if [ $5 -eq 2 ]; then
	python generate_dragon.py $1 $2 $3 > mesh.txt
	python transform_dragon.py -f $4 -c 1 mesh.txt > mesh_shadow0.txt
	python transform_dragon.py -f $4 -c 1 mesh_shadow0.txt > mesh_shadow1.txt
	python lines_to_svg_colour.py mesh.txt mesh_shadow0.txt mesh_shadow1.txt > mesh.svg
	exit;
fi
# for 3 shadow
if [ $5 -eq 3 ]; then
	python generate_dragon.py $1 $2 $3 > mesh.txt
	python transform_dragon.py -f $4 -c 1 mesh.txt > mesh_shadow0.txt
	python transform_dragon.py -f $4 -c 1 mesh_shadow0.txt > mesh_shadow1.txt
	python transform_dragon.py -f $4 -c 1 mesh_shadow1.txt > mesh_shadow2.txt
	python lines_to_svg_colour.py mesh.txt mesh_shadow0.txt mesh_shadow1.txt mesh_shadow2.txt > mesh.svg
	exit;
fi
# for 4 shadow
if [ $5 -eq 4 ]; then
	python generate_dragon.py $1 $2 $3 > mesh.txt
	python transform_dragon.py -f $4 -c 1 mesh.txt > mesh_shadow0.txt
	python transform_dragon.py -f $4 -c 1 mesh_shadow0.txt > mesh_shadow1.txt
	python transform_dragon.py -f $4 -c 1 mesh_shadow1.txt > mesh_shadow2.txt
	python transform_dragon.py -f $4 -c 1 mesh_shadow2.txt > mesh_shadow3.txt
	python lines_to_svg_colour.py mesh.txt mesh_shadow0.txt mesh_shadow1.txt mesh_shadow2.txt mesh_shadow3.txt > mesh.svg
	exit;
fi
# for 5 shadow
if [ $5 -eq 5 ]; then
	python generate_dragon.py $1 $2 $3 > mesh.txt
	python transform_dragon.py -f $4 -c 1 mesh.txt > mesh_shadow0.txt
	python transform_dragon.py -f $4 -c 1 mesh_shadow0.txt > mesh_shadow1.txt
	python transform_dragon.py -f $4 -c 1 mesh_shadow1.txt > mesh_shadow2.txt
	python transform_dragon.py -f $4 -c 1 mesh_shadow2.txt > mesh_shadow3.txt
	python transform_dragon.py -f $4 -c 1 mesh_shadow3.txt > mesh_shadow4.txt
	python lines_to_svg_colour.py mesh.txt mesh_shadow0.txt mesh_shadow1.txt mesh_shadow2.txt mesh_shadow3.txt mesh_shadow4.txt > mesh.svg
	exit;
fi
# for a lot of shadow
echo "amount of shadow too great or too small, reduce to at most 5 or at least 0"
exit;
