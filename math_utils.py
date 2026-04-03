import numpy as np

def is_diagonally_dominant(A: np.ndarray) -> bool:
    """
    Sprawdza, czy macierz A jest diagonalnie dominująca (pozwala to
    określić zbieżność metody).
    Zwraca True, jeśli warunek jest spełniony, w przeciwnym razie False.
    """
    diagonal = np.abs(np.diag(A))

    row_sums = np.sum(np.abs(A), axis=1)

    off_diagonal_sums = row_sums - diagonal

    return np.all(diagonal > off_diagonal_sums)


if __name__ == "__main__":
    print("--- Testowanie modułu math_utils ---")

    A_good = np.array([
        [4, -1, -1],
        [-2, 6, 1],
        [-1, 1, 7]
    ])

    A_bad = np.array([
        [2, 5, 1],
        [1, 3, 1],
        [1, 1, 1]
    ])

    print("\nTest 1: Macierz poprawna (A_good)")
    print(f"Czy dominująca? {is_diagonally_dominant(A_good)}")

    print("\nTest 2: Macierz niepoprawna (A_bad)")
    print(f"Czy dominująca? {is_diagonally_dominant(A_bad)}")