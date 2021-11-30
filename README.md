# Developing a Simple Webserver
## AIM:
To Develop a webserver to display about top five programming languages.

## DESIGN STEPS:
### Step 1:
HTML content creation
### Step 2:

Design of webserver workflow
### Step 3:

Implementation using Python code
### Step 4:

Serving the HTML pages.
### Step 5:

Testing the webserver
## PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html
<head>
<title>Mywebsite</title>
</head>
<body>
<h1>Top five programming language :</h1>
<h2>Javascript</h2>
<h2>Java</h2>
<h2>Ruby</h2>
<h2>Python</h2>
<h2>C++</h2>
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
```

## OUTPUT:
## RESULT:
