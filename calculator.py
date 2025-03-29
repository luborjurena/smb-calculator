import pandas as pd

# Získanie vstupov od používateľa
try:
    basal_rate = float(input("Zadaj bazál (v J/hod): "))
    smb_uam_minutes = int(input("Zadaj SMB/UAM (v minútach): "))
    smb_ratio = float(input("Zadaj podiel SMB (napr. 0.5 pre 50%): "))

    # Výpočet
    bolus = basal_rate * (smb_uam_minutes / 60)
    adjusted_bolus = bolus * smb_ratio

    # Výpis výsledkov v tabuľke
    df = pd.DataFrame([{
        "Bazál (J/hod)": basal_rate,
        "SMB/UAM (min)": smb_uam_minutes,
        "Podiel SMB": smb_ratio,
        "Výsledný bolus (J)": round(adjusted_bolus, 3)
    }])

    print("\nVýpočet bolusu podľa zadaných hodnôt:\n")
    print(df.to_string(index=False))

except ValueError:
    print("⚠️ Nezadal si platné čísla. Skús znova.")
