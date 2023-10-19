import tkinter as tk
import time
from puzz_8 import main, print_puzzle

def draw_puzzle(canvas, puzzle):
    canvas.delete("all")
    canvas.create_text(150, 10, text="8-Puzzle Solver", font=("Arial", 16))

    # Dibuja el puzzle
    for row in range(3):
        for col in range(3):
            x0, y0 = col * 100, row * 100
            x1, y1 = x0 + 100, y0 + 100
            canvas.create_rectangle(x0, y0, x1, y1, outline="black", width=2)
            cell_value = puzzle[row][col]
            if cell_value != 0:
                label = canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=str(cell_value), font=("Arial", 24))
                canvas.itemconfig(label, tags=f"{row}-{col}")

def move_tile(row, col):
    global puzzle_state
    if puzzle_state[row][col] == 0:
        return  # No se puede mover la celda en blanco
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3 and puzzle_state[new_row][new_col] == 0:
            puzzle_state[row][col], puzzle_state[new_row][new_col] = puzzle_state[new_row][new_col], puzzle_state[row][col]
            draw_puzzle(canvas, puzzle_state)
            return

def solve_puzzle():
    br = main(puzzle_state)
    print('Total steps: ', len(br) - 1)
    show_puzzle_in_window([b['node'] for b in br])

def show_puzzle_in_window(puzzle_states):
    root = tk.Tk()
    root.title("8-Puzzle Solver")

    canvas = tk.Canvas(root, width=300, height=350)
    canvas.pack()

    for state in puzzle_states:
        draw_puzzle(canvas, state)
        root.update()
        time.sleep(1)  # Agrega un retraso de 1 segundo entre movimientos (ajusta según sea necesario)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("8-Puzzle Solver")

    puzzle_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Estado inicial en orden
    canvas = tk.Canvas(root, width=300, height=350)
    canvas.pack()
    draw_puzzle(canvas, puzzle_state)

    for row in range(3):
        for col in range(3):
            canvas.tag_bind(f"{row}-{col}", "<Button-1>", lambda event, row=row, col=col: move_tile(row, col))

    solve_button = tk.Button(root, text="Resolver", command=solve_puzzle)
    solve_button.pack()

    root.mainloop()
