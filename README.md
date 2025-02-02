# 🔍 Network Scanner - Python
Un outil Python permettant de **scanner un réseau** et de **détecter les ports ouverts**.

- 🔎 Scan d’un sous-réseau (`192.168.1.0/24`)
- 🚀 Détection des ports ouverts (22, 80, 443, 3389)
- 📄 Exportation des résultats en CSV
- ⚡ Optimisé avec le **multithreading**

## 🚀 Installation
```bash
git clone https://github.com/PrMono/network-scanner.git
cd network-scanner
pip install -r requirements.txt

python scanner/network_scanner.py

| IP Address  | Port  | Status  |
|-------------|------|---------|
| 192.168.1.1 | 80   | Open ✅ |
| 192.168.1.50 | 443  | Open ✅ |
| 192.168.1.100 | 22  | Closed ❌ |

⚠️ **Utilisation légale uniquement !**  
Ce projet doit être utilisé uniquement sur des réseaux dont vous avez l’autorisation.

