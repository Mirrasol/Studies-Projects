`ssh login@address -p port_name` = enter server

`exit` = exit server

- server keys:

`~/.ssh/id_rsa`
`~/.ssh/id_rsa.pub` - at home

`~/.ssh/authorized_keys` - on server with public keys from .pub

`ssh-keygen` = create a key

`ssh-add` = add keys to system

- copy:

`scp -P port_name login@server_address:path1 path2` = copy from server(path1) to client

`scp -P port_name path1 login@server_address:path2` = copy from client(path1) to server

- server control:

`jobs` = list running programs

`fg number` / `bg number` = continue program with this number

`ps` = list current processes

`top` = follow all processes on this comp in real-time

! -u user_name = all processes of that user

! q = exit top

`kill pid` = finish process

`kill -9 pid` = kill process (use caution!)

- multithreading:

`free -g` = info about RAM

`nproc` = number of cores

`lscpu` = general info
