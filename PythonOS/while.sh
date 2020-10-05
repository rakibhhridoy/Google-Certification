#!/bin/bash

#enter first argument as the limit
n=0
end=$1

while [ $n -le $end ]; do
	echo "Iteration number $n"
	((n+=1))
	((a=n**2))
	echo $a

done
