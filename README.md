# Installation

1. python -m venv venv eller python3 -m venv venv
1. aktivera den virtuella miljön
1. pip install -r requirements.txt eller pip3 install -r requirements.txt


# Övningar
Ni kommer att ha användning av dessa tester i er hotellapp så jag rekommenderar att ni gör dem.

Jag har lagt in vissa testfall att lösa och ni kan lägga till fler utöver dessa för att komplettera.

Tänk på att er app = era regler. Så länge ni är tydliga för slutanvändaren vad som gäller vid validering är det ok att ha business rules som är "speciella".

1. Namnvalidering: Lägg till validering för för- och efternamn. I verkliga livet kan folk heta precis vad som helst. Jag ger förslag på enkla regler ni kan implementera:
- Inga siffor eller specialtecken (',.!). OBS! Bindestreck (-) är tillåtet. Britt-Marie är till exempelt ett giltigt namn.
- Det kortaste förnamnet jag kan komma på är Bo eller My, så en rimlig gräns kanske kan vara minst 2 tecken i längd. 
- Maxgränsen blir den gräns ni har i er databaskolumn.
- Tillåt bara svenska tecken (a-ö, stora och små)
- Ett namn kan inte sluta på ett specialtecken (Britt- går ej) eller mellanslag
- Ska mellanrum tillåtas? Ni måste isåfall kolla att ett namn inte endast består av mellanrum ("     " ska inte fungera tex)

2. E-postvalidering: denna validering är egentligen otroligt komplex men för att öva kan vi till exempel säga:
- En e-post måste innehålla @ och .com eller .se
- Någonting måste finnas framför @
- Endast engelska tecken (a-z) och siffror

Om ni undrar varför e-postvalidering är så komplext så är detta en giltig mail enligt spec:

!#$%&'*+-/=.?^_`{|}~@[IPv6:0123:4567:89AB:CDEF:0123:4567:89AB:CDEF]

medan detta är en ogiltig epost:

@example.com

3. Datumvalidering: hotellet måste hantera datum för bokningar.
- Valideringen bör ta in datumen som strängar enligt "YYYY-MM-DD". Det finns inbyggt i python. Se validate_dates för att se hur den funkar.
- Startdatum måste vara minst en dag i framtiden
- Slutdatum måste vara minst en dag efter startdatum

