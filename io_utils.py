import numpy as np

def load_file(filepath: str) -> tuple[np.ndarray, np.ndarray] | tuple[None, None]:
    """
    Wczytuje macierz współczynników A i wektor wyrazów wolnych b z pliku.
    """
    try:
        data = np.loadtxt(filepath)

        A = data[:, :-1]
        b = data[:, -1]

        if A.shape[0] != A.shape[1]:
            raise ValueError("Macierz A nie jest kwadratowa! Sprawdź format danych w pliku.")

        return A, b

    except FileNotFoundError:
        print(f"Błąd: Nie znaleziono pliku '{filepath}'.")
        return None, None
    except Exception as e:
        print(f"Błąd podczas wczytywania danych: {e}")
        return None, None


if __name__ == "__main__":
    print("--- Testowanie modułu io_utils ---")

    filepath = "data.txt"
    A, b = load_file(filepath)

    if A is not None and b is not None:
        print("\nSukces! Dane wczytane prawidłowo.")
        print("Macierz współczynników A:")
        print(A)
        print("\nWektor wyrazów wolnych b:")
        print(b)
    else:
        print("\nNie udało się wczytać danych. Sprawdź błędy powyżej.")