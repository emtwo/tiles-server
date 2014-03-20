import BaseHTTPServer

HOST_NAME = '127.0.0.1'
PORT_NUMBER = 80
TILES_FILE = "directoryTiles.json"

class JSONHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_HEAD(s):
		s.send_response(200)
		s.send_header("Content-type", "application/json")
		s.end_headers()

	def do_GET(s):
		s.wfile.write(open(TILES_FILE).read())

if __name__ == '__main__':
	server_class = BaseHTTPServer.HTTPServer;
	httpd = server_class((HOST_NAME, PORT_NUMBER), JSONHandler)

	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass

	httpd.server_close()