from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os

# Load environment variables
PORT = int(os.getenv("PORT", 5000))
ENV = os.getenv("ENV", "development")

# Sample mock Microsoft 365–style data
mock_data = {
    "users": [
        {"name": "Alice", "email": "alice@company.com", "tasks_completed": 3},
        {"name": "Bob", "email": "bob@company.com", "tasks_completed": 5},
        {"name": "Charlie", "email": "charlie@company.com", "tasks_completed": 2}
    ],
    "documents": [
        {"name": "Report1.docx", "owner": "Alice"},
        {"name": "Financials.xlsx", "owner": "Bob"}
    ],
    "progress": "Initial backend setup running in " + ENV
}

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(mock_data).encode())
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(f"Hello from AutoAudit {ENV} backend!".encode())

HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
