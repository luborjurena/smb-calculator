import pandas as pd
from tabulate import tabulate

# Vstupné hodnoty
basal_rate = 1.0  # J/hod
smb_uam_minutes = [15, 30, 45, 60, 75, 90]
smb_ratio = 0.5   # Podiel SMB

# Výpočty
data = []
for minutes in smb_uam_minutes:
    bolus = basal_rate * (minutes / 60)
    adjusted_bolus = bolus * smb_ratio
    data.append({
        "Bazál (J/hod)": basal_rate,
        "SMB/UAM (min)": minutes,
        "Podiel SMB": smb_ratio,
        "Výsledný bolus (J)": round(adjusted_bolus, 3)
    })

# Vytvorenie DataFrame
df = pd.DataFrame(data)

# Vylepšený výstup v termináli s použitím Tabulate
print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))
