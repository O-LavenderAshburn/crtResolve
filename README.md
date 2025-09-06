```
             _____________                  ______            
_______________  /___  __ \____________________  /__   ______ 
_  ___/_  ___/  __/_  /_/ /  _ \_  ___/  __ \_  /__ | / /  _ \
/ /__ _  /   / /_ _  _, _//  __/(__  )/ /_/ /  / __ |/ //  __/
\___/ /_/    \__/ /_/ |_| \___//____/ \____//_/  _____/ \___/ 
                                                              
```

A Python tool for discovering and resolving subdomains using crt.sh certificate transparency logs.


- Fetch subdomains directly from crt.sh for a given domain/TLD.
- Parse existing CSV files of subdomains.
- Resolve subdomains to IP addresses.

Basic Usage
- `python3 crtResolve <input_file.csv>` — CSV file of subdomains (optional if using --tld)

 Options
- `--tld <domain> [output-file]` — Fetch subdomains for a given domain/TLD directly from crt.sh`
- ` --count <N> `— Stop after resolving N subdomains
- `--out_filename <name>` — Base name for output file (default: resolved_subdomains)`
