import socket
from datetime import datetime

common_ports = {
    21: 'FTP',
    22: 'SSH',
    23: 'Telnet',
    25: 'SMTP',
    53: 'DNS',
    80: 'HTTP',
    110: 'POP3',
    143: 'IMAP',
    443: 'HTTPS',
    3306: 'MySQL',
    8080: 'HTTP-Alt'
}

def scan_ports(target, ports=common_ports):
    print(f"\n🔍 Scanning {target}...\n")
    open_ports = []
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = f"port_scan_{target}_{timestamp}.txt"

    try:
       with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"Port Scan Report for {target}\n")
            f.write(f"Scan Time: {timestamp}\n\n")

            for port, service in ports.items():
                print(f"⏳ Checking port {port} ({service})...", end=" ")
                sock = socket.socket()
                sock.settimeout(0.8)
                result = sock.connect_ex((target, port))
                if result == 0:
                    print("✅ OPEN")
                    f.write(f"✅ Port {port} ({service}) is OPEN\n")
                    open_ports.append((port, service))
                else:
                    print("❌ CLOSED")
                sock.close()

            if not open_ports:
                print("\n❌ No common ports are open.")
                f.write("No common ports are open.\n")
            else:
                print(f"\n🎯 Total Open Ports: {len(open_ports)}")
                f.write(f"\nTotal Open Ports: {len(open_ports)}\n")
                for port, service in open_ports:
                    print(f"🔓 {port} - {service}")
                    f.write(f"🔓 {port} - {service}\n")

            f.write("\n--- End of Report ---\n")
            print(f"\n📝 Report saved as: {output_file}")

    except Exception as e:
        print(f"\n❗ Error: {e}")

    input("\n🔚 Press Enter to return to menu...")

if __name__ == "__main__":
    target = input("🌐 Enter target domain or IP: ")
    scan_ports(target)
