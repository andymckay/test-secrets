from http.server import BaseHTTPRequestHandler
import os

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        message = ""
        keys = sorted(os.environ.keys())
        for key in keys:
            message += key + "=" + os.getenv(key) + "\n"
        self.wfile.write(message.encode())
        return
