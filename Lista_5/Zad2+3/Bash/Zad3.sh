#!/bin/bash
declare sum=0
declare country=$1

while read -a line; do
  if [[ ${#line[*]} -ge 7 && ${line[6]} == "$country" ]]; then
    sum=$(( ${line[4]} + $sum ))
  fi
done

echo "Sum: $sum"