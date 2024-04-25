import matplotlib.pyplot as plt

år = []
startår = 1991
antall_år = 29
for i in range(antall_år):
    år.append(startår)
    startår+=1
# over lager jeg en liste med årene 

def antall_innbyggere_norge(): # Dette er en funksjon som retunerer antall inbyggere i norge fra 1991 til 2019
    populasjonstall = [
        4249830, 4273634, 4299167, 4324815, 4348410, 4369957, 4392714, 4417599,
        4445329, 4478497, 4503436, 4524066, 4552252, 4577457, 4606363, 4640219,
        4681134, 4737171, 4799252, 4858199, 4920305, 4985870, 5051275, 5109056,
        5165802, 5213985, 5258317, 5295619, 5328212
    ]
    return populasjonstall

def antall_innbyggere_kina(): # Dette er en funksjon som retunerer antall inbyggere i Kina fra 1991 til 2019
    populasjonstall = [1170626171,1183813389,1195855558,1207286675,1218144426,1228298836,1237801448,1246836105 ,1255433236
        ,1264099069,1272739582,1280926120,1288873367,1296816711,1304887562,1313086567,1321513224,1330167148,1339125595,1348191368,1357095481,1366560818,1376100308,1385189668,1393715448,1401889681,1410275957,1417069468,1421864031]
    return populasjonstall

def eksport_kina(): # Dette er en funksjon som retunerer eksport per inbygger fra Kina. Her har jeg måtte dele tallene på antall inbyggere for å få data per inbygger.
    eksport_fra_kina_milliarder_us_dollar = [51.511461986063,57.870749262166,
    53.3583402067,104.60692734068,131.8585628586,154.81234251143,187.44666313891,188.75134412844,
    198.69939964002,253.09196235431,272.06105136662,333.00402080112,447.95626936532,607.3568729786,773.33743247657,
    991.72661988774,1258.0514214169,1497.878483246,1262.6611941413,1654.8233226466,2006.3088595814,2175.0693143332,
    2354.2644081048,2462.8257669718,2362.0971773121,2199.97491004,2424.2160211315,2655.6091048984,2628.9411008792,
    ]
    tusen_us_dollar_per_innbygger = []
    antall_innbyggere = antall_innbyggere_kina()

    for i in range(len(eksport_fra_kina_milliarder_us_dollar)):
        tusen_us_dollar_per_innbygger.append((eksport_fra_kina_milliarder_us_dollar[i] * 1_000_000)/antall_innbyggere[i])
    
    return tusen_us_dollar_per_innbygger

def eksport_norge(): # Dette er en funksjon som retunerer eksport per inbygger fra Norge. Her har jeg måtte dele tallene på antall inbyggere for å få data per inbygger.
    eksport_norge_tusen_us_dollar_91_19 = "34743529,47	34743529,47	31903872,54	34743529,47	41740320,77	48954961,92	48549838,85	40401838,08	45479329,79	60337044,46	59219407,25	59624111,56	67913165,67	82399847,44	103804221,8	122080570,5	135689374,7	168998885,2	116295912,6	130656792,4	160409821,5	160952207,4	155350552,8	144611289,8	103785482,3	89628326,85	101976020,2	123040316,9	104029881,5"
    verdier_liste = eksport_norge_tusen_us_dollar_91_19.split('\t') 
    eksport_norge_tusen_us_dollar_91_19 = [float(value.replace(',', '.')) for value in verdier_liste] # Erstatt komma med punktum og konverter til desimaltall

    antall_innbyggere = antall_innbyggere_norge()
    eksport = []
    for i in range(len(eksport_norge_tusen_us_dollar_91_19)):
        eksport.append(eksport_norge_tusen_us_dollar_91_19[i]/antall_innbyggere[i])
    return eksport

print(eksport_kina())
print(eksport_norge())

def utslipp_kina(): #Retunerer co2 utslipp per inbygger fra Kina
    utslipp_karbondioksid_kina_per_innbygger = [
        2.1, 2.2, 2.3, 2.4, 2.6, 2.7, 2.7, 2.6, 2.5, 2.6, 2.6,
        2.9, 3.4, 3.9, 4.3, 4.8, 5.1, 5.4, 5.7, 6.2, 6.8,
        7.0, 7.0, 7.0, 6.9, 6.8, 6.9, 7.0, 7.1
    ]
    return utslipp_karbondioksid_kina_per_innbygger

def utslipp_norge(): #Retunerer co2 utslipp per inbygger fra Norge
    utslipp_karbondioksid_norge_per_innbygger = [
        7.9, 8.1, 8.4, 8.8, 8.9, 9.5, 9.5, 9.5, 9.6, 9.4, 9.7, 9.5, 9.7, 9.7,
        9.5, 9.5, 9.8, 9.5, 9.1, 9.5, 9.2, 9.0, 8.9, 8.7, 8.7, 8.5, 8.2, 8.2, 7.9
    ]
    return utslipp_karbondioksid_norge_per_innbygger

def bnp_norge(): #Retunerer BNP per inbygger i Norge
    bnp_per_person_norge = ["28596.9330036444","30523.9850558974","27963.6979095744","29315.8092337732","34875.7043347536","37321.9741993473","36629.0309036621","34803.4634058738","36393.2927471088","38178.2368777076","38601.897639231","43170.557174499","50250.3298214345","57768.6980958462","67047.1704558264","74434.4996835671","85502.2677087731","97503.5407803783","80347.5700665184","88163.2085931423","101221.813476644","102175.919298374","103553.840134417","97666.6951838749","74809.9658049898","70867.3609970749","76131.8384032764","82792.8427113304","76430.5889473338"]                               
    return bnp_per_person_norge
def bnp_kina(): # Retunerer BNP per inbygger i Kina
    bnp_per_person_kina = ["15465.9245305858","17976.4688629053","20395.5621886121","22502.5302426236","23497.3920767477","24818.3021600084","27330.0933613355","25808.8609899709","25091.6665997966","25756.7728723704","25230.3780910304","24665.8362318216","23977.1734120477","24928.1003722551","26649.637724155","28224.0951563146","30593.9511738646","31515.5292103443","30697.5383861641","32550.136489179","35142.4879344543","36730.796195815","38403.7777145477","40315.3739510191","42432.1619740441","43734.1980702999","46160.429791493","48537.5668888343","48359.0011950597"]
    return bnp_per_person_kina

# Lager plottet for alle fire grafene
fig, ax1 = plt.subplots()
# lager grafer for utslipp
ax1.plot(år, utslipp_norge(), label="CO2-utslipp Norge", color="red")
ax1.plot(år, utslipp_kina(), label="CO2-utslipp Kina", color="blue")
ax1.set_xlabel('År')
ax1.set_ylabel('Utslipp av co2 per innbygger')
ax1.legend()
#under lager jeg grafer for eksport for hver av landene. Dette gjør at jeg kan ha to separate y akser med forskjellige verdier.
ax2 = ax1.twinx()
ax2.plot(år, eksport_norge(), label="Eksport fra Norge", color="orange")
ax2.plot(år, eksport_kina(), label="Eksport fra Kina", color="lightblue")
ax2.set_ylabel('Eksport per innbygger 1000 us-dollar')
ax2.legend()
plt.title("")
plt.show()

# Lager plottet for eksport og utslipp i Norge
fig, ax1 = plt.subplots()
ax1.plot(år, utslipp_norge(), label="CO2-utslipp fra Norge per innbygger", color="red")
ax1.plot(år, eksport_norge(), label="Eksport fra Norge per innbygger 1000 us-dollar", color="orange")
ax1.set_xlabel('År')
ax1.set_ylabel('CO2 utslipp/Eksport')
ax1.legend()
plt.title("Norge")
plt.show()

# Lagre plottet for eksport og utslipp i Kina
fig, ax1 = plt.subplots()
ax1.plot(år, utslipp_kina(), label="CO2-utslipp fra Kina per innbygger", color="red")
ax1.plot(år, eksport_kina(), label="Eksport fra Kina per innbygger 1000 us-dollar", color="orange")
ax1.set_xlabel('År')
ax1.set_ylabel('CO2 utslipp/Eksport')
ax1.legend()
plt.title("Kina")
plt.show()

# Lager plottet for eksport og utslipp i Norge
fig, ax1 = plt.subplots()
ax1.plot(år, utslipp_norge(), label="CO2-utslipp", color="red")
ax1.set_xlabel('År')
ax1.set_ylabel('Utslipp av CO2 per innbygger')
ax1.legend(loc='upper left')  # Plasser legenden øverst til venstre
ax2 = ax1.twinx()
ax2.plot(år, eksport_norge(), label="Eksport fra Norge", color="orange")
ax2.set_ylabel('Eksport per innbygger 1000 us-dollar')
ax2.legend(loc='upper right')  # Plasser legenden øverst til høyre
plt.title("Norge")
plt.show()

# Lagre plottet for eksport og utslipp i Kina
fig, ax1 = plt.subplots()
ax1.plot(år, utslipp_kina(), label="CO2-utslipp fra Kina", color="red")
ax1.set_xlabel('År')
ax1.set_ylabel('Utslipp av CO2 per innbygger')
ax1.legend()
ax2 = ax1.twinx()
ax2.plot(år, eksport_kina(), label="Eksport fra Kina", color="orange")
ax2.set_ylabel('Eksport per innbygger 1000 us-dollar')
ax2.legend(loc='lower right')  # Plasser legenden øverst til høyre

plt.title("Kina")
plt.show()
