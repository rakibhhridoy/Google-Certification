#!/bin/bash

for fruit in peach guava mango pineapple; do
	echo "I like $fruit"

done

names=(rakib hasan hridoy aminul bulbul)

for name in "${names[@]}"; do
	echo "$name"

done


for index in "${!names[@]}"; do
	echo "index are: $index"
done


declare -A array

array["name1"]=rakib
array+=( ["name2"]=aminul ["name3"]=bulbul )

for key in "${!array[@]}"; do
	echo "key: $key, value: ${array[${key}]}"
done



#unset array
