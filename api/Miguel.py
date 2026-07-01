from http.server import BaseHTTPRequestHandler
import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1477413896418754732/bsZ5tOHoAWCf1WqhYhvnMeJHYQXTrGmb3Q0uDtlarnkza__vVrXsJxa6eFd3dyZlemqu"
URL = "http://ipinfo.io/ip"

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            response = requests.get(URL, timeout=10)
            requests.post(
                WEBHOOK_URL,
                data={"content": response.text}
            )

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")

        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode())
