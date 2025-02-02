import socket

def scan_port(target_ip, port):
    """Scanne un port spécifique."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            if s.connect_ex((target_ip, port)) == 0:
                return f"[+] Port {port} ouvert sur {target_ip}"
    except Exception as e:
        return f"Erreur sur {target_ip}:{port} → {e}"
    return f"[-] Port {port} fermé sur {target_ip}"
