import sys
from io_utils import load_file
from math_utils import is_diagonally_dominant
from jacobi_solver import solve_jacobi

def main():
    print("="*50)
    print("   ITERACYJNE ROZWIĄZYWANIE UKŁADÓW RÓWNAŃ   ")
    print("             (Metoda Jacobiego)             ")
    print("=" * 50)

    filepath = input("\nPodaj nazwę pliku z danymi (np. matrix, matrix2): ")
    A_full, b_full = load_file(filepath)

    if A_full is None or b_full is None:
        print("Koniec programu - popraw plik i spróbuj ponownie")
        sys.exit(1)

    max_n = A_full.shape[0]
    print(f"\n[INFO] Z pliku wczytano układ o maksymalnym rozmiarze {max_n}x{max_n}.")

    while True:
        try:
            n_str = input(f"Wybierz ilość równań do rozwiązania (1 do {max_n}): ")
            n = int(n_str)
            if 1 <= n <= max_n:
                break
            else:
                print(f"Błąd: Podaj liczbę z zakresu od 1 do {max_n}.")
        except ValueError:
            print("Błąd: To nie jest liczba całkowita!")

    A = A_full[:n, :n]
    b = b_full[:n]

    print(f"\nDziałamy na macierzy {n}x{n}. Sprawdzam warunek zbieżności...")

    if not is_diagonally_dominant(A):
        print("Błąd: Wybrana macierz nie jest silnie dominująca po przekątnej.")
        print("Oznacza to, że Metoda Jacobiego nie jest zbieżna. Program przerwany.")
        sys.exit(1)

    print("Macierz spełnia warunki zbieżności!")

    print("\nWybierz kryterium zatrzymania algorytmu:")
    print(" a) Spełnienie warunku dokładności (epsilon)")
    print(" b) Osiągnięcie zadanej liczby iteracji")

    while True:
        wybor = input("Twój wybór: ").strip().lower()
        if wybor in ['a','b']:
            break
        print("Błąd: Wybierz 'a' lub 'b'.")

    criterion = ''
    limit_value = 0.0

    if wybor == 'a':
        criterion = 'eps'
        while True:
            try:
                eps_str = input("Podaj wymaganą dokładność epsilon (np. 0.0001): ")
                limit_value = float(eps_str)
                if limit_value <= 0:
                    print("Błąd: Dokładność musi być większe od zera.")
                    continue
                break
            except ValueError:
                print("Błąd: Podaj prawidłową liczbę zmiennoprzecinkową.")

    else:
        criterion = 'iter'
        while True:
            try:
                iter_str = input("Podaj maksymalną liczbę iteracji (np. 10): ")
                limit_value = float(int(iter_str))
                if limit_value <= 0:
                    print("Błąd: Liczba iteracji musi być dodatnia.")
                    continue
                break
            except ValueError:
                print("Błąd: Podaj prawidłową liczbę całkowitą.")

    print("\n" + "-"*50)
    print("Rozpoczęcie obliczania...")

    rozwiazanie, liczba_iteracji = solve_jacobi(A, b, criterion, limit_value)

    print("\nWyniki: ")
    print(f"Ilość wykonanych iteracji: {liczba_iteracji}")
    print("Otrzymany wektor rozwiązań (x):")

    for i, val in enumerate(rozwiazanie):
        print(f"  x{i+1} = {val:.6f}")

    print("-"*50)

if __name__ == "__main__":
    main()