import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv") #sau putem înlocui cu calea reală a fișierului

X=7  #Zaharia
Y=14 #Andrei Cristian

plt.figure(figsize=(10, 6))
plt.plot(data['Durata'], label='Durata', marker='o')
plt.plot(data['Puls'], label='Puls', marker='x')
plt.plot(data['MaxPuls'], label='MaxPuls', marker='*')
plt.plot(data['Calorii'], label='Calorii', marker='D')
plt.title('Toate valorile')
plt.xlabel('Index')
plt.ylabel('Valori')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(data['Durata'][:X], label='Durata', marker='o')  #primele x valori
plt.plot(data['Puls'][:X], label='Puls', marker='x')
plt.plot(data['MaxPuls'][:X], label='MaxPuls', marker='*')
plt.plot(data['Calorii'][:X], label='Calorii', marker='D')
plt.title(f'Primele {X} valori')
plt.xlabel('Index')
plt.ylabel('Valori')
plt.legend()
plt.grid(True)
plt.show()


plt.figure(figsize=(10, 6))
plt.plot(data['Durata'][-Y:], label='Durata', marker='o')   #ultimele y valori pt Durata si Puls 
plt.plot(data['Puls'][-Y:], label='Puls', marker='x')
plt.title(f'Ultimele {Y} valori pentru Durata si Puls')
plt.xlabel('Index')
plt.ylabel('Valori')
plt.legend()
plt.grid(True)
plt.show()