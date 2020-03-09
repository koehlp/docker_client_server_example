import urllib.request

import os
server_ip = os.environ['server_ip']

contents = urllib.request.urlopen("http://{}:8888/".format(server_ip)).read()

print(contents)
