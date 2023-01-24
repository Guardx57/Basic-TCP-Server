#mengimport module socket yang akan digunakan
import socket

#menentukan ip dan port yang akan digunakan untuk komunikasi dengan server
#menggunakan ip (127.0.0.1) = local host dan port bebas disarankan 6000+ (tidak terpakai)
ip = "127.0.0.1"
port = 6060

#mengambil address family yang digunakan socket dengan socket.AF_INET (address family) Internet Protocol v5
#sedangkan socket.SOCK_STREAM bermakna socket yang digunakan adalah TCP
#diambil dari module socket
cl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#membuat koneksi dengan ip dan port ke dalam function cl.connect
cl.connect((ip, port))
pesan = ""

#membuat inputan nama sebagai pembeda antara server dan client (optional)



#mengambil inputan pesan untuk dikirim ke server dan mengambil output yang dihasilkan dari balasan server
#melakukan encode sebelum pengiriman ke server dan decode hasil kiriman balasan dari server
while True:
    pesan = input(f">: ")
    if pesan:
        pesan = clientname + pesan
        pesan = pesan.encode("utf-8")
        cl.send(pesan)
        pesan = ""

        svpesan = cl.recv(1024)
        svpesan = svpesan.decode("utf-8")
        print(f"[Server] {svpesan}")