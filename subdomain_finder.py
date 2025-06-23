import requests
from datetime import datetime

def find_subdomains(domain):
    subdomains = [
        "www", "mail", "blog", "shop", "api", "admin", "support", "dev", "test", "forum"
    ]

    print(f"\n🔍 Scanning for subdomains...\n")
    found = []

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    clean_domain = domain.replace("https://", "").replace("http://", "").replace("/", "")
    output_file = f"subdomain_report_{clean_domain}_{timestamp}.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"Subdomain Scan Report for {domain}\n")
        f.write(f"Scan Time: {timestamp}\n\n")

        for sub in subdomains:
            url = f"http://{sub}.{domain}"
            try:
                response = requests.get(url)
                if response.status_code < 400:
                    print(f"✅ Found: {url}")
                    f.write(f"✅ Found: {url}\n")
                    found.append(url)
            except requests.RequestException:
                pass

        f.write(f"\n🎯 Total found: {len(found)}\n")
        f.write("\n--- End of Report ---\n")

    print(f"\n🎯 Total found: {len(found)}")
    print(f"📝 Report saved as: {output_file}")
    input("\n🔚 Press Enter to return to menu...")

if __name__ == "__main__":
    domain = input("🌐 Enter the main domain (e.g., example.com): ")
    find_subdomains(domain)
