import pandas as pd

# Leser inn CSV-filen
df = pd.read_csv(
    "load_data.csv",
    parse_dates=["Time(Local)"],
    index_col="Time(Local)"
)

# Viser de fem første radene
print(df.head())

# Sjekker hvilken type indeks vi har
print(type(df.index))

# Oppgave 5
print("\nFørste tidspunkt i datasettet:")
print(df.index[0])

# -------------------------
# Oppgave 6
# -------------------------

# Gjør produksjon og forbruk om fra tekst til tall
df["Production"] = (
    df["Production"]
    .str.replace(",", ".", regex=False)
    .astype(float)
)

df["Consumption"] = (
    df["Consumption"]
    .str.replace(",", ".", regex=False)
    .astype(float)
)

# Henter verdiene klokken 03:00
tidspunkt = df.index[3]

print("\nVerdier klokken 03:00:")
print(df.loc[tidspunkt])


# Henter ut 24 timer, fra 00:00 til 23:00
start = df.index[0]
slutt = df.index[23]

dogn = df.loc[start:slutt]

print("\n24-timers lastprofil:")
print(dogn)


# Plotter lastprofilen
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))

plt.plot(
    range(24),
    dogn["Consumption"],
    marker="o"
)

plt.title("24-timers lastprofil")
plt.xlabel("Klokkeslett")
plt.ylabel("Forbruk (MW)")
plt.grid(True)

# Lager klokkeslett fra 00:00 til 23:00
klokkeslett = [f"{time:02d}:00" for time in range(24)]

plt.xticks(
    range(24),
    klokkeslett,
    rotation=45
)

plt.tight_layout()
plt.show()

# Oppgave 7 - beregner nettoeffekt

df["Netto"] = df["Production"] - df["Consumption"]

print("\nData med nettoeffekt:")
print(df.head())

# Oppgave 8 - statistikk for produksjonen

maks_produksjon = df["Production"].max()
min_produksjon = df["Production"].min()
gjennomsnitt_produksjon = df["Production"].mean()

print("\nProduksjonsstatistikk:")
print("Maksimal produksjon:", maks_produksjon, "MW")
print("Minimal produksjon:", min_produksjon, "MW")
print("Gjennomsnittlig produksjon:", gjennomsnitt_produksjon, "MW")

# Oppgave 9 - maks og min nettoeffekt

maks_netto = df["Netto"].max()
min_netto = df["Netto"].min()

tid_maks_netto = df["Netto"].idxmax()
tid_min_netto = df["Netto"].idxmin()

print("\nNettoeffekt:")
print("Maksimal nettoeffekt:", maks_netto, "MW")
print("Tidspunkt:", tid_maks_netto)

print("Minimal nettoeffekt:", min_netto, "MW")
print("Tidspunkt:", tid_min_netto)


# Oppgave 10 - total produksjon

total_produksjon_mwh = df["Production"].sum()
total_produksjon_twh = total_produksjon_mwh / 1_000_000

print("\nTotal produksjon:")
print(total_produksjon_mwh, "MWh")
print(total_produksjon_twh, "TWh")

# Oppgave 11 - produksjon og forbruk over tid

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))

plt.plot(
    range(len(df)),
    df["Production"],
    label="Produksjon"
)

plt.plot(
    range(len(df)),
    df["Consumption"],
    label="Forbruk"
)

plt.title("Produksjon og forbruk over tid")
plt.xlabel("Tid")
plt.ylabel("Effekt (MW)")
plt.grid(True)
plt.legend()

# Lager noen få punkter på x-aksen
antall_punkter = 10
posisjoner = range(0, len(df), max(1, len(df) // antall_punkter))

# Henter datoene som hører til disse punktene
datoer = [
    str(df.index[i]).split(" ")[0]
    for i in posisjoner
]

plt.xticks(
    posisjoner,
    datoer,
    rotation=45
)

plt.tight_layout()
plt.show()

# Oppgave 12 - produksjon, forbruk og nettoeffekt

plt.figure(figsize=(12, 6))

plt.plot(
    range(len(df)),
    df["Production"],
    label="Produksjon"
)

plt.plot(
    range(len(df)),
    df["Consumption"],
    label="Forbruk"
)

plt.plot(
    range(len(df)),
    df["Netto"],
    label="Netto"
)

plt.title("Produksjon, forbruk og nettoeffekt over tid")
plt.xlabel("Tid")
plt.ylabel("Effekt (MW)")
plt.grid(True)
plt.legend()

# Lager noen få punkter på x-aksen
antall_punkter = 10
posisjoner = range(0, len(df), max(1, len(df) // antall_punkter))

datoer = [
    str(df.index[i]).split(" ")[0]
    for i in posisjoner
]

plt.xticks(
    posisjoner,
    datoer,
    rotation=45
)

plt.tight_layout()
plt.show()

# Oppgave 14 - finner tidspunkt for maks produksjon og forbruk

maks_prod_tid = df["Production"].idxmax()
maks_forbruk_tid = df["Consumption"].idxmax()

print("\nOppgave 14:")
print("Produksjonen er høyest:", maks_prod_tid)
print("Forbruket er høyest:", maks_forbruk_tid)