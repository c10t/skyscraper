#!/usr/bin/env python
# -*- coding: utf-8 -*-

import http.server
import socketserver

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler


def main():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()

if __name__ == '__main__':
    main()
