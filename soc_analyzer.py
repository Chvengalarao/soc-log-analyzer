import re

file = open("logs.txt", "r")

brute_force = 0
port_scan = 0
malware = 0

attackers = []

for log in file:

    ip = re.findall(r"\d+\.\d+\.\d+\.\d+", log)

    if "Failed login" in log:
        brute_force += 1
        print("⚠ Brute Force Attack")

    elif "port scan" in log:
        port_scan += 1
        print("⚠ Port Scan Detected")

    elif "malware" in log:
        malware += 1
        print("⚠ Malware Activity")

    else:
        print("✓ Normal activity")

    if ip:
        attackers.append(ip[0])
        print("Attacker IP:", ip[0])

    print("------------------")

print("\n===== SOC REPORT =====")

print("Brute Force Attacks:", brute_force)
print("Port Scans:", port_scan)
print("Malware Alerts:", malware)

print("Attacker IPs:", attackers)
