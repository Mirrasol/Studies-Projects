`vim` = enter
`vim file1` = open
`vim file1 file2 etc` = open multi

`:q` = exit

`:help` = help :)

! vimtutor

- insert mode:

`Esc` / `Ctrl + c` = exit to normal mode

- moving:

`h, j, l, k, arrows`

`w/W` = to word's start

`e/E` = to word's end

`b/B` = to previous's start

`0, ^, $` = to line's start, to first non-space symbol, to line's end

`gg` = file's start

`G` = file's end

`:number + Enter` = to line #number

`Ctrl + D` / `Ctrl + U` = down/up the screen

- deleting:

`x` = symbol on cursor

`X` = symbol before cursor

`d[amount][type]` = multiples (ex. de = to word's end, d$ = to line's end, d5 = 5 words)

`dd` / `d[amount]d` = delete a line / multiple lines

- creation:

`i` = insertion mode

`a` = move cursor to the right and enter insertion mode

`I` = `^i`

`A` = `$a`

`o` / `O` = insert a new line at the end / start and edit it

- copying:

`y[amount][type]`

`yy` = copy the line

- inserting:

`p` / `P` = insert before / after

- searching:

`/[text]` = search text forward

`?[text]` = search text backwards

`n` / `N` = previous / next find

- replacing:

`:%s/[what looking for]/[new]/[flags, optional]`

`g` = multiple replacements
`c` = confirmation

- usefuls:

`u` = abort (Ctrl+Z)

`Ctrl + r` = abort abort (Ctrl+Y)

- saving:

`:w` = save

`:wq` = save and exit

`:q!` = don't save and exit

`:w [file]` = save into file
