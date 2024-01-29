correct_count = 0
wrong_count = 0

def show_title_screen():
    print("EZgoingQuiz")
    input("Drücke die 'Eingabe-Taste' zum STARTEN")
    return
show_title_screen()

def get_player_name():
    name = input("Gebe deinen Namen ein. Das Quiz startet mit Eingabe der 'Enter-Taste': ")
    return name

player_name = get_player_name()

def level_1(correct_answers, wrong_answers):
    global wrong_count
    print("Level 1: Was ist die Hauptstadt von Frankreich?")
    print("a) Berlin")
    print("b) Madrid")
    print("c) Paris")
    print("d) Rom")

    user_input = input("Deine Antwort (a-d): ").lower()

    if user_input == "c":
        print("\nRichtig! Du erhältst 1 Punkt.")
        correct_answers += 1
    else:
        print("\nFalsch! Die richtige Antwort ist c) Paris.")
        wrong_answers += 1
        wrong_count += 1

    print(f"Aktuelle Anzahl richtiger Antworten: {correct_answers}")
    print(f"Aktuelle Anzahl falscher Antworten: {wrong_answers}")

    if wrong_count >= 3:  
        end_game(player_name, correct_answers)
        show_results()
        import sys
        sys.exit()
    
    return correct_answers, wrong_answers

def level_2(correct_answers, wrong_answers):
    global wrong_count
    print("Level 2: Was ist die größte Insel der Welt?")
    print("a) Hawaii")
    print("b) Borneo")
    print("c) Grönland")
    print("d) Island")

    user_input = input("Deine Antwort (a-d): ").lower()

    if user_input == "c":
        print("\nRichtig! Du erhältst 1 Punkt.")
        correct_answers += 1
    else:
        print("\nFalsch! Die richtige Antwort ist c) Grönland.")
        wrong_answers += 1
        wrong_count += 1

    print(f"Aktuelle Anzahl richtiger Antworten: {correct_answers}")
    print(f"Aktuelle Anzahl falscher Antworten: {wrong_answers}")

    if wrong_count >= 3:  
        end_game(player_name, correct_answers)
        show_results()
        import sys
        sys.exit()
    
    return correct_answers, wrong_answers

def level_3(correct_answers, wrong_answers):
    global wrong_count
    print("Level 3: Welches Element hat das chemische Symbol 'O'?")
    print("a) Sauerstoff")
    print("b) Kohlenstoff")
    print("c) Wasserstoff")
    print("d) Stickstoff")

    user_input = input("Deine Antwort (a-d): ").lower()

    if user_input == "a":
        print("\nRichtig! Du erhältst 1 Punkt.")
        correct_answers += 1
    else:
        print("\nFalsch! Die richtige Antwort ist a) Sauerstoff.")
        wrong_answers += 1
        wrong_count += 1

    print(f"Aktuelle Anzahl richtiger Antworten: {correct_answers}")
    print(f"Aktuelle Anzahl falscher Antworten: {wrong_answers}")

    if wrong_count >= 3:  
        end_game(player_name, correct_answers)
        show_results()
        import sys
        sys.exit()
    
    return correct_answers, wrong_answers
        
    


def level_4(correct_answers, wrong_answers):
    global wrong_count
    print("Level 4: In welchem Jahr fand die erste bemannte Mondlandung statt?")
    print("a) 1969")
    print("b) 1972")
    print("c) 1981")
    print("d) 1955")

    user_input = input("Deine Antwort (a-d): ").lower()

    if user_input == "a":
        print("\nRichtig! Du erhältst 1 Punkt.")
        correct_answers += 1
    else:
        print("\nFalsch! Die richtige Antwort ist a) 1969.")
        wrong_answers += 1
        wrong_count += 1

    print(f"Aktuelle Anzahl richtiger Antworten: {correct_answers}")
    print(f"Aktuelle Anzahl falscher Antworten: {wrong_answers}")

    if wrong_count >= 3:  
        end_game(player_name, correct_answers)
        show_results()
        import sys
        sys.exit()
    
    return correct_answers, wrong_answers

def level_5(correct_answers, wrong_answers):
    global wrong_count
    print("Level 5: Wer schrieb das Buch 'Die Odyssee'?\na) Homer\nb) Plato\nc) Herodot\nd) Sappho")
    user_input = input("Deine Antwort (a-d): ").lower()

    if user_input == "a":
        print("\nRichtig! Du erhältst 1 Punkt.")
        correct_answers += 1
    else:
        print("\nFalsch! Die richtige Antwort ist a) Homer.")
        wrong_answers += 1
        wrong_count += 1

    print(f"Aktuelle Anzahl richtiger Antworten: {correct_answers}")
    print(f"Aktuelle Anzahl falscher Antworten: {wrong_answers}")

    if wrong_count >= 3:  
        end_game(player_name, correct_answers)
        show_results()
        import sys
        sys.exit()
    
    return correct_answers, wrong_answers

def level_6(correct_answers, wrong_answers):
    global wrong_count
    print("Level 6: Welcher Planet ist der fünfte in unserem Sonnensystem?\na) Mars\nb) Jupiter\nc) Saturn\nd) Erde")
    user_input = input("Deine Antwort (a-d): ").lower()

    if user_input == "b":
        print("\nRichtig! Du erhältst 1 Punkt.")
        correct_answers += 1
    else:
        print("\nFalsch! Die richtige Antwort ist b) Jupiter.")
        wrong_answers += 1
        wrong_count += 1

    print(f"Aktuelle Anzahl richtiger Antworten: {correct_answers}")
    print(f"Aktuelle Anzahl falscher Antworten: {wrong_answers}")

    if wrong_count >= 3:  
        end_game(player_name, correct_answers)
        show_results()
        import sys
        sys.exit()
    
    return correct_answers, wrong_answers

def level_7(correct_answers, wrong_answers):
    global wrong_count
    print("Level 7: Welches Tier ist der größte lebende Fisch?\na) Walhai\nb) Blauwal\nc) Hammerhai\nd) Makohai")
    user_input = input("Deine Antwort (a-d): ").lower()

    if user_input == "a":
        print("\nRichtig! Du erhältst 1 Punkt.")
        correct_answers += 1
    else:
        print("\nFalsch! Die richtige Antwort ist a) Walhai.")
        wrong_answers += 1
        wrong_count += 1

    print(f"Aktuelle Anzahl richtiger Antworten: {correct_answers}")
    print(f"Aktuelle Anzahl falscher Antworten: {wrong_answers}")

    if wrong_count >= 3:  
        end_game(player_name, correct_answers)
        show_results()
        import sys
        sys.exit()
    
    return correct_answers, wrong_answers

def level_8(correct_answers, wrong_answers):
    global wrong_count
    print("Level 8: In welchem Jahr begann der Erste Weltkrieg?\na) 1901\nb) 1914\nc) 1923\nd) 1939")
    user_input = input("Deine Antwort (a-d): ").lower()

    if user_input == "b":
        print("\nRichtig! Du erhältst 1 Punkt.")
        correct_answers += 1
    else:
        print("\nFalsch! Die richtige Antwort ist b) 1914.")
        wrong_answers += 1
        wrong_count += 1

    print(f"Aktuelle Anzahl richtiger Antworten: {correct_answers}")
    print(f"Aktuelle Anzahl falscher Antworten: {wrong_answers}")

    if wrong_count >= 3:  
        end_game(player_name, correct_answers)
        show_results()
        import sys
        sys.exit()
    
    return correct_answers, wrong_answers

def level_9(correct_answers, wrong_answers):
    global wrong_count
    print("Level 9: Was ist die chemische Formel für Wasser?\na) H2O\nb) CO2\nc) CH4\nd) N2O")
    user_input = input("Deine Antwort (a-d): ").lower()

    if user_input == "a":
        print("\nRichtig! Du erhältst 1 Punkt.")
        correct_answers += 1
    else:
        print("\nFalsch! Die richtige Antwort ist a) H2O.")
        wrong_answers += 1
        wrong_count += 1

    print(f"Aktuelle Anzahl richtiger Antworten: {correct_answers}")
    print(f"Aktuelle Anzahl falscher Antworten: {wrong_answers}")

    if wrong_count >= 3:  
        end_game(player_name, correct_answers)
        show_results()
        import sys
        sys.exit()
    
    return correct_answers, wrong_answers

def level_10(correct_answers, wrong_answers):
    global wrong_count
    print("Level 10: Wie viele Kontinente hat die Erde?\na) 5\nb) 6\nc) 7\nd) 8")
    user_input = input("Deine Antwort (a-d): ").lower()

    if user_input == "c":
        print("\nRichtig! Du erhältst 1 Punkt.")
        correct_answers += 1
    else:
        print("\nFalsch! Die richtige Antwort ist c) 7.")
        wrong_answers += 1
        wrong_count += 1

    print(f"Aktuelle Anzahl richtiger Antworten: {correct_answers}")
    print(f"Aktuelle Anzahl falscher Antworten: {wrong_answers}")

    if wrong_count >= 3:  
        end_game(player_name, correct_answers)
        show_results()
        import sys
        sys.exit()
    
    return correct_answers, wrong_answers

def show_results():
    print("\nErgebnisse:")
    with open("ergebnisse.txt", "r") as file:
        results = file.readlines()

        results.sort(key=lambda x: int(x.split(":")[-1].strip().split()[0]), reverse=True)

        for i, line in enumerate(results[:7], start=1):
            print(f"{i}. {line.strip()}")

def end_game(name, correct_answers):
    print(f"\nDas Spiel ist beendet, {name}!")

    results = []
    with open("ergebnisse.txt", "r") as file:
        results = file.readlines()

    results.append(f"{name}: {correct_answers} Punkte\n")

    with open("ergebnisse.txt", "w") as file:
        file.writelines(results)

    print("Ergebnisse wurden gespeichert.")
    
    


correct_count, wrong_count = level_1(correct_count, wrong_count)
correct_count, wrong_count = level_2(correct_count, wrong_count)
correct_count, wrong_count = level_3(correct_count, wrong_count)
correct_count, wrong_count = level_4(correct_count, wrong_count)
correct_count, wrong_count = level_5(correct_count, wrong_count)
correct_count, wrong_count = level_6(correct_count, wrong_count)
correct_count, wrong_count = level_7(correct_count, wrong_count)
correct_count, wrong_count = level_8(correct_count, wrong_count)
correct_count, wrong_count = level_9(correct_count, wrong_count)
correct_count, wrong_count = level_10(correct_count, wrong_count)

end_game(player_name, correct_count)
show_results()
