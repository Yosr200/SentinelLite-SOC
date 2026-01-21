def block_ip(ip, simulate=True):
    if simulate:
        print(f"[SIMULATION] Blocking IP {ip}")
    else:
        import os
        os.system(f"iptables -A INPUT -s {ip} -j DROP")
