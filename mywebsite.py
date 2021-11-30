from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html
<head>
<title>Mywebsite</title>
</head>
<body>
<h1>Top five programming language :</h1>
<h1>Javascript</h1>
<h1>Java</h1>
<h1>Ruby</h1>
<h1>Python</h1>
<h1>C++</h1>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8080)
httpd = HTTPServer(server_address,myhandler)
print("my server is running...")
httpd.serve_forever()

