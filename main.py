import argparse
from modules.monitor import enable_monitor_mode
from modules.sniffer import start_sniffing
from modules.deauth import perform_deauth_attack
from modules.handshake import capture_handshake
from modules.cracker import crack_handshake

def main():
    parser = argparse.ArgumentParser(description="WLAN Zero Simulator - WiFi Auditor")
    parser.add_argument("--iface", required=True, help="WiFi interface in monitor mode")
    parser.add_argument("--target", help="Target BSSID")
    parser.add_argument("--channel", help="Channel of target network")
    parser.add_argument("--wordlist", default="wordlists/rockyou.txt", help="Path to wordlist")
    parser.add_argument("--crack", action="store_true", help="Crack captured handshake")
    
    args = parser.parse_args()

    print("[*] Starting WLAN Zero Simulator")

    enable_monitor_mode(args.iface)

    if args.target and args.channel:
        capture_handshake(args.iface, args.target, args.channel)
        perform_deauth_attack(args.iface, args.target)
        if args.crack:
            crack_handshake(args.wordlist)
    else:
        start_sniffing(args.iface)

if __name__ == "__main__":
    main()
