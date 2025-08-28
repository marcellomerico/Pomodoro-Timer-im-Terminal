
# Pomodoro Timer mit 4 Arbeitsphasen und 3 Pausenphasen
import time

def countdown(minutes):
    seconds = minutes * 60
    while seconds > 0:
        print(f"Verbleibende Zeit: {seconds // 60}:{seconds % 60:02d}", end='\r')
        time.sleep(1)
        seconds -= 1  
    print("\a")  # System Bell
    print("\nZeit ist um!")

def user_input():
    while True:
        try:
            minutes = int(input("Bitte hier eingeben: "))
            if 1 <= minutes <= 60:
                return minutes
            else:
                print("Bitte eine Zahl zwischen 1 und 60 eingeben.")
        except ValueError:
            print("Ungültige Eingabe. Bitte eine Zahl eingeben.")

  

def user_abfrage():
    print("Willkommen zum Pomodoro Timer!")

    print("Wie viele Arbeitsphasen willst du durchlaufen?")
    arbeitsphasen = user_input()

    print("Wie viele Pausenphasen willst du einlegen?")
    pausenphasen = user_input()

    print("Bitte gib die Dauer für Arbeits- und Pausenphasen ein.")
    arbeitszeit = user_input()
    
    print("Jetzt gib die Dauer für die Pausenphasen ein.")
    pausezeit = user_input()
    return arbeitszeit, pausezeit, arbeitsphasen, pausenphasen
   
def main():
    arbeitszeit, pausezeit, arbeitsphasen, pausenphasen = user_abfrage()
    
    for i in range(arbeitsphasen):
        print(f"\nArbeitsphase {i + 1} von {arbeitsphasen}")
        countdown(arbeitszeit)
        
        if i < pausenphasen:
            print(f"\nPausenphase {i + 1} von {pausenphasen}")
            countdown(pausezeit)
    
    print("Alle Phasen abgeschlossen! Gut gemacht!")


main()


