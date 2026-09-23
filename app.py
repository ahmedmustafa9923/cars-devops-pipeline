import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

class DevOpsApp(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        
        # This automatically maps the folders and logs the structure live
        output = "==================================================\n"
        output += "   DEV OPS AUTOMATED CARS ENGINE ONLINE ENGINE    \n"
        output += "==================================================\n\n"
        
        for root, dirs, files in sorted(os.walk(".")):
            # Skip hidden git folders
            if ".git" in root:
                continue
                
            level = root.replace('.', '').count(os.sep)
            indent = ' ' * 4 * (level)
            output += f"{indent}[+] {os.path.basename(root)}/\n"
            subindent = ' ' * 4 * (level + 1)
            for f in sorted(files):
                if f != "app.py" and f != "Dockerfile":
                    output += f"{subindent}└── [File] {f}\n"
                    
        self.wfile.write(output.encode())

print("DevOps App serving on port 8080...")
HTTPServer(('0.0.0.0', 8080), DevOpsApp).serve_forever()
