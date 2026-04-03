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

