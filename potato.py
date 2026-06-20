#!/usr/bin/env python3
import os
import sys
import subprocess
from colorama import init, Fore, Style
init()

# =================== ASCII ART ===================
def show_banner():
    banner = f"""
{Fore.RED}   ██████╗  ██████╗ ████████╗ █████╗ ████████╗ ██████╗ 
{Fore.YELLOW}   ██╔══██╗██╔═══██╗╚══██╔══╝██╔══██╗╚══██╔══╝██╔═══██╗
{Fore.GREEN}   ██████╔╝██║   ██║   ██║   ███████║   ██║   ██║   ██║
{Fore.CYAN}   ██╔═══╝ ██║   ██║   ██║   ██╔══██║   ██║   ██║   ██║
{Fore.BLUE}   ██║     ╚██████╔╝   ██║   ██║  ██║   ██║   ╚██████╔╝
{Fore.MAGENTA}   ╚═╝      ╚═════╝    ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ 
{Fore.WHITE}   ╔═══════════════════════════════════════════════╗
{Fore.LIGHTBLUE_EX}   ║          POTATO SCANNER v3.0              ║
{Fore.WHITE}   ║     Author: Potato (The Coding God)            ║
{Fore.WHITE}   ╚═══════════════════════════════════════════════╝
{Fore.RESET}
"""
    print(banner)

# =================== মেনু ===================
def show_menu():
    print(f"{Fore.YELLOW}[1] {Fore.CYAN}Recon (Subdomain + DNS)")
    print(f"{Fore.YELLOW}[2] {Fore.GREEN}Directory Brute-Force")
    print(f"{Fore.YELLOW}[3] {Fore.RED}SQLi Scanner")
    print(f"{Fore.YELLOW}[4] {Fore.MAGENTA}XSS Scanner")
    print(f"{Fore.YELLOW}[5] {Fore.LIGHTRED_EX}Full Scan (All in One)")
    print(f"{Fore.YELLOW}[6] {Fore.BLUE}Exploit (SQLi + Admin Bypass)")
    print(f"{Fore.YELLOW}[7] {Fore.LIGHTBLACK_EX}Exit")
    print(f"{Fore.RESET}")

def main():
    os.system("clear" if os.name == "posix" else "cls")
    show_banner()
    show_menu()
    
    choice = input(f"\n{Fore.WHITE}[?] Select option: {Fore.RESET}")
    
    if choice == "1":
        os.system("python recon.py")
    elif choice == "2":
        os.system("python scanner.py")
    elif choice == "3":
        os.system("python scanner.py --sqli")
    elif choice == "4":
        os.system("python scanner.py --xss")
    elif choice == "5":
        os.system("python scanner.py --full")
    elif choice == "6":
        os.system("python exploit.py")
    elif choice == "7":
        print(f"{Fore.RED}[!] Exiting...")
        sys.exit(0)
    else:
        print(f"{Fore.RED}[!] Invalid option")
        sys.exit(1)

if __name__ == "__main__":
    main()
