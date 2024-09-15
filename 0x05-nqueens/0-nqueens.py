#!/usr/bin/python3
import sys


def print_solution(solution):
    """Print the solution in the required format"""
    print([[i, solution[i]] for i in range(len(solution))])


def is_safe(solution, row, col):
    """Check if it's safe to place a queen at (row, col)"""
    for i in range(row):
        if solution[i] == col or \
           solution[i] - i == col - row or \
           solution[i] + i == col + row:
            return False
    return True


def solve_nqueens(N, row, solution):
    """Solve the N queens problem using backtracking"""
    if row == N:
        print_solution(solution)
    else:
        for col in range(N):
            if is_safe(solution, row, col):
                solution[row] = col
                solve_nqueens(N, row + 1, solution)


def main():
    """Main function to check arguments and solve the puzzle"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solution = [-1] * N
    solve_nqueens(N, 0, solution)


if __name__ == "__main__":
    main()
