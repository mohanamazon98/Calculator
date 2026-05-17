from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

# This is our basic HTML interface
html_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Jenkins Python Calculator</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 50px; }
        .calc-box { border: 1px solid #ccc; padding: 20px; width: 300px; }
        .brand-header { color: blue; } 
    </style>
</head>
<body>
    <h2 class="brand-header">calculator built by MG</h2>
    
    <div class="calc-box">
        <h2>Web Calculator</h2>
        <form method="POST">
            <input type="number" name="num1" placeholder="First Number" required><br><br>
            
            <select name="operation">
                <option value="add">Add (+)</option>
                <option value="subtract">Subtract (-)</option>
                <option value="multiply">Multiply (*)</option>
                <option value="divide">Divide (/)</option>
            </select><br><br>
            
            <input type="number" name="num2" placeholder="Second Number" required><br><br>
            
            <button type="submit">Calculate</button>
        </form>
        <h3>Result: {result}</h3>
    </div>
</body>
</html>
"""

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Fixed: Using replace() so CSS braces don't break the server
        self.wfile.write(html_page.replace('{result}', "").encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        parsed_data = parse_qs(post_data)

        try:
            num1 = float(parsed_data.get('num1', [0])[0])
            num2 = float(parsed_data.get('num2', [0])[0])
            operation = parsed_data.get('operation', [''])[0]

            if operation == 'add': result = num1 + num2
            elif operation == 'subtract': result = num1 - num2
            elif operation == 'multiply': result = num1 * num2
            elif operation == 'divide': result = num1 / num2 if num2 != 0 else "Error: Divide by zero"
            else: result = "Invalid Operation"
        except Exception:
            result = "Error: Invalid Input"

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Fixed: Using replace() here as well
        self.wfile.write(html_page.replace('{result}', str(result)).encode('utf-8'))

if __name__ == "__main__":
    server_address = ('', 5000)
    httpd = HTTPServer(server_address, RequestHandler)
    print("Starting web server on port 5000...")
    httpd.serve_forever()