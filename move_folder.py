import os


serverlist = open('servers.txt', 'r')
servers = serverlist.readlines()

for server in servers:
    server = server.split()
    print(server[0])
    os.system(r'xcopy /G /H /S /E /Y "\\{}\c$\ArcSet10\syncthing\*.*" "\\{}\C$\Program Files\syncthing\*.*"'.format(server[0], server[0]))
    os.system(r'RMDIR /s/q "\\{}\C$\ArcSet10\syncthing"'.format(server[0]))

serverlist.close()

input('Press any key...')