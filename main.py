import socket, time, sys

def main() -> None:
    port, file = sys.argv[1] or "80", sys.argv[2] or "index.html"

    with open(file, "r") as f:
        page = f.read()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("", int(port)))
    sock.listen(1)

    while True:
        client = sock.accept()[0]
        if not client:
            break
        else:
            client.send("HTTP/1.1 200 OK\r\n".encode("utf-8"))
            client.send("Server: HTTPython\r\n".encode("utf-8"))
            client.send("Content-Type: text/html\r\n".encode("utf-8"))
            client.send(f"Content-Length: {len(page)}\r\n".encode("utf-8"))
            client.send("\r\n".encode("utf-8"))
            client.send(page.encode("utf-8"))
            client.close()

        time.sleep(0.1)

if __name__ == "__main__":
    main()