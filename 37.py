import socket
import threading
import json
from collections import defaultdict
import time

class QueryStatsClient:
    def __init__(self, host='localhost', port=9090):
        self.host = host
        self.port = port
        self.query_counts = defaultdict(int)
        self.running = False
        self.sock = None
        
    def start(self):
        self.running = True
        self.connect_to_server()
        threading.Thread(target=self.send_stats_periodically, daemon=True).start()
        
    def connect_to_server(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sock.connect((self.host, self.port))
        except ConnectionRefusedError:
            print("Server not available")
            
    def record_query(self, query):
        self.query_counts[query] += 1
        
    def send_stats_periodically(self):
        while self.running:
            time.sleep(10)
            if self.query_counts and self.sock:
                try:
                    stats = dict(self.query_counts)
                    data = json.dumps(stats).encode('utf-8')
                    self.sock.sendall(data)
                    self.query_counts.clear()
                except:
                    self.connect_to_server()
                    
    def stop(self):
        self.running = False
        if self.sock:
            self.sock.close()

class QueryStatsServer:
    def __init__(self, host='localhost', port=9090):
        self.host = host
        self.port = port
        self.clients = []
        self.running = False
        
    def start(self):
        self.running = True
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)
        
        print(f"Server listening on {self.host}:{self.port}")
        
        while self.running:
            try:
                client_socket, addr = server_socket.accept()
                print(f"Client connected: {addr}")
                threading.Thread(target=self.handle_client, args=(client_socket,), daemon=True).start()
            except:
                break
                
    def handle_client(self, client_socket):
        while self.running:
            try:
                data = client_socket.recv(4096)
                if not data:
                    break
                    
                stats = json.loads(data.decode('utf-8'))
                print("\n=== Query Statistics ===")
                for query, count in stats.items():
                    print(f"{query}: {count} requests")
                print("=======================\n")
                
            except:
                break
                
        client_socket.close()
        
    def stop(self):
        self.running = False

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == 'server':
        server = QueryStatsServer()
        try:
            server.start()
        except KeyboardInterrupt:
            server.stop()
    else:
        client = QueryStatsClient()
        client.start()
        
        try:
            while True:
                query = input("Enter user query (or 'quit' to exit): ")
                if query.lower() == 'quit':
                    break
                client.record_query(query)
        except KeyboardInterrupt:
            pass
        finally:
            client.stop()