import socket

COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 443, 445, 8080]

def scan_ports(ip):
    print(f"\n[+] Scanning ports on {ip}")
    open_ports = []

    for port in COMMON_PORTS:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            sock.close()

            if result == 0:
                print(f"    [+] Port {port} is OPEN")
                open_ports.append(port)

        except socket.error:
            pass

    return open_ports

if __name__ == "__main__":
    target = input("Enter target IP: ")
    open_ports = scan_ports(target)

    print("\n[+] Open ports found:")
    for port in open_ports:
        print(port)

