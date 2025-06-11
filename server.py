import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime, timedelta
import urllib
from models import Log


class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        if parsed_path.path == "/":
            self.serve_html()
        elif parsed_path.path == "/data":
            self.serve_data()
        else:
            self.send_error(404, "Not Found")

    def serve_html(self):
        try:
            with open("index.html", "r", encoding="utf-8") as f:
                html = f.read()
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html.encode("utf-8"))
        except FileNotFoundError:
            self.send_error(404, "Arquivo index.html não encontrado")

    def serve_data(self):
        agora = datetime.now()
        cinco_minutos_atras = agora - timedelta(minutes=5)

        query = (
            Log.select()
            .where(Log.dt_registro.between(cinco_minutos_atras, agora))
            .order_by(Log.dt_registro)
        )

        registros = []
        for log in query:
            registros.append(
                {
                    "device_id": log.device_id,
                    "temperatura": log.temperatura,
                    "umidade": log.umidade,
                    "dt_registro": log.dt_registro.strftime("%Y-%m-%d %H:%M:%S"),
                }
            )

        json_data = json.dumps(registros)

        self.send_response(200)
        self.send_header("Content-type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(json_data.encode("utf-8"))


if __name__ == "__main__":
    port = 8007
    print(f"Servidor rodando em http://localhost:{port}/")
    server = HTTPServer(("0.0.0.0", port), RequestHandler)
    server.serve_forever()
