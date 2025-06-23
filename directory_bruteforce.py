import requests
from datetime import datetime

def brute_force_directories(url):
    try:
        with open("directories.txt", "r") as wordlist:
            directories = wordlist.read().splitlines()
    except FileNotFoundError:
        print("❌ directories.txt file not found!")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = f"dir_brute_{url.replace('http://','').replace('https://','').replace('/','')}_{timestamp}.txt"

    found = []

    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"Directory Brute Force Report for {url}\n")
            f.write(f"Scan Time: {timestamp}\n\n")

            for dir in directories:
                full_url = f"{url.rstrip('/')}/{dir}"
                try:
                    response = requests.get(full_url)
                    if response.status_code == 200:
                        print(f"✅ Found: {full_url}")
                        f.write(f"✅ Found: {full_url}\n")
                        found.append(full_url)
                    elif response.status_code == 403:
                        print(f"🔒 Forbidden: {full_url}")
                        f.write(f"🔒 Forbidden: {full_url}\n")
                except requests.exceptions.RequestException:
                    continue

            if not found:
                print("\n❌ No accessible directories found.")
                f.write("\nNo accessible directories found.\n")

            f.write("\n--- End of Report ---\n")

        print(f"\n📝 Report saved as: {output_file}")

    except Exception as e:
        print(f"\n❗ Error: {e}")

    input("\n🔚 Press Enter to return to menu...")

if __name__ == "__main__":
    target_url = input("🌐 Enter target URL (e.g., http://example.com): ")
    brute_force_directories(target_url)
