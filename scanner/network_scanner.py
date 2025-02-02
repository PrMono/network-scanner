import socket
import ipaddress
from concurrent.futures import ThreadPoolExecutor
from scanner.utils import export_results_to_csv  # Importer la fonction d'exportation

def scan_port(target_ip, port):
    """Scanne un port et affiche s'il est ouvert."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            if s.connect_ex((target_ip, port)) == 0:
                print(f"[+] Port {port} ouvert sur {target_ip}")
                return target_ip, port, "Open"
    except Exception as e:
        print(f"Erreur : {e}")
    return target_ip, port, "Closed"

def scan_network(network):
    """Scanne un réseau et détecte les hôtes actifs."""
    print(f"🔍 Scan du réseau {network} en cours...")
    active_hosts = []
    for ip in ipaddress.IPv4Network(network, strict=False):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                if s.connect_ex((str(ip), 80)) == 0:
                    print(f"[+] Hôte actif : {ip}")
                    active_hosts.append(str(ip))
        except:
            pass
    return active_hosts

def scan_active_hosts(hosts, ports):
    """Scanne les ports sur les hôtes détectés."""
    print("🔍 Scan des ports en cours...")
    results = []
    with ThreadPoolExecutor(max_workers=50) as executor:
        for host in hosts:
            for port in ports:
                result = executor.submit(scan_port, host, port)
                results.append(result.result())
    return results

if __name__ == "__main__":
    network = "192.168.1.0/24"
    ports_to_scan = [22, 80, 443, 3389]

    active_hosts = scan_network(network)
    
    if active_hosts:
        results = scan_active_hosts(active_hosts, ports_to_scan)
        export_results_to_csv(results)  # Sauvegarde en CSV
    else:
        print("❌ Aucun hôte actif trouvé.")
