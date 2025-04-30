`команда --опции аргументы` = общий вид комманд

Special Symbols:

    [.] = current dir
    [..] = parent dir
    [~] = home dir
    [*] = any number of symbols
    [?] = exactly one symbol

`man <command>` = 'manual' (Q to exit)

- terminal commands:

 `Ctrl + Shift + T` = new tab

 `Alt + number` = switch to the specific tab

 `Ctrl + Shift + W` = close current tab

- PC specifications:

`free -g` = info about RAM

`nproc` = number of cores

`lscpu` = general info

- general:

`exit` = close terminal

`clear` = clear terminal

`Ctrl+A` = to line start

`Ctrl+E` = to line end

`Ctrl+Z` = pause current process

! +fg = foreground

! +bg / +& = background


`pwd` = 'print working directory'

`ls` = 'list directory content'
`ls -l -h` = +list view, +size in KB/MB
`ls --sort=[sort_type] -l .` = with sorting (specified, ex. size, time)

`mkdir path_to_dir` / `mkdir ./{dir1,dir2,dir3}` = create dir
`mkdir -p path_to_dir` = +parents

`touch path_to_file` / `touch ~/{file1,file2}.txt` = create file

`cd path_to_file` = enter dir

`rm path_to_file` = remove file
`rm -r path_to_dir` = remove dir
`rm -rf path_to_dir` = remove dir -forced

`cp path_to_file_from path_to_file_where` = copy file
`cp -r path_to_dir_from path_to_dir_where`= copy dir

`mv dir1 dir2` = move dir/file


`chmod +x file` = make file executable


`cat file` = see files content

`less file` = open file for read

!    +q = exit

!   +/ = search

!    +g = to start

!    +G = to end

`nano file` = edit file
    +Ctrl+X = exit

- ins, outs and pipes:

`program >out.txt` = redirect stdout
`program 2>err.txt` = redirect stderr
`program <in.txt` = redirect stdin
`program &>file.txt` = redirect stdout + stderr

!    > = rewrite file

!    >> = add to file

`/dev/null` = redirect nowhere

`progr1 | progr2 | ... | progrN` = pipe: stdout1 into stdin2, stdout2 into stdin3 etc

- dowloads:

`wget` = standard prog for Internet downloads

- archiving:

`zip archive.zip file1 file2` = zip multiple files
`gzip file1` = zip 1 file and delete it, into file1.gz by default 

`tar -cvf arch.tar f1 f2` = zip multiple files without compressing

AND

`gzip arch.tar` = zip tar archive into arch.tar.gz, delete arch.tar after

! -v = info on screen (quiet without it)

ALSO

`tar -zcvf arch.tar f1 f2` = zip multiples with compress

`unzip archive.zip` = unzip zip
`gunzip archive.gz` = unzip gz and delete the .gz
`tar -xvf arch.tar` / `tar -zxvf arch.tar.gz` = unzip

ALSO `bzip2` / `bunzip2` (with .tar)

- searching:

`find dir1 -name "file1"` = find file1 in dir1 (or in current dir)

! - works with ~/./*/?

`find -iname filename` = without register


`grep "line1" file1` = find smth in file1

`grep -c "line1" file1` = count lines with line1 in file1

`grep -r "line1" dir1` = find line1 in dir

! --color = to color those line1

! -h = don't show the path to the file

`grep -E "regexp"` = find some regexps

- install apps:

`sudo apt-get install program` = install

`sudo apt-get remove program` = remove

`sudo apt-get update` = update package links

`sudo apt-get upgrade` = update installed packages

`sudo apt-get install --only-upgrade program` = update just the program

- permissions:

`users` = check all users

`groups` = check all groups

`ls -l path_to_file` = all permissions/groups for a file/dir

`chmod [ugoa][+-][rwx] path_to_file` = change permissions

`chown new_user:new_group path` = change ownership (can enter only user / only :new_group)

`sudo` = make smth from root

- misc. commands:

`wc -l path` = lines count
`wc -w path` = words count
`wc -c path` = bytes count

`diff [-q -r] path1 path2` = show diff between p1 and p2
`diff path1 path2 | less` = open diff in less editor
`-q` = don't show the diff itself, just tell if diff exists
`-r` = recursive for dirs

`du [--max-depth <depth> -h] path` = how nuch space is occupied on disk

`df [-h]` = how much is occupied in all disks, the entire system

`head [-n <lines amount>] path` = show lines from the start of the file
`tail [-n <lines amount>] path` = show lines from the end of the file

`sed 'instruction' file` / `cat filename | sed 'instruction'` = потоковый редактор (читает файл в stdin, обрабатывает по инструкции, пишет в stdout)
`-i` / `--in-name` = rewrite the file
