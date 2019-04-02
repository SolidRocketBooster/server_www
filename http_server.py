import http.server 
import socketserver
import yaml
import os

with open('config.yml', 'r') as conf:
    config = conf.read()

os.chdir(yaml.load(config).get('PATH'))
port = yaml.load(config).get('PORT')
handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", port), handler) as httpd:
    print("serving at port", port)
    httpd.serve_forever()

