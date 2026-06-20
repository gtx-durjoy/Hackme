import urllib.request
from concurrent.futures import ThreadPoolExecutor

def check_dir(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=3) as resp:
            if resp.getcode() < 500:
                print(f"[+] {url} ({resp.getcode()})")
    except:
        pass