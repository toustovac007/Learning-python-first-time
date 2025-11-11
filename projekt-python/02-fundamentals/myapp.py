"""
myapp.py – ukázková aplikace používající modul physics
Autor: [Tvoje jméno]
"""

import physics

def main():
    print("=== DEMONSTRACE MODULU physics ===\n")

    mass = 70  # kg
    print(f"Tíha člověka na Zemi: {physics.vaha_na_planete(mass):.2f} N")
    print(f"Tíha člověka na Měsíci: {physics.vaha_na_planete(mass, physics.MOON_GRAVITY):.2f} N")

    m = 0.001  # kg
    print(f"Energie podle E = mc^2 pro 1 g látky: {physics.energie_ze_hmoty(m):.2e} J")

    wavelength = 500e-9  # 500 nm = zelené světlo
    print(f"Energie jednoho fotonu se λ = 500 nm: {physics.energie_fotonu(wavelength):.2e} J")

    distance = 1000  # m
    print(f"Zvuk urazí 1 km za {physics.cas_pro_zvuk(distance):.3f} s")
    print(f"Světlo urazí 1 km za {physics.cas_pro_svetlo(distance):.9f} s")

if __name__ == "__main__":
    main()
