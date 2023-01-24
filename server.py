#mengimport module socket yang akan digunakan
import socket

#menentukan ip dan port yang akan digunakan untuk komunikasi dengan client
#menggunakan ip (127.0.0.1) = local host dan port bebas disarankan 6000+ (tidak terpakai)
ip = "127.0.0.1"
port = 6060

#mengambil address family yang digunakan socket dengan socket.AF_INET (address family) Internet Protocol v5
#sedangkan socket.SOCK_STREAM bermakna socket yang digunakan adalah TCP
sv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sv.bind digunakan untuk membuat server socket untuk koneksi dengan client tetapi hanya terlihat pada mesin yang sama
sv.bind((ip, port))
#server dapat berkomunikasi sampai dengan 5 client
sv.listen(5)

#mengkonfirmasi bahwa client telah terkoneksi dan menampilkan ke layar
client, addr = sv.accept()
print(f"Koneksi dari {addr[0]}:{addr[1]} telah tersambung.")

#mengambil mengambil output yang dihasilkan dari client dan inputan pesan untuk dikirim sebagai balasan ke client
#melakukan decode hasil kiriman dari client dan encode sebelum pengiriman ke client
while True:
    clpesan = client.recv(1024)
    clpesan = clpesan.decode("utf-8")
    print(f"{clpesan}")
    msg = input(">: ")
    msg = msg.encode("utf-8")
    client.send(msg)

