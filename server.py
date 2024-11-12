import os
import http.server
import socketserver

from http import HTTPStatus
import random

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        htmlhead = """
<html>
<head>
    <title>Lame PoC</title>
    <style type='text/css'>
        body    {background-color: powderblue;}
        p       {font-family: verdana;}
        .word   {color: green; font-weight: bold}
    </style>
</head>
"""
        ratingword = random.choice(['extremely', 'incredibly', 'profoundly', 'hilariously', 'implausibly', 'disturbingly', 'embarrassingly', 'ridiculously', 'astonishingly'])
        probability = 80.0 + random.random()*20.0
        htmlbody = f"""
<body>
    <p>Our model indicates that Simon is <span class='word'>{ratingword}</span> lame, with <span class='word'>{probability:.2f}</span>% confidence.</p>
    <p>
        <button type="button" onclick="location.reload();">Resample training data</button>
        <button type="button" onclick="location.reload();">Recalculate linear regression</button>
        <button type="button" onclick="location.reload();">Update model assumptions</button>
    </p>
</body>
</html>
"""
        page = htmlhead + htmlbody
        self.wfile.write(page.encode())


port = int(os.getenv('PORT', 8080))
print('Listening on port %s' % (port))
httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()
