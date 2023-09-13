import os


serverlist = open('servers.txt', 'r')
servers = serverlist.readlines()

for server in servers:
    server = server.split()
    print(server[0])
    os.system(r'D:\distr\PSTools\PsExec64.exe \\{} "C:\Program Files\syncthing\nssm.exe" install Syncthing "C:\Program Files\syncthing\syncthing.exe"'.format(server[0]))
    os.system(r'D:\distr\PSTools\PsExec64.exe \\{} "C:\Program Files\syncthing\nssm.exe" set Syncthing Description "Sync&Share"'.format(server[0]))
    os.system(r'D:\distr\PSTools\PsExec64.exe \\{} "C:\Program Files\syncthing\nssm.exe" set Syncthing ObjectName .\Администратор Ctrnjhufp@'.format(server[0]))
    os.system(r'sc \\{} start Syncthing'.format(server[0]))
    os.system(r'ping 172.16.1.2')
    os.system(r'sc \\{} stop Syncthing'.format(server[0]))

serverlist.close()

input('Press any key...')