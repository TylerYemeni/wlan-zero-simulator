import subprocess
import os

def capture_handshake(interface, bssid, channel):
    print("[+] Capturing WPA Handshake")
    dump_file = "capture"
    command = [
        "airodump-ng", "-c", channel,
        "--bssid", bssid,
        "-w", dump_file,
        interface
    ]
    try:
        subprocess.run(command)
    except KeyboardInterrupt:
        print("[!] Capture stopped. Check for handshake in capture-01.cap")
