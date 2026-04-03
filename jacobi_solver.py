import numpy as np

def solve_jacobi(A: np.ndarray, b: np.ndarray, criterion: str, limit_value: float) -> tuple[np.ndarray, int]:
    """
    Rozwiązuje układ równań Ax = b metodą Jacobiego.
    Występują dwa kryteria stopu:
    - criterion == 'iter': wykonuje 'limit_value' iteracji.
    - criterion == 'eps': wykonuje pętle dopóki nie zostanie osiągnięta określona tolerancja ('limit_value').
    """
    x = np.zeros_like(b)
    D = np.diag(A)
    R = A - np.diagflat(D)

    iterations = 0

    #Kryterium stopu nr 1: Z góry zadana liczba iteracji
    if criterion == 'iter':
        max_iter = int(limit_value)
        for _ in range(max_iter):
            x_new = (b - np.dot(R, x)) / D
            x = x_new
            iterations += 1

    #Kryterium stopu nr 2: Z góry zadana dokładność
    elif criterion == 'eps':
        tolerance = float(limit_value)
        error = float('inf')

        while error >= tolerance:
            x_new = (b - np.dot(R, x)) / D
            error = np.max(np.abs(x_new - x))
            x = x_new
            iterations += 1

            if iterations > 1000:
                print("Ostrzeżenie: Przekroczono 1000 iteracji, wymuszone przerwanie!")
                break

    else:
        raise ValueError("Nieznane kryterium. Wybierz 'iter' lub 'eps'.")

    return x, iterations


if __name__ == "__main__":
    print("--- Testowanie modułu jacobi_solver ---")

    A = np.array([
        [4, -1, -1],
        [-2, 6, 1],
        [-1, 1, 7]
    ])
    b = np.array([3, 9, -6])

    print("\nTest KRYTERIUM A: Dokładność (eps = 0.0001)")
    rozw_eps, iter_eps = solve_jacobi(A, b, criterion='eps', limit_value=0.0001)
    print(f"Wynik: {rozw_eps}")
    print(f"Ilość wykonanych iteracji do osiągnięcia dokładności: {iter_eps}")

    print("\nTest KRYTERIUM B: Stała liczba iteracji (iter = 5)")
    rozw_iter, iter_iter = solve_jacobi(A, b, criterion='iter', limit_value=5)
    print(f"Wynik: {rozw_iter}")
    print(f"Ilość wykonanych iteracji: {iter_iter}")