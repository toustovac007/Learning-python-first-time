
'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.81 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.62 #? měsíční gravitace
SPEED_OF_LIGHT = 299792458 #? rychlost světla ve vakuu
SPEED_OF_SOUND = 343 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu
PLANCK_CONSTANT = 6.626e-34  #lanckova konstanta
C = SPEED_OF_LIGHT            # alias

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''




def vaha_na_planete(hmotnost: float, gravitace: float = EARTH_GRAVITY) -> float:
    """
    Vrátí tíhu tělesa (v newtonech) pro danou hmotnost a gravitační zrychlení.
    :param hmotnost: hmotnost tělesa v kilogramech
    :param gravitace: tíhové zrychlení (m/s^2)
    :return: tíha v newtonech
    """
    return hmotnost * gravitace


def energie_ze_hmoty(hmotnost: float) -> float:
    """
    Vypočítá energii podle Einsteinova vztahu E = m * c^2.
    :param hmotnost: hmotnost v kilogramech
    :return: energie v joulech
    """
    return hmotnost * C ** 2


def energie_fotonu(vlnovaDelka: float) -> float:
    """
    Vypočítá energii fotonu pro danou vlnovou délku.
    :param vlnovaDelka: vlnová délka v metrech
    :return: energie fotonu v joulech
    """
    return PLANCK_CONSTANT * C / vlnovaDelka


def cas_pro_zvuk(vzdalenostVMetrech: float) -> float:
    """
    Vypočítá čas, za který urazí zvuk danou vzdálenost při 20 °C.
    :param vzdalenostVMetrech: vzdálenost v metrech
    :return: čas v sekundách
    """
    return vzdalenostVMetrech / SPEED_OF_SOUND


def cas_pro_svetlo(vzdalenostVMetrech: float) -> float:
    """
    Vypočítá čas, za který urazí světlo danou vzdálenost ve vakuu.
    :param vzdalenostVMetrech: vzdálenost v metrech
    :return: čas v sekundách
    """
    return vzdalenostVMetrech / SPEED_OF_LIGHT