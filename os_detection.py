import subprocess
import platform
import re

def detect_os(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", ip]

    try:
        output = subprocess.check_output(command).decode()

        ttl_match = re.search(r"ttl=(\d+)", output, re.IGNORECASE)
        if ttl_match:
            ttl = int(ttl_match.group(1))

            if ttl <= 64:
                return "Linux / Unix"
            elif ttl <= 128:
                return "Windows"
            else:
                return "Unknown"

    except:
        return "Unknown"
    
    
    
    if __name__ == "__main__":
        target = input("Enter target IP: ")
        os_name = detect_os(target)
        print(f"Detected OS: {os_name}")


