# VECTEUR 2 -> Detecter les volumes importants de requêtes suspectes
    # 5% des volumes les plus elevés

from pathlib import Path
import csv
from rich.pretty import pprint

log_path = Path(__file__).resolve().parent / "logs.csv"

with open(log_path, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    datas = list(reader)

pprint(datas[0]["source_ip"])

# VECTEUR 1 -> Analyse des IP
    # Calcul de la moyenne
    # Détection des IP > (10 x moyenne)

