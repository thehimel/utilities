#!/usr/bin/env python3
"""
Domain checker script using python-whois.
Checks if a domain is registered or available.
"""

import sys
import whois


def is_domain_registered(domain: str) -> bool:
    """
    Check if a domain is registered.
    
    Args:
        domain: The domain name to check (e.g., 'example.com')
        
    Returns:
        True if domain is registered, False if available/not registered
    """
    try:
        # Remove protocol if present
        domain = domain.strip().lower()
        if domain.startswith('http://') or domain.startswith('https://'):
            domain = domain.split('//')[1].split('/')[0]
        if domain.startswith('www.'):
            domain = domain[4:]
        
        # Query whois
        w = whois.whois(domain)
        
        # Check if domain has registration info
        # If domain is not registered, whois might return None or empty values
        if w is None:
            return False
        
        # Check if domain_name exists and is not empty
        if hasattr(w, 'domain_name'):
            domain_name = w.domain_name
            if domain_name is None:
                return False
            # Sometimes it's a list
            if isinstance(domain_name, list):
                return len(domain_name) > 0 and domain_name[0] is not None
            return domain_name is not None and domain_name != ''
        
        # Check expiration date as alternative indicator
        if hasattr(w, 'expiration_date'):
            exp_date = w.expiration_date
            if exp_date is not None:
                return True
        
        # If we have any meaningful data, consider it registered
        # Check for registrar
        if hasattr(w, 'registrar') and w.registrar:
            return True
        
        # Default to False if no clear registration info
        return False
        
    except Exception as e:
        # Domain not found/not registered or other errors
        # python-whois may raise various exceptions for unavailable domains
        # Most commonly: whois.parser.PywhoisError (older versions) or 
        # general exceptions when domain is not registered
        # For simplicity, treat any exception as domain not registered
        return False


def main():
    """Main function to run from command line."""
    if len(sys.argv) < 2:
        print("Usage: python check_domain.py <domain>", file=sys.stderr)
        sys.exit(1)
    
    domain = sys.argv[1]
    is_registered = is_domain_registered(domain)
    
    if is_registered:
        print(f"{domain}: not available")
        sys.exit(0)
    else:
        print(f"{domain}: available")
        sys.exit(0)


if __name__ == "__main__":
    main()

