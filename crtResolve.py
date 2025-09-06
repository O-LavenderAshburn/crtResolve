#!/usr/bin/env python3
"""
THIS SCRIPT WAS MADE BY DREAD PIRATE WILLIAM.
"""
import socket
import sys
import time
import requests
import argparse
import json


from DomainResolver import resolve_subdomain
from CrtDownloader import download_csv_from_crtsh
from FormatParser import parse_csv_input, write_csv


crtTitle = r"""
             _____________                  ______            
_______________  /___  __ \____________________  /__   ______ 
_  ___/_  ___/  __/_  /_/ /  _ \_  ___/  __ \_  /__ | / /  _ \
/ /__ _  /   / /_ _  _, _//  __/(__  )/ /_/ /  / __ |/ //  __/
\___/ /_/    \__/ /_/ |_| \___//____/ \____//_/  _____/ \___/  
"""

orange = "\033[38;2;255;165;0m"
reset = "\033[0m"
green = "\033[38;2;0;255;0m"
red = "\033[38;2;255;0;0m"

def main():

    # Parse arguements and configure input filename and 
    parser = argparse.ArgumentParser(description="Subdomain resolver powered by crt.sh")
    parser.add_argument("input_file", nargs="?", help="CSV file to parse (optional if using --tld)")
    parser.add_argument("--tld", help="Fetch subdomains for a given TLD directly from crt.sh")
    parser.add_argument("--count",type=int,help="Collect specified amount")
    parser.add_argument("--out_format", help="Format of the output file: [csv,json]" , default="csv")
    parser.add_argument("--out_filename", nargs="?", default=f"resolved_subdomains", help="Output CSV filename")
    args = parser.parse_args()

   
    out_format = args.out_format
    output_file = args.out_filename 
    output_file = output_file + out_format
    

    print(f"{orange}{crtTitle}{reset}")

    # If --tld provided, download CSV from crt.sh
    if args.tld:
        input_file = download_csv_from_crtsh(args.tld)
    elif args.input_file:
        input_file = args.input_file
    else:
        print("[!] You must provide either an input file or --tld <TLD>")
        sys.exit(1)
    
    print(f"[*] Reading CSV file: {input_file}")
    all_subdomains = parse_csv_input(input_file)
    
    if not all_subdomains:
        print("[!] No subdomains found in input file")
        sys.exit(1)
    
    print(f"[*] Extracted {len(all_subdomains)} unique subdomains")
    
    results = []
    resolved_count = 0
    failed_count = 0

    print("[*] Resolving IP addresses...")    
    for i, subdomain in enumerate(sorted(all_subdomains), 1):
        try:

            print(f"[*] Processing {i}/{len(all_subdomains)}: {subdomain}")
            
            ip_addresses, error = resolve_subdomain(subdomain)
            
            if ip_addresses:
                ip_str = "[" + ", ".join(ip_addresses) + "]"
                results.append({
                    'subdomain': subdomain,
                    'ip_address': ip_str,
                    'status': 'resolved'
                })
                resolved_count += 1
                print(f"    -> {green}{ip_str} (resolved){reset}\n")
            else:
                failed_count += 1
                print(f"    -> {red}Failed: {error}{reset}\n")

            # early exit if count is set and reached
            if args.count and i >= args.count:
                print(f"[*] Reached count limit ({args.count})")
                break

            time.sleep(0.1)
        except KeyboardInterrupt:
            break
    
    if(out_format == "csv"):
        write_csv(results, output_file)
    elif(out_format == "json"):
        pass
    
    print(f"\n[*] Results saved to: {output_file}")
    print(f"[*] Summary:")
    print(f"    - Total subdomains: {len(all_subdomains)}")
    print(f"{green}    - Successfully resolved: {resolved_count}{reset}")
    print(f"{red}    - Failed to resolve: {failed_count}{reset}")
    print(f"{orange}{crtTitle}{reset}")
    print(f"{orange}Courtesy of Dread Pirate William{reset}")

if __name__ == "__main__":
    main()
