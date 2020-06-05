#!/usr/bin/python3

import http.server
import socketserver

def main():

    PORT = 9021

    Handler = http.server.SimpleHTTPRequestHandler

    httpd = socketserver.TCPServer(("", PORT), Handler)

    print(("serving at port", PORT))
    httpd.serve_forever()

if __name__ == "__main__":
    main()

