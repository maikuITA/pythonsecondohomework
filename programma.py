# input: una sequenza di numeri con la virgola; chiamiamo R tale sequenza
path = r"D:\Documenti\Programs\programma\input.txt" # Percorso del file di input
file = open(path, 'r') # Apro il file in lettura
r = file.read().split(", ") # Leggo il file e lo divido in una lista di stringhe
file.close() # Chiudo il file
for i in range(len(r)): # Converto ogni elemento della lista in un float
    r[i] = float(r[i])
print("R:", r,"\n") # Stampo la lista R

# se R e' vuota, dare un messaggio d’errore senza effettuare altri calcoli;
if len(r) < 1 : 
    print("Errore: la lista e' vuota")
    exit() 
    
# se la lunghezza di R non e' pari, aggiungere uno zero alla fine
if(len(r)%2 != 0):
    r.append(0)
indice = int(len(r)/2) # Calcolo l'indice di mezzo della lista r

# scissione della strinnga in P ed S
p = r.copy()[:indice]
s = r.copy()[indice:]
print("P:", p,"\n") # Stampo la lista P
print("S:", s,"\n") # Stampo la lista S

o = 0 # Inizializzo l'output a 0 (dato che si tratta di una somma)
for(i, j) in zip(p, s): # Scorro le liste p e s
    o += i*((100-j)/100) # Applico lo sconto e sommo
print("O:", o) # Stampo l'output
    
# output: considerando R come composta da 2 sottosequenze P ed S, calcolare la spesa totale derivante 
#         dall’applicare uno-a-uno gli sconti in S ai prezzi in P.
path = r"D:\Documenti\Programs\programma\output.txt" # Percorso del file di output
file = open(path, 'w') # Apro il file in scrittura
r = file.write(str(o)) # Scrivo l'output nel file
file.close() # Chiudo il file

# maiku