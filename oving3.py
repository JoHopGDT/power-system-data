import pandas as pd
import matplotlib.pyplot as plt

# Leser inn datasettet
df = pd.read_csv(
    "load/forbruk_2025.csv",
    index_col=0
)

# Gjør indeksen om til dato og klokkeslett
df.index = pd.to_datetime(df.index, utc=True)

# Vis de første radene
print(df.head())

# Vis informasjon om datasettet
print(df.info())
# Beregn gjennomsnittlig last for hver måned
manedlig_last = df.resample("ME").mean()

# Vis resultatet
print("\nGjennomsnittlig last per måned:")
print(manedlig_last)

import os

# Opprett results-mappen hvis den ikke finnes
os.makedirs("results", exist_ok=True)

# Lagre månedlig gjennomsnitt som CSV-fil
manedlig_last.to_csv("results/manedlig_last_2025.csv")

print("\nResultatet er lagret i results/manedlig_last_2025.csv")

# Lager figur av gjennomsnittlig månedlig last
plt.figure(figsize=(10, 6))

plt.plot(
    manedlig_last.index,
    manedlig_last["Actual Load"],
    marker="o"
)

plt.title("Gjennomsnittlig månedlig last i Norge 2025")
plt.xlabel("Måned")
plt.ylabel("Gjennomsnittlig last (MW)")
plt.grid(True)

plt.tight_layout()

# Lagre figuren
plt.savefig("results/manedlig_last_2025.png")

plt.show()

# Beregn statistikk for hver måned
manedlig_statistikk = df.resample("ME").agg(
    ["max", "min", "std"]
)

# Vis resultatet
print("\nMånedlig statistikk:")
print(manedlig_statistikk)

# Lagre resultatet
manedlig_statistikk.to_csv(
    "results/manedlig_last_statistikk_2025.csv"
)
