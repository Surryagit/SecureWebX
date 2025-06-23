import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_info_scan():
    os.system("python domain_info.py")

def run_xss_scan():
    os.system("python xss_scanner.py")

def run_subdomain_scan():
    os.system("python subdomain_finder.py")

def run_port_scan():
    os.system("python port_scanner.py")

def run_directory_brute_force():
    os.system("python directory_bruteforce.py")

def menu():
    while True:
        clear()
        print("🛡️  SECUREWEBX - CYBERSECURITY TOOLKIT 🛡️\n")
        print("1️⃣  Domain Info Scanner")
        print("2️⃣  XSS Vulnerability Scanner")
        print("3️⃣  Subdomain Finder")
        print("4️⃣  Port Scanner")
        print("5️⃣  Directory Brute-Forcer")
        print("6️⃣  Exit")

        choice = input("\n👉 Choose an option (1-6): ")

        if choice == "1":
            run_info_scan()
        elif choice == "2":
            run_xss_scan()
        elif choice == "3":
            run_subdomain_scan()
        elif choice == "4":
            run_port_scan()
        elif choice == "5":
            run_directory_brute_force()
        elif choice == "6":
            print("👋 Exiting SecureWebX. Stay safe, Surya!")
            break
        else:
            print("❌ Invalid choice!")
            input("Press Enter to try again...")

if __name__ == "__main__":
    menu()
