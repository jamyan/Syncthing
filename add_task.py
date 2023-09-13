import os


serverlist = open('servers.txt', 'r')
servers = serverlist.readlines()

for server in servers:
    server = server.split()
    print(server[0])
    os.system(r'SCHTASKS /Create /S {} /XML "D:\tmp\Setv10backup_server_BD.xml" /RU {}\Администратор /RP Ctrnjhufp@ /TN "Backup Set10"'.format(server[0], server[1]))
    os.system(r'SCHTASKS /RUN /S {} /TN "Backup Set10"'.format(server[0]))

serverlist.close()

input('Press any key...')