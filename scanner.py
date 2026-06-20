#!/usr/bin/env python3
import sys
import argparse
from colorama import init, Fore
init()

from utils.anonymizer import anonymize
from utils.helpers import brute_dirs, check_sqli, scan_xss

def main():
    parser = argparse.ArgumentParser(description="Potato Scanner")
    parser.add_argument("-u", "--url", required=True, help="Target URL")
    parser.add_argument("-t", "--threads", type=int, default=20, help="Threads (default 20)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    args = parser.parse_args()
    
    print(f"{Fore.GREEN}[+] Target: {args.url}")
    print(f"{Fore.YELLOW}[*] Scanning directories...")
    brute_dirs(args.url, args.threads)
    
    print(f"{Fore.YELLOW}[*] Checking SQLi...")
    check_sqli(args.url)
    
    print(f"{Fore.YELLOW}[*] Scanning XSS...")
    scan_xss(args.url)
    
    print(f"{Fore.GREEN}[✓] Scan complete.")

if __name__ == "__main__":
    main()
