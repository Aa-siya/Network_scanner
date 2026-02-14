import subprocess
import platform



def ping_host(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", ip]
    response = subprocess.call(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
     )
    return response == 0



def scan_network(network_prefix):
    print("\n[+] Scanning for live hosts...\n")
    live_hosts = []

    for i in range(1, 255):
        ip = f"{network_prefix}.{i}"
        print(f"[*] Pinging {ip}...")
        if ping_host(ip):
            print(f"[+] Host is alive: {ip}")
            live_hosts.append(ip)

    return live_hosts



if __name__ == "__main__":
    network = input("Enter network prefix (e.g. 192.168.1): ")
    live_hosts = scan_network(network)

    print("\n[+] Live hosts found:")
    for host in live_hosts:
        print(host)
        
        







# if __name__ == "__main__":
#     test_ip = "8.8.8.8"
#     if ping_host(test_ip):
#         print(f"{test_ip} is alive!")
#     else:
#         print(f"{test_ip} is not reachable.")
