#!/usr/bin/env python3
"""
Very simple HTTP server in python for logging requests
Usage::
    ./server.py [<port>]
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging


class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        result = "GET request,\n\nPath: {path}\nHeaders:\n{headers}\n" \
            .format(path=str(self.path),headers=str(self.headers))

        logging.info(result)

        self._set_response()
        self.wfile.write(result.encode('utf-8'))

    def do_POST(self):
        # <--- Gets the size of data
        content_length = int(self.headers['Content-Length'])
        # <--- Gets the data itself
        post_data = self.rfile.read(content_length)

        result = "POST request,\n\nPath: {path}\nHeaders:\n{headers}\nBody:\n{body}\n" \
            .format(path=str(self.path),headers=str(self.headers),body=post_data.decode('utf-8'))

        logging.info(result)

        self._set_response()
        self.wfile.write(result.encode('utf-8'))
    
    def do_HEAD(self):
        result = "HEAD request,\n\nPath: {path}\nHeaders:\n{headers}\n" \
            .format(path=str(self.path),headers=str(self.headers))

        logging.info(result)

        self._set_response()
        self.wfile.write(result.encode('utf-8'))



def run(server_class=HTTPServer, handler_class=S, port=8000):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
