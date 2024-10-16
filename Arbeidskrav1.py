# Arbeidskrav 1

# Valg av bil (Elbil eller bensinbil)

ant_km_aar = 10000

# Trafikkforsikringsavgift for begge
trafikkforsikringsavgift = 8.38 # kr/dag
trafikkforsikringsavgift_aar = trafikkforsikringsavgift * 365 # kr/år

# Årlig kostnader - ELBIL

# Forsikring 
forsikringEl = 5000 # kr/år

# Drivstoffbrukk
kWhKm = 0.2 #  kWh/km
kWhAar = ant_km_aar * kWhKm # kWh
strømpris = 2.00 # kr/kWh
total_drivsstoff_pris_el = kWhAar * strømpris # kr

# Bomavgift
bomavgift_el = 0.1 # kr/km
bomavgift_totalt_el = bomavgift_el * ant_km_aar # kr

# Totalt
total_el = forsikringEl + trafikkforsikringsavgift_aar + total_drivsstoff_pris_el + bomavgift_totalt_el # kr

print("Årlige kostnader for ELBIL:")
print("Forsikring: ", forsikringEl)
print("Trafikkforsikringsavgift: ", trafikkforsikringsavgift_aar)
print("Drivstoffbruk: ", total_drivsstoff_pris_el)
print("Bomavgift: ", bomavgift_totalt_el)
print("Total kostnader for ELBIL = ", total_el) 

print("")

# Årlig kostnader - BENSINBIL

# Forsikring 
forsikringBensin = 7500 # kr/år

# Drivstoffbrukk
bensin_pris = 1.0 # kr/km
total_drivsstoff_pris_bensin = ant_km_aar * bensin_pris # kr

# Bomavgift
bomavgift_bensin = 0.3 # kr/km
bomavgift_totalt_bensin = bomavgift_bensin * ant_km_aar # kr

# Totalt
total_bensin = forsikringBensin + trafikkforsikringsavgift_aar + total_drivsstoff_pris_bensin + bomavgift_totalt_bensin # kr

print("Årlige kostnader for BENSINBIL:")
print("Forsikring: ", forsikringBensin)
print("Trafikkforsikringsavgift: ", trafikkforsikringsavgift_aar)
print("Drivstoffbruk: ", total_drivsstoff_pris_bensin)
print("Bomavgift: ", bomavgift_totalt_bensin)
print("Total kostnader for BENSINBIL = ", total_bensin) 

print("")

if (total_bensin < total_el):
    print ("Du burde velge bensin bil!")
    print ("Bensinbil koster ", total_el - total_bensin, " kr billigere.")
else:
    print("Du burde velge elbil!")
    print ("Elbil koster ", total_bensin - total_el, " kr billigere.")

