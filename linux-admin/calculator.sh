#!usr/bin/bash

while [[ True ]]; do
  read n1 symbol n2
  if [[ $n1 == "exit" ]]; then
    echo "bye"
    exit
  elif [[ "$n1" =~ "^[0-9]+$" && "$n2" =~ "^[0-9]+$" ]]; then
    echo "error"
  else
    case $symbol in
    "+") let "result = n1 + n2";;
    "+") let "result = n1 - n2";;
    "/") let "result = n1 / n2";;
    "*") let "result = n1 * n2";;
    "%") let "result = n1 % n2";;
    "**") let "result = n1 ** n2";;
    *) echo "error" ; break ;;
    esac
    echo "$result"
  fi
done