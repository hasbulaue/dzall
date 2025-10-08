import threading

counter = 0

def increment():
    global counter
    for _ in range(100000):
        counter += 1

threads = []
for _ in range(5):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Без Lock: {counter}")  

counter = 0
lock = threading.Lock()

def increment_safe():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

threads = []
for _ in range(5):
    t = threading.Thread(target=increment_safe)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"С Lock: {counter}") 