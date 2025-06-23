import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from datetime import datetime

def get_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

def form_details(form):
    details = {}
    action = form.attrs.get("action", "").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            data[input["name"]] = value
    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

def scan_xss(url):
    forms = get_forms(url)
    print(f"\n🔍 Found {len(forms)} forms on {url}\n")

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = f"xss_report_{url.replace('https://','').replace('http://','').replace('/', '')}_{timestamp}.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"XSS Scan Report for: {url}\n")
        f.write(f"Scan Time: {timestamp}\n")
        f.write(f"Total Forms Found: {len(forms)}\n\n")

        for i, form in enumerate(forms, start=1):
            details = form_details(form)
            f.write(f"📄 Form #{i} details:\n{details}\n")
            print(f"📄 Form #{i} details:\n{details}")

            is_vulnerable = False
            response = submit_form(details, url, "<script>alert('XSS')</script>")
            if "<script>alert('XSS')</script>" in response.text:
                print("⚠️ XSS vulnerability detected!\n")
                f.write("⚠️ XSS vulnerability detected!\n\n")
                is_vulnerable = True
            else:
                print("✅ Safe from XSS.\n")
                f.write("✅ Safe from XSS.\n\n")

        f.write("--- End of Report ---\n")

    print(f"📝 Report saved as: {output_file}")
    input("🔚 Press Enter to return to menu...")

if __name__ == "__main__":
    url = input("Enter URL to scan for forms and XSS: ")
    scan_xss(url)
