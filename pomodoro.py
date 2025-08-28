
# Pomodoro Timer mit 4 Arbeitsphasen und 3 Pausenphasen
import time

def countdown(minutes):
    seconds = minutes * 60
    while seconds > 0:
        print(f"Verbleibende Zeit: {seconds // 60}:{seconds % 60:02d}", end='\r')
        time.sleep(1)
        seconds -= 1  
    print("\nZeit ist um!")


print("Fokus beginnt jetzt, viel Erfolg!")
countdown(25)
print("Erste kurze Pause, entspann dich!")
countdown(5)
print("Zurück zur Arbeit, du schaffst das!")
countdown(25)
print("Zweite kurze Pause, tief durchatmen!")
countdown(5)
print("Letzte Arbeitsphase, gib alles!")
countdown(25)
print("Große Pause, genieße deine Zeit!")
countdown(15)
print("Pomodoro-Zyklus abgeschlossen! Gute Arbeit!")
