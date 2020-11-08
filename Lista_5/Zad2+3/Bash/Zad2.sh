#!/bin/bash
declare sum=0

while read -a line; do
  if [[ ${#line[*]} -ge 5 ]]; then
    sum=$(( ${line[4]} + $sum ))
  fi
done

echo "Sum: $sum"