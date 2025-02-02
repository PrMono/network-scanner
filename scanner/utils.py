import csv

def export_results_to_csv(results, filename="scan_results.csv"):
    """Sauvegarde les résultats du scan dans un fichier CSV."""
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["IP Address", "Port", "Status"])
        for result in results:
            if result:  # Évite d'écrire des valeurs nulles
                writer.writerow(result)
    print(f"✅ Résultats enregistrés dans {filename}")
