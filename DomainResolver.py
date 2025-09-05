"""
Resolve Ipv4 and Ipv6 addresses from domain names
"""

import socket

def resolve_subdomain(subdomain):
    try:
        if subdomain.startswith('*.'):
            clean_subdomain = subdomain[2:]
        else:
            clean_subdomain = subdomain

        if not clean_subdomain:
            return None, "Empty domain"

        addrinfo = socket.getaddrinfo(clean_subdomain, None)

        addresses = set()
        for result in addrinfo:
            family, _, _, _, sockaddr = result
            if family in (socket.AF_INET, socket.AF_INET6):
                addresses.add(sockaddr[0])

        return sorted(addresses), None

    except socket.gaierror:
        return None, "DNS resolution failed"
    except Exception as e:
        return None, f"Error: {str(e)}"

