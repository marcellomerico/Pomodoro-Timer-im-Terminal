
# Pomodoro Timer mit 4 Arbeitsphasen und 3 Pausenphasen
import time

def countdown(minutes):
    seconds = minutes * 60
    while seconds > 0:
        print(f"Verbleibende Zeit: {seconds // 60}:{seconds % 60:02d}", end='\r')
        time.sleep(1)
        seconds -= 1  
    print("\nZeit ist um!")

def user_input():
    while True:
        try:
            minutes = int(input("Gib die Anzahl der Minuten ein (1-60): "))
            if 1 <= minutes <= 60:
                return minutes
            else:
                print("Bitte eine Zahl zwischen 1 und 60 eingeben.")
        except ValueError:
            print("Ungültige Eingabe. Bitte eine Zahl eingeben.")
         

print("Willkommen zum Pomodoro Timer!")
print("Du wirst 4 Arbeitsphasen und 3 Pausenphasen durchlaufen.")
print("Bitte gib die Dauer für Arbeits- und Pausenphasen ein.")
arbeitszeit = user_input()
print("Jetzt gib die Dauer für die Pausenphasen ein.")
pausezeit = user_input()

print("Fokus beginnt jetzt, viel Erfolg!")
countdown(arbeitszeit)
print("Erste kurze Pause, entspann dich!")
countdown(pausezeit)
print("Zurück zur Arbeit, du schaffst das!")
countdown(arbeitszeit)
print("Zweite kurze Pause, tief durchatmen!")
countdown(pausezeit)
print("Letzte Arbeitsphase, gib alles!")
countdown(arbeitszeit)
print("Große Pause, genieße deine Zeit!")
countdown(pausezeit)
print("Pomodoro-Zyklus abgeschlossen! Gute Arbeit!")
