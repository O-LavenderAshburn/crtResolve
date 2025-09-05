"""
Handle CRT operations
"""

import sys
import requests
import datetime
from datetime import datetime

def download_csv_from_crtsh(tld):
    """
    Download a CSV from crt.sh for the given TLD
    """

    
    url = f"https://crt.sh/csv?q={tld}&exclude=expired&group=none"

    print(f"[*] Downloading CSV from: {url}")
    response = requests.get(url, timeout=30)

    if response.status_code == 200:
        filename = f"{datetime.now().strftime('%Y-%m-%d')}_{tld}.csv"
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"[*] CSV downloaded successfully as {filename}")
        return filename
    else:
        print(f"[!] Failed to fetch data from crt.sh (status {response.status_code})")
        sys.exit(1)