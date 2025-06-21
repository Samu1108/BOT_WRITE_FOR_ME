import pyautogui
import time
import random

# === CONFIGURAZIONI ===
PAUSA_INIZIALE = 5  # Tempo per mettere il cursore su VS Code
FREQUENZA_ERRORI = 0.015  # ~1.5% errori di battitura
PAUSA_BASE = (0.07, 0.22)  # Intervallo normale tra tasti
PAUSA_LUNGA = (1.5, 4.0)  # Pausa lunga (pensiero)
PAUSA_CRUCIALE = {
    '.': (0.5, 1.2),
    ',': (0.4, 0.9),
    ':': (0.6, 1.1),
    ';': (0.6, 1.2),
    '\n': (1.0, 2.5),
    '“': (0.8, 1.6),
    '”': (0.8, 1.6),
    '(': (0.7, 1.3),
    ')': (0.7, 1.3)
}

# === TESTO ===
with open("testo.txt", "r", encoding="utf-8") as f:
    testo = f.read()

print(f"Hai {PAUSA_INIZIALE} secondi per posizionare il cursore su VS Code...")
time.sleep(PAUSA_INIZIALE)

def simula_digitazione(carattere):
    """Simula la scrittura di un carattere con pause umane"""
    # Pausa cruciale su punteggiatura e momenti logici
    if carattere in PAUSA_CRUCIALE:
        time.sleep(random.uniform(*PAUSA_CRUCIALE[carattere]))
    elif random.random() < 0.01:  # Pausa casuale (stanchezza, pensiero)
        time.sleep(random.uniform(*PAUSA_LUNGA))
    else:
        time.sleep(random.uniform(*PAUSA_BASE))

    # Possibilità di errore umano (es. tasto vicino sbagliato)
    if random.random() < FREQUENZA_ERRORI and carattere.isalpha():
        errore = random.choice('abcdefghijklmnopqrstuvwxyz')
        pyautogui.write(errore)
        time.sleep(random.uniform(0.05, 0.15))
        pyautogui.press('backspace')
        time.sleep(random.uniform(0.05, 0.2))

    # Scrivi il carattere reale
    pyautogui.write(carattere)

# === DIGITAZIONE ===
for c in testo:
    simula_digitazione(c)
