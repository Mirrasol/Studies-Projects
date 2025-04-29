#!/usr/bin/bash

while true
do
  echo "enter your name:"
  read name
  if [[ -z $name ]]
  then
    echo "bye"
    break
  fi
  echo "enter your age:"
  read age
  if [[ $age -eq 0 ]]
  then
    echo "bye"
    break
  fi    
  if [[ age -le 16 ]]
  then
    echo "$name, your group is child"
  elif [[ age -gt 25 ]]
  then
    echo "$name, your group is adult"
  else
    echo "$name, your group is youth"
  fi
done