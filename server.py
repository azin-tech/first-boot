#!/usr/bin/env python3
import http.server
import html
import os

VM_NAME = os.environ.get("BOXD_VM_NAME", "Snake Game")

# Read and template the HTML once at startup
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")) as f:
    PAGE = f.read().replace("{{VM_NAME}}", html.escape(VM_NAME))

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(PAGE.encode())
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        print(f"[{self.log_date_time_string()}] {args[0]}")

if __name__ == "__main__":
    server = http.server.HTTPServer(("0.0.0.0", 3000), Handler)
    print(f"Snake Game running on http://0.0.0.0:3000 (VM: {VM_NAME})")
    server.serve_forever()
