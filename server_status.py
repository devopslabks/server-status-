
from http.server import BaseHTTPRequestHandler, HTTPServer

servers = ["web1", "web2", "web3"]

class ServerStatus(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        message = ""
        for server in servers:
            message += server + " is Running\n"

        self.wfile.write(message.encode())

server = HTTPServer(("0.0.0.0", 8080), ServerStatus)

print("Server Status application running on port 8080")

server.serve_forever()


