- Shell = оболочка, интерпретатор комманд 

1) sh = de-facto standard
2) bash = upgraded sh

`which bash` = path to bash

`chmod +x path_to_file` = before executing

- состоит из инструкций (команд) и переменных
- можно писать комменты (тоже через решетку, кроме самой первой строчки с !)

`#!/bin/bash` = shebang

- переменная:

`<name>=<value>`

`$name` / `${name}` = чтение переменной

- аргументы:

`./script.sh arg1 arg2` = pass args to a script

`$1`  = arg1

`$2`  = arg2

`$0`  = scripts name

`$#`  = args amount

- ветвление:
1)

    if [[ condition ]]
    then
    some_actions_if_True
    fi

2)

    if [[ condition ]]
    then
    actions_c1_True
    elif [[ condition2]]
    then
    actions_c1_False_c2_True
    else
    actions_c1_c2 _both_False
    fi

3)

    case var in
    val1)
    some_actions_if_var==val1
    ;;
    val2)
    some_actions_if_var==val2
    ;;
    *)
    some_action_if_else
    esac

`-z line` = empty line/var etc

`-n line` = not an empty line

`line1 == line2` vs `var1 != var2`

1)for nums:

`-eq` = '==' for numbers (can use == for str)
`-ne` = '!=' for nums
`-lt` = '<'
`-le` = '<='
`-gt` = '>'
`-ge` = '>='

2)for files:

`-e path` = exists
`-f path` = that is a file
`-d path` = that is a dir
`-s path` = file's size > 0
`-x path` = file is executable

3)logics:

`!` = negative
`&&` = logical AND
`||` = logical OR

- циклы:

1)

    for var in some_values
    do
    some_actions
    done

+ break + continue

2)

    while [[ condition ]]
    do
    some_actions_for_True
    done

- арифметика:

`let "var = expression"` / `let var=1+1` => можно без кавычек, если нет пробелов

- внешние программы:

    var=\`bash_programm\`

`$?` = check returning code (0 = success)

`exit [code]` = exit and execute some code

    if `bash_code`
    then
      some_actions_if_0
    else
      some_actions_if_not_0
    fi

-  функции:

1)

    func_name () 
    {
        some_actions
        var_global=1
        local var_local=2
    }

2)

    func_name () { action1; action2; }
