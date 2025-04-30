#!/usr/bin/bash

print_sum () { let "sum = $1 + $2"; echo "$1 + $2 = $sum"; }

print_sum 2 5