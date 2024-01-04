spread=$[ 2 ** $1 ]
x_length=$[ $spread * 2 ]
positions=( $[ $x_length / 2 ] )
iterations=$1
line_length=$x_length
while [ $x_length -ge 1 ];do
static_line=$static_line\_
x_length=$[ $x_length - 1]
done
function get_line {
	local x_length=$x_length
	if [ $# -eq 0 ];then
		echo $static_line
		return 0;
	else
		local line=$static_line
		local positions=("$@")
		for position in ${positions[@]};do
			line=${line:0:$[$position - 1]}1${line:$position}
		done
	fi
	echo $line
}
while [ $iterations -gt 0 ];do
	y_spread=$[ $spread / 2 ]
	line=$( get_line ${positions[@]} )
	while [ $y_spread -gt 0 ];do
		echo $line
		y_spread=$[ $y_spread -1 ]
	done
	x_spread=$[ $spread / 2 ]
	index=0
	sub=()
	for position in ${positions[@]};do
        	sub[$index]=$position
        	index=$[ $index + 1 ]
        	sub[$index]=$position
        	index=$[ $index + 1 ]
        done
	while [ $x_spread -gt 0 ];do
		index=0	
		orientation=0
		while [ $index -lt ${#sub[@]} ];do
			if [ $orientation -eq 0 ];then
                		sub[$index]=$[ ${sub[$index]} - 1 ]
				orientation=1
                	else
                		sub[$index]=$[ ${sub[$index]} + 1 ]
				orientation=0
                	fi
			index=$[ $index + 1 ]
		done
		line=$(get_line ${sub[@]})
		echo $line
		x_spread=$[ $x_spread - 1]
	done
	iterations=$[ $iterations - 1]
	spread=$[ $spread / 2]
	positions=( ${sub[@]} )
done
