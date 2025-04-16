import subprocess

def start_sniffing(interface):
    print("[+] Starting airodump-ng")
    subprocess.run(["airodump-ng", interface])
