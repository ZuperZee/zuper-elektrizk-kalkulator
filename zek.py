from tkinter import *
from math import *


root = Tk()
root.title("Zuper Elektrizk Kalkulator")
root.geometry("900x720")

# Farger
col = "deepSkyBlue"
coll = "chocolate"

# Variables (Variabler)
# Variable for radrioknappene
knappVar = IntVar()

# Variables for Entries (Boks man skriver i)
# Variabler for begge
varBeggeU = DoubleVar()
varBeggeRf = DoubleVar()
varBeggeCos = DoubleVar()
varBeggeSin = DoubleVar()
varBeggeV = DoubleVar()
# Variabler for stjerne
varStjerneUf = DoubleVar()
varStjerneI = DoubleVar()
varStjerneIf = DoubleVar()
varStjerneR = DoubleVar()
varStjerneP1 = DoubleVar()
varStjerneP2 = DoubleVar()
varStjerneQ = DoubleVar()
varStjerneS = DoubleVar()
# Variabler for trekant
varTrekantUf = DoubleVar()
varTrekantI = DoubleVar()
varTrekantIf = DoubleVar()
varTrekantR = DoubleVar()
varTrekantP1 = DoubleVar()
varTrekantP2 = DoubleVar()
varTrekantQ = DoubleVar()
varTrekantS = DoubleVar()

# Variabler for hvor mye over og under som er akseptert vis det er flere Entries som er fylt inn av brukeren
overUnder = 0.02
maxOver = 1 + overUnder
minUnder = 1 - overUnder

# Tall etter komma/dot
etDigit = '.1f'
toDigits = '.2f'
treDigits = '.3f'
digits = toDigits

# Hvordan teksten skal se ut. (font)
fontForTittel = ("impact", 12)
fontForOvertekst = ("verdana", 9, "bold")
fontForOvertekstBigger = ("verdana", 15, "bold")
fontForLabels = ("verdana", 9)
fontForLabelsBigger = ("verdana", 10, "bold")
fontForKnapp = ("verdana", 12, "bold")


# Lister
# Lister over rader og kolonner
varRad1, varRad2, varRad3, varRad4, varRad5 = 2, 2, 3, 4, 5
varKolonne1, varKolonne2, varKolonne3, varKolonne4, varKolonne5 = 2, 3, 4, 5, 6,

# Labels for tilbakemelding (Feedback)
labelKalkuleringGlad = Label(root, text="Det var alt jeg klarte å regne ut (ᵔᴥᵔ)",
                             font=fontForOvertekst, fg="darkMagenta")
labelFeil = Label(root, text="Beklager, men jeg tror du har fylt inn feil",
                  font=fontForOvertekst, fg="red")


# Kalkulerer tallene
def kalkuler(event=None):

    labelFeil.grid_forget()
    labelKalkuleringGlad.grid_forget()
    labelKalkuleringGlad.grid(row=31, column=varKolonne1, columnspan=3, sticky=N)
    knappKalkuler.grid_forget()
    knappReset.grid(row=32, column=varKolonne1, columnspan=3, sticky=N)
    feil = 0
    fargeBrukerFyll = "limeGreen"

    # Hvilken Entry brukeren har fylt
    brukerBeggeU = 0
    brukerBeggeRf = 0
    brukerBeggeCos = 0
    brukerBeggeSin = 0
    brukerBeggeV = 0
    # Variabler for stjbrukererne
    brukerStjerneUf = 0
    brukerStjerneI = 0
    brukerStjerneIf = 0
    brukerStjerneR = 0
    brukerStjerneP1 = 0
    brukerStjerneP2 = 0
    brukerStjerneQ = 0
    brukerStjerneS = 0
    # Variabler for trekant
    brukerTrekantUf = 0
    brukerTrekantI = 0
    brukerTrekantIf = 0
    brukerTrekantR = 0
    brukerTrekantP1 = 0
    brukerTrekantP2 = 0
    brukerTrekantQ = 0
    brukerTrekantS = 0

    # Variabler for å få tallene fra entries (Boksene man skriver i)
    beggeU = getdouble(varBeggeU.get())
    stjerneUf = getdouble(varStjerneUf.get())
    trekantUf = getdouble(varTrekantUf.get())
    beggeCos = getdouble(varBeggeCos.get())
    beggeSin = getdouble(varBeggeSin.get())
    beggeRf = getdouble(varBeggeRf.get())
    stjerneR = getdouble(varStjerneR.get())
    trekantR = getdouble(varTrekantR.get())
    stjerneI = getdouble(varStjerneI.get())
    trekantI = getdouble(varTrekantI.get())
    stjerneIf = getdouble(varStjerneIf.get())
    trekantIf = getdouble(varTrekantIf.get())
    stjerneS = getdouble(varStjerneS.get())
    trekantS = getdouble(varTrekantS.get())
    stjerneP1 = getdouble(varStjerneP1.get())
    trekantP1 = getdouble(varTrekantP1.get())
    stjerneP2 = getdouble(varStjerneP2.get())
    trekantP2 = getdouble(varTrekantP2.get())
    stjerneQ = getdouble(varStjerneQ.get())
    trekantQ = getdouble(varTrekantQ.get())
    virkningsgrad = getdouble(varBeggeV.get())

    # Husker hvilket tall som brukeren fylte inn
    # Begge
    if beggeU > 0:
        brukerBeggeU = 1
    if beggeRf > 0:
        brukerBeggeRf = 1
    if beggeCos != 1:
        brukerBeggeCos = 1
    if beggeSin > 0:
        brukerBeggeSin = 1
    if virkningsgrad != 1:
        brukerBeggeV = 1
    # Stjerne
    if stjerneUf > 0:
        brukerStjerneUf = 1
    if stjerneR > 0:
        brukerStjerneR = 1
    if stjerneI > 0:
        brukerStjerneI = 1
    if stjerneIf > 0:
        brukerStjerneIf = 1
    if stjerneP1 > 0:
        brukerStjerneP1 = 1
    if stjerneP2 > 0:
        brukerStjerneP2 = 1
    if stjerneQ > 0:
        brukerStjerneQ = 1
    if stjerneS > 0:
        brukerStjerneS = 1
    # Trekant
    if trekantUf > 0:
        brukerTrekantUf = 1
    if trekantR > 0:
        brukerTrekantR = 1
    if trekantI > 0:
        brukerTrekantI = 1
    if trekantIf > 0:
        brukerTrekantIf = 1
    if trekantP1 > 0:
        brukerTrekantP1 = 1
    if trekantP2 > 0:
        brukerTrekantP2 = 1
    if trekantQ > 0:
        brukerTrekantQ = 1
    if trekantS > 0:
        brukerTrekantS = 1

    # Regner ut det den kan
    for a in range(2):
        for b in range(3):
            if 0 < beggeCos < 1:
                if beggeSin == 0:
                    bCos = acos(beggeCos)
                    beggeSin = sin(bCos)
                    labelFormelBeggeSin.configure(text="Sin = Sin(Cos^-1(Cos))")
                elif beggeSin > 0:
                    bCos = acos(beggeCos)
                    bBeggeSin = sin(bCos)
                    sjekkBeggeSin = bBeggeSin
                    minBeggeSin = sjekkBeggeSin * minUnder
                    maxBeggeSin = sjekkBeggeSin * maxOver
                    if beggeSin < minBeggeSin:
                        feil = 1
                    elif beggeSin > maxBeggeSin:
                        feil = 1
            elif beggeSin > 0:
                if beggeCos == 0 or 1:
                    bSin = asin(beggeSin)
                    beggeCos = cos(bSin)
                    labelFormelBeggeCos.configure(text="Cos = Cos(Sin^-1(Sin))")
            if beggeU + stjerneUf + trekantUf > 0:
                if beggeU > 0:
                    if stjerneUf == 0:
                        stjerneUf = beggeU / sqrt(3)
                        labelFormelStjerneUf.configure(text="Ufy = U / √3")
                    elif stjerneUf > 0:
                        sjekkStjerneUf = beggeU / sqrt(3)
                        minStjerneUf = sjekkStjerneUf * minUnder
                        maxStjerneUf = sjekkStjerneUf * maxOver
                        if stjerneUf < minStjerneUf:
                            feil = 1
                        elif stjerneUf > maxStjerneUf:
                            feil = 1
                    if trekantUf == 0:
                        trekantUf = beggeU
                        labelFormelTrekantUf.configure(text="UfΔ = U")
                    elif trekantUf > 0:
                        sjekkTrekantUf = beggeU
                        minTrekantUf = sjekkTrekantUf * minUnder
                        maxTrekantUf = sjekkTrekantUf * maxOver
                        if trekantUf < minTrekantUf:
                            feil = 1
                        elif trekantUf > maxTrekantUf:
                            feil = 1
                elif stjerneUf > 0:
                    if beggeU == 0:
                        beggeU = stjerneUf * sqrt(3)
                        labelFormelBeggeU.configure(text="U = Ufy * √3")
                    if trekantUf == 0:
                        trekantUf = stjerneUf * sqrt(3)
                        labelFormelTrekantUf.configure(text="UfΔ = Ufy * √3")
                    elif trekantUf > 0:
                        sjekkTrekantUf = stjerneUf * sqrt(3)
                        minTrekantUf = sjekkTrekantUf * minUnder
                        maxTrekantUf = sjekkTrekantUf * maxOver
                        if trekantUf < minTrekantUf:
                            feil = 1
                        elif trekantUf > maxTrekantUf:
                            feil = 1
                elif trekantUf > 0:
                    if beggeU == 0:
                        beggeU = trekantUf
                        labelFormelBeggeU.configure(text="U = UfΔ")
                    if stjerneUf == 0:
                        stjerneUf = trekantUf / sqrt(3)
                        labelFormelStjerneUf.configure(text="Ufy = UfΔ / √3")
            if beggeRf + stjerneR + trekantR > 0:
                if beggeRf > 0:
                    if stjerneR == 0:
                        stjerneR = beggeRf * sqrt(3)
                        labelFormelStjerneR.configure(text="Ry = Rf * √3")
                    elif stjerneR > 0:
                        sjekkStjerneR = beggeRf * sqrt(3)
                        minStjerneR = sjekkStjerneR * minUnder
                        maxStjerneR = sjekkStjerneR * maxOver
                        if stjerneR < minStjerneR:
                            feil = 1
                        elif stjerneR > maxStjerneR:
                            feil = 1
                    if trekantR == 0:
                        trekantR = beggeRf / sqrt(3)
                        labelFormelTrekantR.configure(text="RΔ = Rf / √3")
                    elif trekantR > 0:
                        sjekkTrekantR = beggeRf / sqrt(3)
                        minTrekantR = sjekkTrekantR * minUnder
                        maxTrekantR = sjekkTrekantR * maxOver
                        if trekantR < minTrekantR:
                            feil = 1
                        elif trekantR > maxTrekantR:
                            feil = 1
                elif stjerneR > 0:
                    if beggeRf == 0:
                        beggeRf = stjerneR / sqrt(3)
                        labelFormelBeggeRf.configure(text="Rf = Ry / √3")
                    if trekantR == 0:
                        trekantR = stjerneR / 3
                        labelFormelTrekantR.configure(text="RΔ = Ry / 3")
                    elif trekantR > 0:
                        sjekkTrekantR = stjerneR / 3
                        minTrekantR = sjekkTrekantR * minUnder
                        maxTrekantR = sjekkTrekantR * maxOver
                        if trekantR < minTrekantR:
                            feil = 1
                        elif trekantR > maxTrekantR:
                            feil = 1
                elif trekantR > 0:
                    if beggeRf == 0:
                        beggeRf = trekantR * sqrt(3)
                        labelFormelBeggeRf.configure(text="Rf = RΔ * √3")
                    if stjerneR == 0:
                        stjerneR = trekantR * 3
                        labelFormelStjerneR.configure(text="Ry =  RΔ * 3")
            if stjerneI + trekantI + stjerneIf + trekantIf > 0:
                if stjerneI > 0:
                    if trekantI == 0:
                        trekantI = stjerneI * 3
                        labelFormelTrekantI.configure(text="IΔ = Iy * 3")
                    elif trekantI > 0:
                        sjekkTrekantI = stjerneI * 3
                        minTrekantI = sjekkTrekantI * minUnder
                        maxTrekantI = sjekkTrekantI * maxOver
                        if trekantI < minTrekantI:
                            feil = 1
                        elif trekantI > maxTrekantI:
                            feil = 1
                    if stjerneIf == 0:
                        stjerneIf = stjerneI
                        labelFormelStjerneIf.configure(text="Ify = Iy")
                    elif stjerneIf > 0:
                        sjekkStjerneIf = stjerneI
                        minStjerneIf = sjekkStjerneIf * minUnder
                        maxStjerneIf = sjekkStjerneIf * maxOver
                        if stjerneIf < minStjerneIf:
                            feil = 1
                        elif stjerneIf > maxStjerneIf:
                            feil = 1
                    if trekantIf == 0:
                        trekantIf = stjerneI * sqrt(3)
                        labelFormelTrekantIf.configure(text="IfΔ = Iy * √3")
                    elif trekantIf > 0:
                        sjekkTrekantIf = stjerneI * sqrt(3)
                        minTrekantIf = sjekkTrekantIf * minUnder
                        maxTrekantIf = sjekkTrekantIf * maxOver
                        if trekantIf < minTrekantIf:
                            feil = 1
                        elif trekantIf > maxTrekantIf:
                            feil = 1
                elif trekantI > 0:
                    if stjerneI == 0:
                        stjerneI = trekantI / 3
                        labelFormelStjerneI.configure(text="Iy = IΔ / 3")
                        stjerneI2Digits = format(stjerneI, '.2f')
                        entryStjerneHovedstrom.delete(0, END)
                        entryStjerneHovedstrom.insert(0, stjerneI2Digits)
                    if stjerneIf == 0:
                        stjerneIf = trekantI / 3
                        labelFormelStjerneIf.configure(text="Ify = IΔ / 3")
                    elif stjerneIf > 0:
                        sjekkStjerneIf = trekantI / 3
                        minStjerneIf = sjekkStjerneIf * minUnder
                        maxStjerneIf = sjekkStjerneIf * maxOver
                        if stjerneIf < minStjerneIf:
                            feil = 1
                        elif stjerneIf > maxStjerneIf:
                            feil = 1
                    if trekantIf == 0:
                        trekantIf = trekantI / sqrt(3)
                        labelFormelTrekantIf.configure(text="IfΔ = IΔ / √3")
                    elif trekantIf > 0:
                        sjekkTrekantIf = trekantI / sqrt(3)
                        minTrekantIf = sjekkTrekantIf * minUnder
                        maxTrekantIf = sjekkTrekantIf * maxOver
                        if trekantIf < minTrekantIf:
                            feil = 1
                        elif trekantIf > maxTrekantIf:
                            feil = 1
                elif stjerneIf > 0:
                    if stjerneI == 0:
                        stjerneI = stjerneIf
                        labelFormelStjerneI.configure(text="Iy = Ify")
                    if trekantI == 0:
                        trekantI = stjerneIf * 3
                        labelFormelTrekantI.configure(text="IΔ = Ify * 3")
                    if trekantIf == 0:
                        trekantIf = stjerneIf * sqrt(3)
                        labelFormelTrekantIf.configure(text="IfΔ = Ify * √3")
                    elif trekantIf > 0:
                        sjekkTrekantIf = stjerneIf * sqrt(3)
                        minTrekantIf = sjekkTrekantIf * minUnder
                        maxTrekantIf = sjekkTrekantIf * maxOver
                        if trekantIf < minTrekantIf:
                            feil = 1
                        elif trekantIf > maxTrekantIf:
                            feil = 1
                elif trekantIf > 0:
                    if stjerneI == 0:
                        stjerneI = trekantIf / sqrt(3)
                        labelFormelStjerneI.configure(text="Iy = IfΔ / √3")
                    if trekantI == 0:
                        trekantI = trekantIf * sqrt(3)
                        labelFormelTrekantI.configure(text="IΔ = IfΔ * √3")
                    if stjerneIf == 0:
                        stjerneIf = trekantIf / sqrt(3)
                        labelFormelStjerneIf.configure(text="Ify = IfΔ / √3")
            if stjerneP1 + trekantP1 + stjerneP2 + trekantP2 + stjerneQ + trekantQ + stjerneS + trekantS > 0:
                if stjerneP1 > 0:
                    if trekantP1 == 0:
                        trekantP1 = stjerneP1 * 3
                        labelFormelTrekantP1.configure(text="P1Δ = P1y * 3 ")
                    elif trekantP1 > 0:
                        sjekkTrekantP1 = stjerneP1 * 3
                        minTrekantP1 = sjekkTrekantP1 * minUnder
                        maxTrekantP1 = sjekkTrekantP1 * maxOver
                        if trekantP1 < minTrekantP1:
                            feil = 1
                        elif trekantP1 > maxTrekantP1:
                            feil = 1
                    if stjerneP2 > 0:
                        if virkningsgrad == 1:
                            virkningsgrad = stjerneP2 / stjerneP1
                            labelFormelBeggeVirkningsgrad.configure(text="η = P2y / P1y")
                        elif virkningsgrad != 1:
                            sjekkVirkningsgrad = stjerneP2 / stjerneP1
                            minVirkningsgrad = sjekkVirkningsgrad * minUnder
                            maxVirkningsgrad = sjekkVirkningsgrad * maxOver
                            if virkningsgrad < minVirkningsgrad:
                                feil = 1
                            elif virkningsgrad > maxVirkningsgrad:
                                feil = 1
                    if trekantP2 > 0:
                        if virkningsgrad == 1:
                            virkningsgrad = trekantP2 / 3 / stjerneP1
                            labelFormelBeggeVirkningsgrad.configure(text="η = P2Δ / 3 / P1y")
                        elif virkningsgrad != 1:
                            sjekkVirkningsgrad = trekantP2 / 3 / stjerneP1
                            minVirkningsgrad = sjekkVirkningsgrad * minUnder
                            maxVirkningsgrad = sjekkVirkningsgrad * maxOver
                            if virkningsgrad < minVirkningsgrad:
                                feil = 1
                            elif virkningsgrad > maxVirkningsgrad:
                                feil = 1
                    if stjerneP2 == 0:
                        stjerneP2 = stjerneP1 * virkningsgrad
                        labelFormelStjerneP2.configure(text="P2y = P1y * η")
                    if trekantP2 == 0:
                        trekantP2 = stjerneP1 * 3 * virkningsgrad
                        labelFormelTrekantP2.configure(text="P2Δ = P1y * 3 * η")

                if trekantP1 > 0:
                    if stjerneP1 == 0:
                        stjerneP1 = trekantP1 / 3
                        labelFormelStjerneP1.configure(text="P1y = P1Δ / 3 ")
                    elif stjerneP1 > 0:
                        sjekkStjerneP1 = trekantP1 / 3
                        minStjerneP1 = sjekkStjerneP1 * minUnder
                        maxStjerneP1 = sjekkStjerneP1 * maxOver
                        if stjerneP1 < minStjerneP1:
                            feil = 1
                        elif stjerneP1 > maxStjerneP1:
                            feil = 1
                    if stjerneP2 > 0:
                        if virkningsgrad == 1:
                            virkningsgrad = stjerneP2 * 3 / trekantP1
                            labelFormelBeggeVirkningsgrad.configure(text="η = P2y * 3 / P1Δ")
                        elif virkningsgrad != 1:
                            sjekkVirkningsgrad = stjerneP2 * 3 / trekantP1
                            minVirkningsgrad = sjekkVirkningsgrad * minUnder
                            maxVirkningsgrad = sjekkVirkningsgrad * maxOver
                            if virkningsgrad < minVirkningsgrad:
                                feil = 1
                            elif virkningsgrad > maxVirkningsgrad:
                                feil = 1
                    if trekantP2 > 0:
                        if virkningsgrad == 1:
                            virkningsgrad = trekantP2 / trekantP1
                            labelFormelBeggeVirkningsgrad.configure(text="η = P2Δ / P1Δ")
                        elif virkningsgrad != 1:
                            sjekkVirkningsgrad = trekantP2 / trekantP1
                            minVirkningsgrad = sjekkVirkningsgrad * minUnder
                            maxVirkningsgrad = sjekkVirkningsgrad * maxOver
                            if virkningsgrad < minVirkningsgrad:
                                feil = 1
                            elif virkningsgrad > maxVirkningsgrad:
                                feil = 1
                    if stjerneP2 == 0:
                        stjerneP2 = trekantP1 / 3 * virkningsgrad
                        labelFormelStjerneP2.configure(text="P2y = P1Δ / 3 * η")
                    if trekantP2 == 0:
                        trekantP2 = trekantP1 * virkningsgrad
                        labelFormelTrekantP2.configure(text="P2Δ = P1Δ * η")

                if stjerneP2 > 0:
                    if trekantP2 == 0:
                        trekantP2 = stjerneP2 * 3
                        labelFormelTrekantP2.configure(text="P2Δ = P2y * 3")
                    elif trekantP2 > 0:
                        sjekkTrekantP2 = stjerneP2 * 3
                        minTrekantP2 = sjekkTrekantP2 * minUnder
                        maxTrekantP2 = sjekkTrekantP2 * maxOver
                        if trekantP2 < minTrekantP2:
                            feil = 1
                        elif trekantP2 > maxTrekantP2:
                            feil = 1
                    if stjerneP1 > 0:
                        if virkningsgrad == 1:
                            virkningsgrad = stjerneP2 / stjerneP1
                            labelFormelBeggeVirkningsgrad.configure(text="η = P2y / P1y")
                        elif virkningsgrad != 1:
                            sjekkVirkningsgrad = stjerneP2 / stjerneP1
                            minVirkningsgrad = sjekkVirkningsgrad * minUnder
                            maxVirkningsgrad = sjekkVirkningsgrad * maxOver
                            if virkningsgrad < minVirkningsgrad:
                                feil = 1
                            elif virkningsgrad > maxVirkningsgrad:
                                feil = 1
                    if trekantP1 > 0:
                        if virkningsgrad == 1:
                            virkningsgrad = stjerneP2 * 3 / trekantP1
                            labelFormelBeggeVirkningsgrad.configure(text="η = P2y * 3 / P1Δ")
                        elif virkningsgrad != 1:
                            sjekkVirkningsgrad = stjerneP2 * 3 / trekantP1
                            minVirkningsgrad = sjekkVirkningsgrad * minUnder
                            maxVirkningsgrad = sjekkVirkningsgrad * maxOver
                            if virkningsgrad < minVirkningsgrad:
                                feil = 1
                            elif virkningsgrad > maxVirkningsgrad:
                                feil = 1
                    if stjerneP1 == 0:
                        stjerneP1 = stjerneP2 / virkningsgrad
                        labelFormelStjerneP1.configure(text="P1y = P2y / η")
                    if trekantP1 == 0:
                        trekantP1 = stjerneP2 * 3 / virkningsgrad
                        labelFormelTrekantP1.configure(text="P1Δ = P2y * 3 / η")

                if trekantP2 > 0:
                    if stjerneP2 == 0:
                        stjerneP2 = trekantP2 / 3
                        labelFormelStjerneP2.configure(text="P2y = P2Δ / 3")
                    elif stjerneP2 > 0:
                        sjekkStjerneP2 = trekantP2 / 3
                        minStjerneP2 = sjekkStjerneP2 * minUnder
                        maxStjerneP2 = sjekkStjerneP2 * maxOver
                        if stjerneP2 < minStjerneP2:
                            feil = 1
                        elif stjerneP2 > maxStjerneP2:
                            feil = 1
                    if stjerneP1 > 0:
                        if virkningsgrad == 1:
                            virkningsgrad = trekantP2 / 3 / stjerneP1
                            labelFormelBeggeVirkningsgrad.configure(text="η = P2Δ / 3 / P1y")
                        elif virkningsgrad != 1:
                            sjekkVirkningsgrad = trekantP2 / 3 / stjerneP1
                            minVirkningsgrad = sjekkVirkningsgrad * minUnder
                            maxVirkningsgrad = sjekkVirkningsgrad * maxOver
                            if virkningsgrad < minVirkningsgrad:
                                feil = 1
                            elif virkningsgrad > maxVirkningsgrad:
                                feil = 1
                    if trekantP1 > 0:
                        if virkningsgrad == 1:
                            virkningsgrad = trekantP2 / trekantP1
                            labelFormelBeggeVirkningsgrad.configure(text="η = P2Δ / P1Δ")
                        elif virkningsgrad != 1:
                            sjekkVirkningsgrad = trekantP2 / trekantP1
                            minVirkningsgrad = sjekkVirkningsgrad * minUnder
                            maxVirkningsgrad = sjekkVirkningsgrad * maxOver
                            if virkningsgrad < minVirkningsgrad:
                                feil = 1
                            elif virkningsgrad > maxVirkningsgrad:
                                feil = 1
                    if stjerneP1 == 0:
                        stjerneP1 = trekantP2 / 3 / virkningsgrad
                        labelFormelStjerneP1.configure(text="P1y = P2Δ / 3 / η")
                    if trekantP1 == 0:
                        trekantP1 = trekantP2 / virkningsgrad
                        labelFormelTrekantP1.configure(text="P1Δ = P2Δ / η")

                if beggeCos == 1:
                    if stjerneP1 > 0:
                        if stjerneS == 0:
                            if stjerneQ > 0:
                                stjerneS = sqrt(stjerneP1 * stjerneP1 + stjerneQ * stjerneQ)
                                labelFormelStjerneS.configure(text="Sy = √(P1y * P1y + Qy * Qy)")
                            if trekantQ > 0:
                                stjerneS = sqrt(stjerneP1 * stjerneP1 + (trekantQ * trekantQ) / 9)
                                labelFormelStjerneS.configure(text="Sy = √(P1y * P1y + (QΔ * QΔ)/9)")
                        if stjerneS > 0:
                            beggeCos = stjerneP1 / stjerneS
                            labelFormelBeggeCos.configure(text="Cos = P1y / Sy")
                        elif trekantS > 0:
                            beggeCos = stjerneP1 * 3 / trekantS
                            labelFormelBeggeCos.configure(text="Cos = P1y * 3 / SΔ")

                    if beggeSin == 0:
                        bCos = acos(beggeCos)
                        beggeSin = sin(bCos)
                        labelFormelBeggeSin.configure(text="Sin = Sin(Cos^-1(Cos))")
                    elif beggeSin > 0:
                        bCos = acos(beggeCos)
                        bBeggeSin = sin(bCos)
                        sjekkBeggeSin = bBeggeSin
                        minBeggeSin = sjekkBeggeSin * minUnder
                        maxBeggeSin = sjekkBeggeSin * maxOver
                        if beggeSin < minBeggeSin:
                            feil = 1
                        elif beggeSin > maxBeggeSin:
                            feil = 1

                if stjerneQ > 0:
                    if trekantQ == 0:
                        trekantQ = stjerneQ * 3
                        labelFormelTrekantQ.configure(text="QΔ = Qy * 3")
                    if trekantQ > 0:
                        sjekkTrekantQ = stjerneQ * 3
                        minTrekantQ = sjekkTrekantQ * minUnder
                        maxTrekantQ = sjekkTrekantQ * maxOver
                        if trekantQ < minTrekantQ:
                            feil = 1
                        if trekantQ > maxTrekantQ:
                            feil = 1

                elif trekantQ > 0:
                    stjerneQ = trekantQ / 3
                    labelFormelStjerneQ.configure(text="Qy = QΔ / 3")

                if stjerneS == 0:
                    if stjerneP1 > 0:
                        if beggeCos != 1:
                            stjerneS = stjerneP1 / beggeCos
                            labelFormelStjerneS.configure(text="Sy = P1y / Cos")
                        elif stjerneQ > 0:
                            stjerneS = sqrt(stjerneP1 * stjerneP1 + stjerneQ * stjerneQ)
                            labelFormelStjerneS.configure(text="Sy = √(P1y * P1y + Qy * Qy")
                    if stjerneQ > 0:
                        if beggeSin > 0:
                            stjerneS = stjerneQ / beggeSin
                            labelFormelStjerneS.configure(text="Sy = Qy / Sin")
                if trekantS > 0:
                    if stjerneS == 0:
                        stjerneS = trekantS / 3
                        labelFormelStjerneS.configure(text="Sy = SΔ / 3")

                if stjerneS > 0:
                    if trekantS == 0:
                        trekantS = stjerneS * 3
                        labelFormelTrekantS.configure(text="SΔ = Sy * 3")
                    elif trekantS > 0:
                        sjekkTrekantS = stjerneS * 3
                        minTrekantS = sjekkTrekantS * minUnder
                        maxTrekantS = sjekkTrekantS * maxOver
                        if trekantS < minTrekantS:
                            feil = 1
                        elif trekantS > maxTrekantS:
                            feil = 1
                    if beggeCos != 1:
                        if stjerneP1 == 0:
                            stjerneP1 = stjerneS * beggeCos
                            labelFormelStjerneP1.configure(text="P1y = Sy * Cos")
                        elif stjerneP1 > 0:
                            sjekkStjerneP1 = stjerneS * beggeCos
                            minStjerneP1 = sjekkStjerneP1 * minUnder
                            maxStjerneP1 = sjekkStjerneP1 * maxOver
                            if stjerneP1 < minStjerneP1:
                                feil = 1
                            elif stjerneP1 > maxStjerneP1:
                                feil = 1
                        if stjerneQ == 0:
                            stjerneQ = stjerneS * beggeSin
                            labelFormelStjerneQ.configure(text="Qy = Sy * Sin")
                        if stjerneQ > 0:
                            sjekkStjerneQ = stjerneS * beggeSin
                            minStjerneQ = sjekkStjerneQ * minUnder
                            maxStjerneQ = sjekkStjerneQ * maxOver
                            if stjerneQ < minStjerneQ:
                                feil = 1
                            elif stjerneQ > maxStjerneQ:
                                feil = 1

            if stjerneS == 0:
                if stjerneP1 > 0:
                    if beggeCos != 0:
                        stjerneS = stjerneP1 / beggeCos
                    labelFormelStjerneS.configure(text="Sy = P1y / Cos")
                elif stjerneQ > 0:
                    if beggeSin != 0:
                        stjerneS = stjerneQ / beggeSin
                    labelFormelStjerneS.configure(text="Sy = Qy / Sin")

            if stjerneP1 == 0:
                if stjerneS > 0:
                    stjerneP1 = stjerneS * beggeCos
                    labelFormelStjerneP1.configure(text="P1y = Sy * Cos")

            if stjerneQ == 0:
                if stjerneS > 0:
                    stjerneQ = stjerneS * beggeSin
                    labelFormelStjerneQ.configure(text="Qy = Sy * Sin")

            if beggeU > 0:
                if beggeRf > 0:
                    if stjerneIf == 0:
                        stjerneIf = stjerneUf / beggeRf
                        labelFormelStjerneIf.configure(text="Ify = Ufs / Rf")
                    elif stjerneIf > 0:
                        sjekkStjerneIf = stjerneUf / beggeRf
                        minStjerneIf = sjekkStjerneIf * minUnder
                        maxStjerneIf = sjekkStjerneIf * maxOver
                        if stjerneIf < minStjerneIf:
                            feil = 1
                        elif stjerneIf > maxStjerneIf:
                            feil = 1

                    if stjerneS == 0:
                        stjerneS = stjerneUf * stjerneUf / beggeRf * 3
                        labelFormelStjerneS.configure(text="Sy = Ufy * Ufy / Rf * 3")
                    elif stjerneS > 0:
                        sjekkStjerneS = stjerneUf * stjerneUf / beggeRf * 3
                        minStjerneS = sjekkStjerneS * minUnder
                        maxStjerneS = sjekkStjerneS * maxOver
                        if stjerneS < minStjerneS:
                            feil = 1
                        elif stjerneS > maxStjerneS:
                            feil = 1

                elif stjerneIf > 0:
                    if beggeRf == 0:
                        beggeRf = stjerneUf / stjerneIf
                        labelFormelBeggeRf.configure(text="Rf = Ufy / Ify")

                    if stjerneS == 0:
                        stjerneS = stjerneUf * stjerneIf * 3
                        labelFormelStjerneS.configure(text="Sy = Ufy * Ify * 3")
                    elif stjerneS > 0:
                        sjekkStjerneS = stjerneUf * stjerneIf * 3
                        minStjerneS = sjekkStjerneS * minUnder
                        maxStjerneS = sjekkStjerneS * maxOver
                        if stjerneS < minStjerneS:
                            feil = 1
                        elif stjerneS > maxStjerneS:
                            feil = 1

                elif stjerneS > 0:
                    if stjerneIf == 0:
                        stjerneIf = stjerneS / stjerneUf / 3
                        labelFormelStjerneIf.configure(text="Ify = Sy / Ufs / 3")

                    if beggeRf == 0:
                        beggeRf = stjerneUf * stjerneUf / stjerneS * 3
                        labelFormelBeggeRf.configure(text="Rf = Ufy * Ufy / Sy * 3")

            elif beggeRf > 0:
                if stjerneIf > 0:
                    if beggeU == 0:
                        beggeU = beggeRf * stjerneIf * sqrt(3)
                        labelFormelBeggeU.configure(text="U = Rf * Ify * √3")

                    if stjerneS == 0:
                        stjerneS = stjerneIf * stjerneIf * beggeRf * 3
                        labelFormelStjerneS.configure(text="Sy = Ify * Ify * Rf * 3")
                    elif stjerneS > 0:
                        sjekkStjerneS = stjerneIf * stjerneIf * beggeRf * 3
                        minStjerneS = sjekkStjerneS * minUnder
                        maxStjerneS = sjekkStjerneS * maxOver
                        if stjerneS < minStjerneS:
                            feil = 1
                        elif stjerneS > maxStjerneS:
                            feil = 1

                elif stjerneS > 0:
                    if beggeU == 0:
                        beggeU = sqrt(stjerneS * beggeRf)
                        labelFormelBeggeU.configure(text="U = √(Sy * Rf)")
                    if stjerneIf == 0:
                        stjerneIf = sqrt(stjerneS / beggeRf / 3)
                        labelFormelStjerneIf.configure(text="Ify = √(Sy / Rf / 3)")
                    elif stjerneIf > 0:
                        sjekkStjerneIf = stjerneUf / beggeRf
                        minStjerneIf = sjekkStjerneIf * minUnder
                        maxStjerneIf = sjekkStjerneIf * maxOver
                        if stjerneIf < minStjerneIf:
                            feil = 1
                        elif stjerneIf > maxStjerneIf:
                            feil = 1

            elif stjerneIf > 0:
                if stjerneS > 0:
                    if beggeU == 0:
                        beggeU = stjerneS / stjerneIf / sqrt(3)
                        labelFormelBeggeU.configure(text="U = Sy / Ify / √3")
                    if beggeRf == 0:
                        beggeRf = (stjerneS / 3) / (stjerneIf * stjerneIf)
                        labelFormelBeggeRf.configure(text="Rf = (Sy / 3) / (Ify * Ify)")

    # Tall etter komma/dot
    # Begge
    beggeUDigits = format(beggeU, digits)
    beggeRfDigits = format(beggeRf, digits)
    beggeCosDigits = format(beggeCos, digits)
    beggeSinDigits = format(beggeSin, digits)
    beggeVirkningsgradDigits = format(virkningsgrad, digits)
    # Stjerne
    stjerneUfDigits = format(stjerneUf, digits)
    stjerneRDigits = format(stjerneR, digits)
    stjerneIDigits = format(stjerneI, digits)
    stjerneIfDigits = format(stjerneIf, digits)
    stjerneP1Digits = format(stjerneP1, digits)
    stjerneP2Digits = format(stjerneP2, digits)
    stjerneQDigits = format(stjerneQ, digits)
    stjerneSDigits = format(stjerneS, digits)
    # Trekant
    trekantUfDigits = format(trekantUf, digits)
    trekantRDigits = format(trekantR, digits)
    trekantIDigits = format(trekantI, digits)
    trekantIfDigits = format(trekantIf, digits)
    trekantP1Digits = format(trekantP1, digits)
    trekantP2Digits = format(trekantP2, digits)
    trekantQDigits = format(trekantQ, digits)
    trekantSDigits = format(trekantS, digits)

    # Hvis det er en feil med tallene brukeren skreiv inn vil tallene som brukeren skreiv inn bli rødfarget
    if feil == 1:
        if brukerBeggeU == 0:
            entryBeggeHovedspenning.delete(0, END)
            entryBeggeHovedspenning.insert(0, 0.0)
        elif brukerBeggeU == 1:
            entryBeggeHovedspenning.configure(fg="red")

        if brukerBeggeRf == 0:
            entryBeggeFaseresistans.delete(0, END)
            entryBeggeFaseresistans.insert(0, 0.0)
        elif brukerBeggeRf == 1:
            entryBeggeFaseresistans.configure(fg="red")

        if brukerBeggeCos == 0:
            entryBeggeCosPhi.delete(0, END)
            entryBeggeCosPhi.insert(0, 1.0)
        elif brukerBeggeCos == 1:
            entryBeggeCosPhi.configure(fg="red")

        if brukerBeggeSin == 0:
            entryBeggeSinPhi.delete(0, END)
            entryBeggeSinPhi.insert(0, 0.0)
        elif brukerBeggeSin == 1:
            entryBeggeSinPhi.configure(fg="red")

        if brukerBeggeV == 0:
            entryBeggeVirkningsgrad.delete(0, END)
            entryBeggeVirkningsgrad.insert(0, 1.0)
        elif brukerBeggeV == 1:
            entryBeggeVirkningsgrad.configure(fg="red")

        if brukerStjerneUf == 0:
            entryStjerneFasespenning.delete(0, END)
            entryStjerneFasespenning.insert(0, 0.0)
        elif brukerStjerneUf == 1:
            entryStjerneFasespenning.configure(fg="red")

        if brukerStjerneR == 0:
            entryStjerneHovedresistans.delete(0, END)
            entryStjerneHovedresistans.insert(0, 0.0)
        elif brukerStjerneR == 1:
            entryStjerneHovedresistans.configure(fg="red")

        if brukerStjerneI == 0:
            entryStjerneHovedstrom.delete(0, END)
            entryStjerneHovedstrom.insert(0, 0.0)
        elif brukerStjerneI == 1:
            entryStjerneHovedstrom.configure(fg="red")

        if brukerStjerneIf == 0:
            entryStjerneFasestrom.delete(0, END)
            entryStjerneFasestrom.insert(0, 0.0)
        elif brukerStjerneIf == 1:
            entryStjerneFasestrom.configure(fg="red")

        if brukerStjerneP1 == 0:
            entryStjerneTilfortEffekt.delete(0, END)
            entryStjerneTilfortEffekt.insert(0, 0.0)
        elif brukerStjerneP1 == 1:
            entryStjerneTilfortEffekt.configure(fg="red")

        if brukerStjerneP2 == 0:
            entryStjerneAvgittEffekt.delete(0, END)
            entryStjerneAvgittEffekt.insert(0, 0.0)
        elif brukerStjerneP2 == 1:
            entryStjerneAvgittEffekt.configure(fg="red")

        if brukerStjerneQ == 0:
            entryStjerneReaktivEffekt.delete(0, END)
            entryStjerneReaktivEffekt.insert(0, 0.0)
        elif brukerStjerneQ == 1:
            entryStjerneReaktivEffekt.configure(fg="red")

        if brukerStjerneS == 0:
            entryStjerneTilsynelatendeEffekt.delete(0, END)
            entryStjerneTilsynelatendeEffekt.insert(0, 0.0)
        elif brukerStjerneS == 1:
            entryStjerneTilsynelatendeEffekt.configure(fg="red")

        if brukerTrekantUf == 0:
            entryTrekantFasespenning.delete(0, END)
            entryTrekantFasespenning.insert(0, 0.0)
        elif brukerTrekantUf == 1:
            entryTrekantFasespenning.configure(fg="red")

        if brukerTrekantR == 0:
            entryTrekantHovedresistans.delete(0, END)
            entryTrekantHovedresistans.insert(0, 0.0)
        elif brukerTrekantR == 1:
            entryTrekantHovedresistans.configure(fg="red")

        if brukerTrekantI == 0:
            entryTrekantHovedstrom.delete(0, END)
            entryTrekantHovedstrom.insert(0, 0.0)
        elif brukerTrekantI == 1:
            entryTrekantHovedstrom.configure(fg="red")

        if brukerTrekantIf == 0:
            entryTrekantFasestrom.delete(0, END)
            entryTrekantFasestrom.insert(0, 0.0)
        elif brukerTrekantIf == 1:
            entryTrekantFasestrom.configure(fg="red")

        if brukerTrekantP1 == 0:
            entryTrekantTilfortEffekt.delete(0, END)
            entryTrekantTilfortEffekt.insert(0, 0.0)
        elif brukerTrekantP1 == 1:
            entryTrekantTilfortEffekt.configure(fg="red")

        if brukerTrekantP2 == 0:
            entryTrekantAvgittEffekt.delete(0, END)
            entryTrekantAvgittEffekt.insert(0, 0.0)
        elif brukerTrekantP2 == 1:
            entryTrekantAvgittEffekt.configure(fg="red")

        if brukerTrekantQ == 0:
            entryTrekantReaktivEffekt.delete(0, END)
            entryTrekantReaktivEffekt.insert(0, 0.0)
        elif brukerTrekantQ == 1:
            entryTrekantReaktivEffekt.configure(fg="red")

        if brukerTrekantS == 0:
            entryTrekantTilsynelatendeEffekt.delete(0, END)
            entryTrekantTilsynelatendeEffekt.insert(0, 0.0)
        elif brukerTrekantS == 1:
            entryTrekantTilsynelatendeEffekt.configure(fg="red")

        # Glemmer Grids for Formel-Labels
        # Begge
        labelFormelBeggeU.configure(text="")
        labelFormelBeggeRf.configure(text="")
        labelFormelBeggeCos.configure(text="")
        labelFormelBeggeSin.configure(text="")
        labelFormelBeggeVirkningsgrad.configure(text="")
        # Stjerne
        labelFormelStjerneUf.configure(text="")
        labelFormelStjerneR.configure(text="")
        labelFormelStjerneI.configure(text="")
        labelFormelStjerneIf.configure(text="")
        labelFormelStjerneP1.configure(text="")
        labelFormelStjerneP2.configure(text="")
        labelFormelStjerneQ.configure(text="")
        labelFormelStjerneS.configure(text="")
        # Trekant
        labelFormelTrekantUf.configure(text="")
        labelFormelTrekantR.configure(text="")
        labelFormelTrekantI.configure(text="")
        labelFormelTrekantIf.configure(text="")
        labelFormelTrekantP1.configure(text="")
        labelFormelTrekantP2.configure(text="")
        labelFormelTrekantQ.configure(text="")
        labelFormelTrekantS.configure(text="")

        labelKalkuleringGlad.grid_forget()
        labelFeil.grid(row=31, column=varKolonne1, columnspan=3, sticky=N)

    # Tallene som brukeren skreiv inn vil bli grønne vis det ikke er noen feil
    else:
        # Begge
        if brukerBeggeU == 1:
            entryBeggeHovedspenning.configure(fg=fargeBrukerFyll)
        elif brukerBeggeU == 0:
            entryBeggeHovedspenning.delete(0, END)
            entryBeggeHovedspenning.insert(0, beggeUDigits)

        if brukerBeggeRf == 1:
            entryBeggeFaseresistans.configure(fg=fargeBrukerFyll)
        elif brukerBeggeRf == 0:
            entryBeggeFaseresistans.delete(0, END)
            entryBeggeFaseresistans.insert(0, beggeRfDigits)

        if brukerBeggeCos == 1:
            entryBeggeCosPhi.configure(fg=fargeBrukerFyll)
        elif brukerBeggeCos == 0:
            entryBeggeCosPhi.delete(0, END)
            entryBeggeCosPhi.insert(0, beggeCosDigits)

        if brukerBeggeSin == 1:
            entryBeggeSinPhi.configure(fg=fargeBrukerFyll)
        elif brukerBeggeSin == 0:
            entryBeggeSinPhi.delete(0, END)
            entryBeggeSinPhi.insert(0, beggeSinDigits)

        if brukerBeggeV == 1:
            entryBeggeVirkningsgrad.configure(fg=fargeBrukerFyll)
        elif brukerBeggeV == 0:
            entryBeggeVirkningsgrad.delete(0, END)
            entryBeggeVirkningsgrad.insert(0, beggeVirkningsgradDigits)

        # Stjerne
        if brukerStjerneUf == 1:
            entryStjerneFasespenning.configure(fg=fargeBrukerFyll)
        elif brukerStjerneUf == 0:
            entryStjerneFasespenning.delete(0, END)
            entryStjerneFasespenning.insert(0, stjerneUfDigits)

        if brukerStjerneR == 1:
            entryStjerneHovedresistans.configure(fg=fargeBrukerFyll)
        elif brukerStjerneR == 0:
            entryStjerneHovedresistans.delete(0, END)
            entryStjerneHovedresistans.insert(0, stjerneRDigits)

        if brukerStjerneI == 1:
            entryStjerneHovedstrom.configure(fg=fargeBrukerFyll)
        elif brukerStjerneI == 0:
            entryStjerneHovedstrom.delete(0, END)
            entryStjerneHovedstrom.insert(0, stjerneIDigits)

        if brukerStjerneIf == 1:
            entryStjerneFasestrom.configure(fg=fargeBrukerFyll)
        elif brukerStjerneIf == 0:
            entryStjerneFasestrom.delete(0, END)
            entryStjerneFasestrom.insert(0, stjerneIfDigits)

        if brukerStjerneP1 == 1:
            entryStjerneTilfortEffekt.configure(fg=fargeBrukerFyll)
        elif brukerStjerneP1 == 0:
            entryStjerneTilfortEffekt.delete(0, END)
            entryStjerneTilfortEffekt.insert(0, stjerneP1Digits)

        if brukerStjerneP2 == 1:
            entryStjerneAvgittEffekt.configure(fg=fargeBrukerFyll)
        elif brukerStjerneP2 == 0:
            entryStjerneAvgittEffekt.delete(0, END)
            entryStjerneAvgittEffekt.insert(0, stjerneP2Digits)

        if brukerStjerneQ == 1:
            entryStjerneReaktivEffekt.configure(fg=fargeBrukerFyll)
        elif brukerStjerneQ == 0:
            entryStjerneReaktivEffekt.delete(0, END)
            entryStjerneReaktivEffekt.insert(0, stjerneQDigits)

        if brukerStjerneS == 1:
            entryStjerneTilsynelatendeEffekt.configure(fg=fargeBrukerFyll)
        elif brukerStjerneS == 0:
            entryStjerneTilsynelatendeEffekt.delete(0, END)
            entryStjerneTilsynelatendeEffekt.insert(0, stjerneSDigits)

        # Trekant
        if brukerTrekantUf == 1:
            entryTrekantFasespenning.configure(fg=fargeBrukerFyll)
        elif brukerTrekantUf == 0:
            entryTrekantFasespenning.delete(0, END)
            entryTrekantFasespenning.insert(0, trekantUfDigits)

        if brukerTrekantR == 1:
            entryTrekantHovedresistans.configure(fg=fargeBrukerFyll)
        elif brukerTrekantR == 0:
            entryTrekantHovedresistans.delete(0, END)
            entryTrekantHovedresistans.insert(0, trekantRDigits)

        if brukerTrekantI == 1:
            entryTrekantHovedstrom.configure(fg=fargeBrukerFyll)
        elif brukerTrekantI == 0:
            entryTrekantHovedstrom.delete(0, END)
            entryTrekantHovedstrom.insert(0, trekantIDigits)

        if brukerTrekantIf == 1:
            entryTrekantFasestrom.configure(fg=fargeBrukerFyll)
        elif brukerTrekantIf == 0:
            entryTrekantFasestrom.delete(0, END)
            entryTrekantFasestrom.insert(0, trekantIfDigits)

        if brukerTrekantP1 == 1:
            entryTrekantTilfortEffekt.configure(fg=fargeBrukerFyll)
        elif brukerTrekantP1 == 0:
            entryTrekantTilfortEffekt.delete(0, END)
            entryTrekantTilfortEffekt.insert(0, trekantP1Digits)

        if brukerTrekantP2 == 1:
            entryTrekantAvgittEffekt.configure(fg=fargeBrukerFyll)
        elif brukerTrekantP2 == 0:
            entryTrekantAvgittEffekt.delete(0, END)
            entryTrekantAvgittEffekt.insert(0, trekantP2Digits)

        if brukerTrekantQ == 1:
            entryTrekantReaktivEffekt.configure(fg=fargeBrukerFyll)
        elif brukerTrekantQ == 0:
            entryTrekantReaktivEffekt.delete(0, END)
            entryTrekantReaktivEffekt.insert(0, trekantQDigits)

        if brukerTrekantS == 1:
            entryTrekantTilsynelatendeEffekt.configure(fg=fargeBrukerFyll)
        elif brukerTrekantS == 0:
            entryTrekantTilsynelatendeEffekt.delete(0, END)
            entryTrekantTilsynelatendeEffekt.insert(0, trekantSDigits)


def nullstill():
    # Nullstiller Entries
    entryBeggeHovedspenning.delete(0, END)
    entryBeggeHovedspenning.insert(0, 0.0)
    entryBeggeHovedspenning.configure(fg="black")
    entryBeggeFaseresistans.delete(0, END)
    entryBeggeFaseresistans.insert(0, 0.0)
    entryBeggeFaseresistans.configure(fg="black")
    entryBeggeCosPhi.delete(0, END)
    entryBeggeCosPhi.insert(0, 1.0)
    entryBeggeCosPhi.configure(fg="black")
    entryBeggeSinPhi.delete(0, END)
    entryBeggeSinPhi.insert(0, 0.0)
    entryBeggeSinPhi.configure(fg="black")
    entryBeggeVirkningsgrad.delete(0, END)
    entryBeggeVirkningsgrad.insert(0, 1.0)
    entryBeggeVirkningsgrad.configure(fg="black")
    entryStjerneFasespenning.delete(0, END)
    entryStjerneFasespenning.insert(0, 0.0)
    entryStjerneFasespenning.configure(fg="black")
    entryStjerneHovedresistans.delete(0, END)
    entryStjerneHovedresistans.insert(0, 0.0)
    entryStjerneHovedresistans.configure(fg="black")
    entryStjerneHovedstrom.delete(0, END)
    entryStjerneHovedstrom.insert(0, 0.0)
    entryStjerneHovedstrom.configure(fg="black")
    entryStjerneFasestrom.delete(0, END)
    entryStjerneFasestrom.insert(0, 0.0)
    entryStjerneFasestrom.configure(fg="black")
    entryStjerneTilfortEffekt.delete(0, END)
    entryStjerneTilfortEffekt.insert(0, 0.0)
    entryStjerneTilfortEffekt.configure(fg="black")
    entryStjerneAvgittEffekt.delete(0, END)
    entryStjerneAvgittEffekt.insert(0, 0.0)
    entryStjerneAvgittEffekt.configure(fg="black")
    entryStjerneReaktivEffekt.delete(0, END)
    entryStjerneReaktivEffekt.insert(0, 0.0)
    entryStjerneReaktivEffekt.configure(fg="black")
    entryStjerneTilsynelatendeEffekt.delete(0, END)
    entryStjerneTilsynelatendeEffekt.insert(0, 0.0)
    entryStjerneTilsynelatendeEffekt.configure(fg="black")
    entryTrekantFasespenning.delete(0, END)
    entryTrekantFasespenning.insert(0, 0.0)
    entryTrekantFasespenning.configure(fg="black")
    entryTrekantHovedresistans.delete(0, END)
    entryTrekantHovedresistans.insert(0, 0.0)
    entryTrekantHovedresistans.configure(fg="black")
    entryTrekantHovedstrom.delete(0, END)
    entryTrekantHovedstrom.insert(0, 0.0)
    entryTrekantHovedstrom.configure(fg="black")
    entryTrekantFasestrom.delete(0, END)
    entryTrekantFasestrom.insert(0, 0.0)
    entryTrekantFasestrom.configure(fg="black")
    entryTrekantTilfortEffekt.delete(0, END)
    entryTrekantTilfortEffekt.insert(0, 0.0)
    entryTrekantTilfortEffekt.configure(fg="black")
    entryTrekantAvgittEffekt.delete(0, END)
    entryTrekantAvgittEffekt.insert(0, 0.0)
    entryTrekantAvgittEffekt.configure(fg="black")
    entryTrekantReaktivEffekt.delete(0, END)
    entryTrekantReaktivEffekt.insert(0, 0.0)
    entryTrekantReaktivEffekt.configure(fg="black")
    entryTrekantTilsynelatendeEffekt.delete(0, END)
    entryTrekantTilsynelatendeEffekt.insert(0, 0.0)
    entryTrekantTilsynelatendeEffekt.configure(fg="black")

    # Glemmer Grids for Formel-Labels
    # Begge
    labelFormelBeggeU.configure(text="")
    labelFormelBeggeRf.configure(text="")
    labelFormelBeggeCos.configure(text="")
    labelFormelBeggeSin.configure(text="")
    labelFormelBeggeVirkningsgrad.configure(text="")
    # Stjerne
    labelFormelStjerneUf.configure(text="")
    labelFormelStjerneR.configure(text="")
    labelFormelStjerneI.configure(text="")
    labelFormelStjerneIf.configure(text="")
    labelFormelStjerneP1.configure(text="")
    labelFormelStjerneP2.configure(text="")
    labelFormelStjerneQ.configure(text="")
    labelFormelStjerneS.configure(text="")
    # Trekant
    labelFormelTrekantUf.configure(text="")
    labelFormelTrekantR.configure(text="")
    labelFormelTrekantI.configure(text="")
    labelFormelTrekantIf.configure(text="")
    labelFormelTrekantP1.configure(text="")
    labelFormelTrekantP2.configure(text="")
    labelFormelTrekantQ.configure(text="")
    labelFormelTrekantS.configure(text="")

    labelFeil.grid_forget()
    labelKalkuleringGlad.grid_forget()
    knappReset.grid_forget()
    knappKalkuler.grid(row=32, column=varKolonne1, columnspan=3, sticky=N)


# Labels (Boks med tekst i) Entries (Boksene man skriver i)
# Linjene i programmet
for i in range(40):
    finKolonne = Label(root, font=("verdana", 3), bg=coll, width=1, height=3)
    finKolonne.grid(row=i+2, column=1, sticky=N + S + W)
for i in range(40):
    finKolonne = Label(root, font=("verdana", 3), bg=col)
    finKolonne.grid(row=i+2, column=0, sticky=N + S + W + E)

for i in range(50):
    finnKolonne = Label(root, font=("verdana", 2), bg=coll, width=10, height=0)
    finnKolonne.grid(row=1, column=i, sticky=W + E + S)
for i in range(50):
    finnKolonne = Label(root, font=("verdana", 2), bg=col, width=10, height=0)
    finnKolonne.grid(row=0, column=i, sticky=W + E + S + N)

# Tittelen for ZEK.
lTittel = Label(root, text="     Zuper Elektrizk Kalkulator (ZEK)", font=fontForTittel, fg=coll, bg=col)
lTittel.grid(row=0, column=0, columnspan=10, sticky=N + W)

# Labels for info
labelInfoTitle = Label(root, font=fontForOvertekstBigger, text="Zuper Elektrizk Kalkulator", fg="limeGreen")
labelInfoBeskrivelse = Label(root, text="Hei. Jeg heter ZEK, som står for Zuper Elektrizk Kalulator."
                                        "\nSkaperen min heter Ole Kristian Kåseth. "
                                        "\nHan programmerte meg for å regne ut elektriske formler,"
                                        "\nmen jeg kan bare finne det ut hvis jeg får nok informasjon (ᵔᴥᵔ)",
                             font=fontForLabelsBigger, fg="darkMagenta")
labelInfoSkaperen = Label(root, text="Vis du finner noen bugs eller feil med programmet ville det "
                                     "\nvært en stor hjelp vis du kunne sende en mail til skaperen min"
                                     "\nom hva slags bugs eller feil det er med programmet (ᵔᴥᵔ)",
                          font=fontForLabelsBigger, fg="red")
textInfoMail = Text(root, height=0.1, width=30)
textInfoMail.insert(1.0, "     ole.kristian.kaaseth@gmail.com")
textInfoMail.configure(bg=root.cget('bg'), relief=FLAT, state="disabled", fg="dodgerBlue", font=fontForLabelsBigger)

# Labels for mer orden
labelOrden = Label(root, width=1)

# Labels for trefase
# Labels for forklaring
labelForklaring1 = Label(root, text="Hei. Hvis du fyller inn så mye du kan, så fyller jeg inn så mye jeg kan. ",
                         font=fontForOvertekst, fg="darkMagenta")
labelForklaring2 = Label(root, text="Ikke fyll inn det du ikke vet (ᵔᴥᵔ)",
                         font=fontForOvertekst, fg="red")

# Labels for navnet til begge
labelBegge = Label(root, font=fontForOvertekst, text="Stjerne og trekant", fg="limeGreen")
labelBeggeHovedspenning = Label(root, font=fontForLabels, text="Hovedspenning")
labelBeggeFaseresistans = Label(root, font=fontForLabels, text="Faseresistans")
labelBeggeCosPhi = Label(root, font=fontForLabels, text="Cosinus phi")
labelBeggeSinPhi = Label(root, font=fontForLabels, text="Sinus phi")
labelBeggeVirkningsgrad = Label(root, font=fontForLabels, text="Virkningsgrad")

# Labels for symbolene til begge
labelBeggeStjerneTrekant = Label(root, font=fontForLabels, text="Y/Δ")
labelBeggeU = Label(root, font=fontForLabels, text="U")
labelBeggeRf = Label(root, font=fontForLabels, text="Rf")
labelBeggeCos = Label(root, font=fontForLabels, text="Cos")
labelBeggeSin = Label(root, font=fontForLabels, text="Sin")
labelBeggeV = Label(root, font=fontForLabels, text="η")

# Entries for begge
entryBeggeHovedspenning = Entry(root, textvariable=varBeggeU)
entryBeggeFaseresistans = Entry(root, textvariable=varBeggeRf)
entryBeggeCosPhi = Entry(root, textvariable=varBeggeCos)
entryBeggeSinPhi = Entry(root, textvariable=varBeggeSin)
entryBeggeVirkningsgrad = Entry(root, textvariable=varBeggeV)

# Labels for formlene til begge
labelFormelBeggeFormel = Label(root, font=fontForOvertekst, text="Formlene som ble brukt", fg="dodgerBlue")
labelFormelBeggeU = Label(root, font=fontForLabels)
labelFormelBeggeRf = Label(root, font=fontForLabels)
labelFormelBeggeCos = Label(root, font=fontForLabels)
labelFormelBeggeSin = Label(root, font=fontForLabels)
labelFormelBeggeVirkningsgrad = Label(root, font=fontForLabels)

# Labels for navnet til stjerne
labelStjerne = Label(root, font=fontForOvertekst, text="Stjerne", fg="limeGreen")
labelStjerneFasespenning = Label(root, font=fontForLabels, text="Fasespenning")
labelStjerneHovedresistans = Label(root, font=fontForLabels, text="Hovedresistans")
labelStjerneHovedstrom = Label(root, font=fontForLabels, text="Hovedstrøm")
labelStjerneFasestrom = Label(root, font=fontForLabels, text="Fasestrøm")
labelStjerneTilfortEffekt = Label(root, font=fontForLabels, text="Effekt (Tilført effekt)")
labelStjerneAvgittEffekt = Label(root, font=fontForLabels, text="Avgitt effekt")
labelStjerneReaktivEffekt = Label(root, font=fontForLabels, text="Reaktiv effekt")
labelStjerneTilsynelatendeEffekt = Label(root, font=fontForLabels, text="Tilsynelatende effekt")

# Labels for symbolene for stjerne
labelStjerneStjerne = Label(root, font=fontForLabels, text="Y")
labelStjerneUf = Label(root, font=fontForLabels, text="Uf")
labelStjerneR = Label(root, font=fontForLabels, text="R")
labelStjerneI = Label(root, font=fontForLabels, text="I")
labelStjerneIf = Label(root, font=fontForLabels, text="If")
labelStjerneP1 = Label(root, font=fontForLabels, text="P1")
labelStjerneP2 = Label(root, font=fontForLabels, text="P2")
labelStjerneQ = Label(root, font=fontForLabels, text="Q")
labelStjerneS = Label(root, font=fontForLabels, text="S")

# Entries for stjerne
entryStjerneFasespenning = Entry(root, textvariable=varStjerneUf)
entryStjerneHovedresistans = Entry(root, textvariable=varStjerneR)
entryStjerneHovedstrom = Entry(root, textvariable=varStjerneI)
entryStjerneFasestrom = Entry(root, textvariable=varStjerneIf)
entryStjerneTilfortEffekt = Entry(root, textvariable=varStjerneP1)
entryStjerneAvgittEffekt = Entry(root, textvariable=varStjerneP2)
entryStjerneReaktivEffekt = Entry(root, textvariable=varStjerneQ)
entryStjerneTilsynelatendeEffekt = Entry(root, textvariable=varStjerneS)

# Labels for formlene til stjerne
labelFormelStjerneUf = Label(root, font=fontForLabels)
labelFormelStjerneR = Label(root, font=fontForLabels)
labelFormelStjerneI = Label(root, font=fontForLabels)
labelFormelStjerneIf = Label(root, font=fontForLabels)
labelFormelStjerneP1 = Label(root, font=fontForLabels)
labelFormelStjerneP2 = Label(root, font=fontForLabels)
labelFormelStjerneQ = Label(root, font=fontForLabels)
labelFormelStjerneS = Label(root, font=fontForLabels)

# Labels for navnet til trekant
labelTrekant = Label(root, font=fontForOvertekst, text="Trekant", fg="limeGreen")
labelTrekantFasespenning = Label(root, font=fontForLabels, text="Fasespenning")
labelTrekantHovedresistans = Label(root, font=fontForLabels, text="Hovedresistans")
labelTrekantHovedstrom = Label(root, font=fontForLabels, text="Hovedstrøm")
labelTrekantFasestrom = Label(root, font=fontForLabels, text="Fasestrøm")
labelTrekantTilfortEffekt = Label(root, font=fontForLabels, text="Effekt (Tilført effekt)")
labelTrekantAvgittEffekt = Label(root, font=fontForLabels, text="Avgitt effekt")
labelTrekantReaktivEffekt = Label(root, font=fontForLabels, text="Reaktiv effekt")
labelTrekantTilsynelatendeEffekt = Label(root, font=fontForLabels, text="Tilsynelatende effekt")

# Labels for symbolene for trekant
labelTrekantTrekant = Label(root, font=fontForLabels, text="Δ")
labelTrekantUf = Label(root, font=fontForLabels, text="Uf")
labelTrekantR = Label(root, font=fontForLabels, text="R")
labelTrekantI = Label(root, font=fontForLabels, text="I")
labelTrekantIf = Label(root, font=fontForLabels, text="If")
labelTrekantP1 = Label(root, font=fontForLabels, text="P1")
labelTrekantP2 = Label(root, font=fontForLabels, text="P2")
labelTrekantQ = Label(root, font=fontForLabels, text="Q")
labelTrekantS = Label(root, font=fontForLabels, text="S")

# Entries for trekant
entryTrekantFasespenning = Entry(root, textvariable=varTrekantUf)
entryTrekantHovedresistans = Entry(root, textvariable=varTrekantR)
entryTrekantHovedstrom = Entry(root, textvariable=varTrekantI)
entryTrekantFasestrom = Entry(root, textvariable=varTrekantIf)
entryTrekantTilfortEffekt = Entry(root, textvariable=varTrekantP1)
entryTrekantAvgittEffekt = Entry(root, textvariable=varTrekantP2)
entryTrekantReaktivEffekt = Entry(root, textvariable=varTrekantQ)
entryTrekantTilsynelatendeEffekt = Entry(root, textvariable=varTrekantS)

# Labels for formlene til trekant
labelFormelTrekantUf = Label(root, font=fontForLabels)
labelFormelTrekantR = Label(root, font=fontForLabels)
labelFormelTrekantI = Label(root, font=fontForLabels)
labelFormelTrekantIf = Label(root, font=fontForLabels)
labelFormelTrekantP1 = Label(root, font=fontForLabels)
labelFormelTrekantP2 = Label(root, font=fontForLabels)
labelFormelTrekantQ = Label(root, font=fontForLabels)
labelFormelTrekantS = Label(root, font=fontForLabels)

# Buttons (Knapper)
knappInfo = Radiobutton(root, value=0, variable=knappVar, text="Info      ", fg="orangeRed", font=fontForKnapp,
                        command=lambda: commando(0), bg=col)
knappTrefase = Radiobutton(root, value=1, variable=knappVar, text="Trefase", fg="saddleBrown", font=fontForKnapp,
                           command=lambda: commando(1), bg=col)
knappKalkuler = Button(root, text="La meg regne resten", font=fontForOvertekst, command=kalkuler, fg="Green")
knappReset = Button(root, text="Reset", font=fontForOvertekst, command=nullstill, width=10, fg="Red")

# Grids for Buttons (Knapper)
knappInfo.grid(row=3, rowspan=2, column=0, sticky=W + S + N)
knappTrefase.grid(row=5, rowspan=2, column=0, sticky=W + S + N)

# Setter Cos og Virkningsgrad til 1
entryBeggeCosPhi.delete(0, END)
entryBeggeCosPhi.insert(0, 1.0)
entryBeggeVirkningsgrad.delete(0, END)
entryBeggeVirkningsgrad.insert(0, 1.0)


def commando(num):
    varRad10 = varRad1
    # Glemme grid for info
    labelInfoTitle.grid_forget()
    labelInfoBeskrivelse.grid_forget()
    labelInfoSkaperen.grid_forget()
    textInfoMail.grid_forget()

    # Glemme grid for Trefase
    # Glemme grid for beskrivelse
    labelForklaring1.grid_forget()
    labelForklaring2.grid_forget()
    labelFormelBeggeFormel.grid_forget()
    labelFeil.grid_forget()
    labelFormelBeggeFormel.grid_forget()
    labelKalkuleringGlad.grid_forget()
    labelOrden.grid_forget()

    # Glemme grid for stjerne of trekant
    labelBegge.grid_forget()
    labelBeggeHovedspenning.grid_forget()
    labelBeggeFaseresistans.grid_forget()
    labelBeggeCosPhi.grid_forget()
    labelBeggeSinPhi.grid_forget()
    labelBeggeVirkningsgrad.grid_forget()

    labelBeggeStjerneTrekant.grid_forget()
    labelBeggeU.grid_forget()
    labelBeggeRf.grid_forget()
    labelBeggeCos.grid_forget()
    labelBeggeSin.grid_forget()
    labelBeggeV.grid_forget()

    entryBeggeHovedspenning.grid_forget()
    entryBeggeFaseresistans.grid_forget()
    entryBeggeCosPhi.grid_forget()
    entryBeggeSinPhi.grid_forget()
    entryBeggeVirkningsgrad.grid_forget()

    labelFormelBeggeU.grid_forget()
    labelFormelBeggeRf.grid_forget()
    labelFormelBeggeCos.grid_forget()
    labelFormelBeggeSin.grid_forget()
    labelFormelBeggeVirkningsgrad.grid_forget()

    # Glemme grid for stjerne
    labelStjerne.grid_forget()
    labelStjerneFasespenning.grid_forget()
    labelStjerneHovedresistans.grid_forget()
    labelStjerneHovedstrom.grid_forget()
    labelStjerneFasestrom.grid_forget()
    labelStjerneTilfortEffekt.grid_forget()
    labelStjerneAvgittEffekt.grid_forget()
    labelStjerneReaktivEffekt.grid_forget()
    labelStjerneTilsynelatendeEffekt.grid_forget()

    labelStjerneStjerne.grid_forget()
    labelStjerneUf.grid_forget()
    labelStjerneR.grid_forget()
    labelStjerneI.grid_forget()
    labelStjerneIf.grid_forget()
    labelStjerneP1.grid_forget()
    labelStjerneP2.grid_forget()
    labelStjerneQ.grid_forget()
    labelStjerneS.grid_forget()

    entryStjerneFasespenning.grid_forget()
    entryStjerneHovedresistans.grid_forget()
    entryStjerneHovedstrom.grid_forget()
    entryStjerneFasestrom.grid_forget()
    entryStjerneTilfortEffekt.grid_forget()
    entryStjerneAvgittEffekt.grid_forget()
    entryStjerneReaktivEffekt.grid_forget()
    entryStjerneTilsynelatendeEffekt.grid_forget()

    labelFormelStjerneUf.grid_forget()
    labelFormelStjerneR.grid_forget()
    labelFormelStjerneI.grid_forget()
    labelFormelStjerneIf.grid_forget()
    labelFormelStjerneP1.grid_forget()
    labelFormelStjerneP2.grid_forget()
    labelFormelStjerneQ.grid_forget()
    labelFormelStjerneS.grid_forget()

    # Glemme grid for trekant
    labelTrekant.grid_forget()
    labelTrekantFasespenning.grid_forget()
    labelTrekantHovedresistans.grid_forget()
    labelTrekantHovedstrom.grid_forget()
    labelTrekantFasestrom.grid_forget()
    labelTrekantTilfortEffekt.grid_forget()
    labelTrekantAvgittEffekt.grid_forget()
    labelTrekantReaktivEffekt.grid_forget()
    labelTrekantTilsynelatendeEffekt.grid_forget()

    labelTrekantTrekant.grid_forget()
    labelTrekantUf.grid_forget()
    labelTrekantR.grid_forget()
    labelTrekantI.grid_forget()
    labelTrekantIf.grid_forget()
    labelTrekantP1.grid_forget()
    labelTrekantP2.grid_forget()
    labelTrekantQ.grid_forget()
    labelTrekantS.grid_forget()

    entryTrekantFasespenning.grid_forget()
    entryTrekantHovedresistans.grid_forget()
    entryTrekantHovedstrom.grid_forget()
    entryTrekantFasestrom.grid_forget()
    entryTrekantTilfortEffekt.grid_forget()
    entryTrekantAvgittEffekt.grid_forget()
    entryTrekantReaktivEffekt.grid_forget()
    entryTrekantTilsynelatendeEffekt.grid_forget()

    labelFormelTrekantUf.grid_forget()
    labelFormelTrekantR.grid_forget()
    labelFormelTrekantI.grid_forget()
    labelFormelTrekantIf.grid_forget()
    labelFormelTrekantP1.grid_forget()
    labelFormelTrekantP2.grid_forget()
    labelFormelTrekantQ.grid_forget()
    labelFormelTrekantS.grid_forget()

    # Glemme knapper
    knappKalkuler.grid_forget()
    knappReset.grid_forget()

    if num != 1 and num != 2 and num != 3:
        # Grid for info
        labelInfoTitle.grid(row=varRad10, rowspan=varRad10+1, column=varKolonne1, sticky=N)
        varRad10 = varRad10 + 2
        labelInfoBeskrivelse.grid(row=varRad10, rowspan=varRad10+3, column=varKolonne1, sticky=W + N)
        varRad10 = varRad10 + 4
        labelInfoSkaperen.grid(row=varRad10, rowspan=varRad10+1, column=varKolonne1, sticky=W + N)
        varRad10 = varRad10 + 3
        textInfoMail.grid(row=varRad10, column=varKolonne1, sticky=N)

    if num == 1:
        # Grid for trefase
        # Grid for beskrivelse
        labelForklaring1.grid(row=varRad10, column=varKolonne1, columnspan=10, sticky=W)
        varRad10 = varRad10 + 1
        labelForklaring2.grid(row=varRad10, column=varKolonne1, columnspan=10, sticky=W)

        # Grid for stjerne og trekant
        varRad10 = varRad10 + 2
        labelBegge.grid(row=varRad10, column=varKolonne1, sticky=W)
        labelBeggeStjerneTrekant.grid(row=varRad10, column=varKolonne2, sticky=N)
        labelOrden.grid(row=varRad10, column=varKolonne4, sticky=W)
        labelFormelBeggeFormel.grid(row=varRad10, column=varKolonne5, sticky=W)
        varRad10 = varRad10 + 1
        labelBeggeHovedspenning.grid(row=varRad10, column=varKolonne1, sticky=W)
        labelBeggeU.grid(row=varRad10, column=varKolonne2, sticky=N)
        entryBeggeHovedspenning.grid(row=varRad10, column=varKolonne3, sticky=W)
        labelFormelBeggeU.grid(row=varRad10, column=varKolonne5, sticky=W)
        varRad10 = varRad10 + 1
        labelBeggeFaseresistans.grid(row=varRad10, column=varKolonne1, sticky=W)
        labelBeggeRf.grid(row=varRad10, column=varKolonne2, sticky=N)
        entryBeggeFaseresistans.grid(row=varRad10, column=varKolonne3, sticky=W)
        labelFormelBeggeRf.grid(row=varRad10, column=varKolonne5, sticky=W)
        varRad10 = varRad10 + 1
        labelBeggeCosPhi.grid(row=varRad10, column=varKolonne1, sticky=W)
        labelBeggeCos.grid(row=varRad10, column=varKolonne2, sticky=N)
        entryBeggeCosPhi.grid(row=varRad10, column=varKolonne3, sticky=W)
        labelFormelBeggeCos.grid(row=varRad10, column=varKolonne5, sticky=W)
        varRad10 = varRad10 + 1
        labelBeggeSinPhi.grid(row=varRad10, column=varKolonne1, sticky=W)
        labelBeggeSin.grid(row=varRad10, column=varKolonne2, sticky=N)
        entryBeggeSinPhi.grid(row=varRad10, column=varKolonne3, sticky=W)
        labelFormelBeggeSin.grid(row=varRad10, column=varKolonne5, sticky=W)
        varRad10 = varRad10 + 1
        labelBeggeVirkningsgrad.grid(row=varRad10, column=varKolonne1, sticky=W)
        labelBeggeV.grid(row=varRad10, column=varKolonne2, sticky=N)
        entryBeggeVirkningsgrad.grid(row=varRad10, column=varKolonne3, sticky=W)
        labelFormelBeggeVirkningsgrad.grid(row=varRad10, column=varKolonne5, sticky=W)

        # grid for stjerne
        varRad10 = varRad10 + 2
        labelStjerne.grid(row=varRad10, column=varKolonne1, sticky=W)
        labelStjerneStjerne.grid(row=varRad10, column=varKolonne2, sticky=N)
        varRad10 = varRad10 + 1
        labelStjerneFasespenning.grid(row=varRad10, column=varKolonne1, sticky=W)
        labelStjerneUf.grid(row=varRad10, column=varKolonne2, sticky=N)
        entryStjerneFasespenning.grid(row=varRad10, column=varKolonne3, sticky=W)
        labelFormelStjerneUf.grid(row=varRad10, column=varKolonne5, sticky=W)
        varRad10 = varRad10 + 1
        labelStjerneHovedresistans.grid(row=varRad10, column=varKolonne1, sticky=W)
        labelStjerneR.grid(row=varRad10, column=varKolonne2, sticky=N)
        entryStjerneHovedresistans.grid(row=varRad10, column=varKolonne3, sticky=W)
        labelFormelStjerneR.grid(row=varRad10, column=varKolonne5, sticky=W)
        varRad10 = varRad10 + 1
        labelStjerneHovedstrom.grid(row=varRad10, column=varKolonne1, sticky=W)
        labelStjerneI.grid(row=varRad10, column=varKolonne2, sticky=N)
        entryStjerneHovedstrom.grid(row=varRad10, column=varKolonne3, sticky=W)
        labelFormelStjerneI.grid(row=varRad10, column=varKolonne5, sticky=W)
        varRad10 = varRad10 + 1
        labelStjerneFasestrom.grid(row=varRad10, column=varKolonne1, sticky=W)
        labelStjerneIf.grid(row=varRad10, column=varKolonne2, sticky=N)
        entryStjerneFasestrom.grid(row=varRad10, column=varKolonne3, sticky=W)
        labelFormelStjerneIf.grid(row=varRad10, column=varKolonne5, sticky=W)
        varRad10 = varRad10 + 1
        labelStjerneTilfortEffekt.grid(row=varRad10, column=varKolonne1, sticky=W)
        labelStjerneP1.grid(row=varRad10, column=varKolonne2, sticky=N)
        entryStjerneTilfortEffekt.grid(row=varRad10, column=varKolonne3, sticky=W)
        labelFormelStjerneP1.grid(row=varRad10, column=varKolonne5, sticky=W)
        varRad10 = varRad10 + 1
        labelStjerneAvgittEffekt.grid(row=varRad10, column=varKolonne1, sticky=W)
        labelStjerneP2.grid(row=varRad10, column=varKolonne2, sticky=N)
        entryStjerneAvgittEffekt.grid(row=varRad10, column=varKolonne3, sticky=W)
        labelFormelStjerneP2.grid(row=varRad10, column=varKolonne5, sticky=W)
        varRad10 = varRad10 + 1
        labelStjerneReaktivEffekt.grid(row=varRad10, column=varKolonne1, sticky=W)
        labelStjerneQ.grid(row=varRad10, column=varKolonne2, sticky=N)
        entryStjerneReaktivEffekt.grid(row=varRad10, column=varKolonne3, sticky=W)
        labelFormelStjerneQ.grid(row=varRad10, column=varKolonne5, sticky=W)
        varRad10 = varRad10 + 1
        labelStjerneTilsynelatendeEffekt.grid(row=varRad10, column=varKolonne1, sticky=W)
        labelStjerneS.grid(row=varRad10, column=varKolonne2, sticky=N)
        entryStjerneTilsynelatendeEffekt.grid(row=varRad10, column=varKolonne3, sticky=W)
        labelFormelStjerneS.grid(row=varRad10, column=varKolonne5, sticky=W)

        # grid for trekant
        varRad10 = varRad10 + 2
        labelTrekant.grid(row=varRad10, column=varKolonne1, sticky=W)
        labelTrekantTrekant.grid(row=varRad10, column=varKolonne2, sticky=N)
        varRad10 = varRad10 + 1
        labelTrekantFasespenning.grid(row=varRad10, column=varKolonne1, sticky=W)
        labelTrekantUf.grid(row=varRad10, column=varKolonne2, sticky=N)
        entryTrekantFasespenning.grid(row=varRad10, column=varKolonne3, sticky=W)
        labelFormelTrekantUf.grid(row=varRad10, column=varKolonne5, sticky=W)
        varRad10 = varRad10 + 1
        labelTrekantHovedresistans.grid(row=varRad10, column=varKolonne1, sticky=W)
        labelTrekantR.grid(row=varRad10, column=varKolonne2, sticky=N)
        entryTrekantHovedresistans.grid(row=varRad10, column=varKolonne3, sticky=W)
        labelFormelTrekantR.grid(row=varRad10, column=varKolonne5, sticky=W)
        varRad10 = varRad10 + 1
        labelTrekantHovedstrom.grid(row=varRad10, column=varKolonne1, sticky=W)
        labelTrekantI.grid(row=varRad10, column=varKolonne2, sticky=N)
        entryTrekantHovedstrom.grid(row=varRad10, column=varKolonne3, sticky=W)
        labelFormelTrekantI.grid(row=varRad10, column=varKolonne5, sticky=W)
        varRad10 = varRad10 + 1
        labelTrekantFasestrom.grid(row=varRad10, column=varKolonne1, sticky=W)
        labelTrekantIf.grid(row=varRad10, column=varKolonne2, sticky=N)
        entryTrekantFasestrom.grid(row=varRad10, column=varKolonne3, sticky=W)
        labelFormelTrekantIf.grid(row=varRad10, column=varKolonne5, sticky=W)
        varRad10 = varRad10 + 1
        labelTrekantTilfortEffekt.grid(row=varRad10, column=varKolonne1, sticky=W)
        labelTrekantP1.grid(row=varRad10, column=varKolonne2, sticky=N)
        entryTrekantTilfortEffekt.grid(row=varRad10, column=varKolonne3, sticky=W)
        labelFormelTrekantP1.grid(row=varRad10, column=varKolonne5, sticky=W)
        varRad10 = varRad10 + 1
        labelTrekantAvgittEffekt.grid(row=varRad10, column=varKolonne1, sticky=W)
        labelTrekantP2.grid(row=varRad10, column=varKolonne2, sticky=N)
        entryTrekantAvgittEffekt.grid(row=varRad10, column=varKolonne3, sticky=W)
        labelFormelTrekantP2.grid(row=varRad10, column=varKolonne5, sticky=W)
        varRad10 = varRad10 + 1
        labelTrekantReaktivEffekt.grid(row=varRad10, column=varKolonne1, sticky=W)
        labelTrekantQ.grid(row=varRad10, column=varKolonne2, sticky=N)
        entryTrekantReaktivEffekt.grid(row=varRad10, column=varKolonne3, sticky=W)
        labelFormelTrekantQ.grid(row=varRad10, column=varKolonne5, sticky=W)
        varRad10 = varRad10 + 1
        labelTrekantTilsynelatendeEffekt.grid(row=varRad10, column=varKolonne1, sticky=W)
        labelTrekantS.grid(row=varRad10, column=varKolonne2, sticky=N)
        entryTrekantTilsynelatendeEffekt.grid(row=varRad10, column=varKolonne3, sticky=W)
        labelFormelTrekantS.grid(row=varRad10, column=varKolonne5, sticky=W)
        varRad10 = varRad10 + 2
        # grid for kalkuler
        knappKalkuler.grid(row=varRad10, column=varKolonne1, columnspan=3, sticky=N)

    if num == 2:
        print(num)
    if num == 3:
        print(num)


commando(0)

mainloop()
