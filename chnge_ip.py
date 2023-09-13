serverlist = open('servers.txt', 'r')
servers = serverlist.readlines()

for server in servers:
    server = server.split()
    print(server[0])
    fin = open(r"\\{}\c$\Users\Администратор\AppData\Local\Syncthing\config.xml".format(server[0]), "rt")
    data = fin.read()
    data = data.replace('127.0.0.1', server[0])
    fin.close()
    fin = open(r"\\{}\c$\Users\Администратор\AppData\Local\Syncthing\config.xml".format(server[0]), "wt")
    fin.write(data)
    fin.close()
serverlist.close()

input('Press any key...')