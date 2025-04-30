#!usr/bin/bash

gcd ()  # n1 n2
{
    n1=$1
    n2=$2
    if [ $n1 -eq $n2 ]; then
      echo "GCD is $n1"
    elif [ $n1 -gt $n2 ]; then
      let "n1 -= n2"
      gcd $n1 $n2
    else
      let "n2 -= n1"
      gcd $n1 $n2
    fi
}

while [ true ]; do
  read n1 n2
  if [ -z $n1 ]; then
    echo "bye"
    exit
  else
  gcd $n1 $n2
  fi
done
  