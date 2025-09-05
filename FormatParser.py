"""
Handle formatting for inputs and outpus. Currently supports 
CSV
"""

import csv

def parse_csv_input(filename):
    subdomains = set()
    
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            sample = csvfile.read(1024)
            csvfile.seek(0)
            sniffer = csv.Sniffer()
            has_header = sniffer.has_header(sample)
            
            reader = csv.reader(csvfile)
            
            if has_header:
                next(reader)
            
            for row in reader:
                if len(row) >= 5:
                    common_name = row[4].strip().strip('"')
                    if common_name:
                        subdomains.add(common_name.lower())
                    
                    if len(row) >= 6:
                        matching_identities = row[5].strip().strip('"')
                        if matching_identities:
                            sans = matching_identities.replace('\n', ',').split(',')
                            for san in sans:
                                san = san.strip().lower()
                                if san:
                                    subdomains.add(san)
    
    except FileNotFoundError:
        print(f"[!] File not found: {filename}")
        return set()
    except Exception as e:
        print(f"[!] Error reading CSV file: {e}")
        return set()
    
    return subdomains


def write_csv(results, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['subdomain', 'ip_address', 'status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(result)