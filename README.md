# ResolveCert

# Certificate Transparency DNS Resolver

A Python script that extracts subdomains from Certificate Transparency (CT) logs exported from crt.sh and resolves their IP addresses using DNS lookups. This tool is designed for OSINT (Open Source Intelligence) gathering and reconnaissance activities.

# About

This script processes CSV data exported from crt.sh - a Certificate Transparency log search interface. It extracts subdomains from both the Common Name and Subject Alternative Names (SANs) fields in SSL/TLS certificates, then performs DNS resolution to find the IP addresses of active subdomains.

# Usage
`python3 crt_dns_resolver.py <input_csv> [output_csv]`
