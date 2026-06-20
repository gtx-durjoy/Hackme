#!/usr/bin/env python3
import os
import sys
import subprocess
from colorama import init, Fore, Style
init(autoreset=True)

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
    while True:
        os.system("clear" if os.name == "posix" else "cls")
        show_banner()
        show_menu()
        
        choice = input(f"\n{Fore.WHITE}[?] Select option: {Fore.RESET}").strip()
        
        if choice == "1":
            print(f"{Fore.GREEN}[+] Running Recon...{Fore.RESET}")
            subprocess.run(["python", "recon.py"])
            input("\nPress Enter to continue...")
        elif choice == "2":
            print(f"{Fore.GREEN}[+] Running Directory Brute-Force...{Fore.RESET}")
            subprocess.run(["python", "scanner.py"])
            input("\nPress Enter to continue...")
        elif choice == "3":
            print(f"{Fore.GREEN}[+] Running SQLi Scanner...{Fore.RESET}")
            subprocess.run(["python", "scanner.py", "--sqli"])
            input("\nPress Enter to continue...")
        elif choice == "4":
            print(f"{Fore.GREEN}[+] Running XSS Scanner...{Fore.RESET}")
            subprocess.run(["python", "scanner.py", "--xss"])
            input("\nPress Enter to continue...")
        elif choice == "5":
            print(f"{Fore.GREEN}[+] Running Full Scan...{Fore.RESET}")
            subprocess.run(["python", "scanner.py", "--full"])
            input("\nPress Enter to continue...")
        elif choice == "6":
            print(f"{Fore.GREEN}[+] Running Exploit...{Fore.RESET}")
            subprocess.run(["python", "exploit.py"])
            input("\nPress Enter to continue...")
        elif choice == "7":
            print(f"{Fore.RED}[!] Exiting...{Fore.RESET}")
            sys.exit(0)
        else:
            print(f"{Fore.RED}[!] Invalid option{Fore.RESET}")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()