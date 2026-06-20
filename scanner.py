#!/usr/bin/env python3
import sys
import argparse
from colorama import init, Fore
init()

def main():
    parser = argparse.ArgumentParser(description="Potato Scanner")
    parser.add_argument("--sqli", action="store_true", help="Only SQLi scan")
    parser.add_argument("--xss", action="store_true", help="Only XSS scan")
    parser.add_argument("--full", action="store_true", help="Full scan")
    args = parser.parse_args()
    
    print(f"{Fore.GREEN}[+] Starting Potato Scanner...")
    # এখানে তোমার আগের কোড বসবে
    print(f"{Fore.YELLOW}[*] Scanning... (Placeholder)")

if __name__ == "__main__":
    main()