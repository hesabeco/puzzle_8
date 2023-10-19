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
                canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=str(cell_value), font=("Arial", 24))

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
    # Lógica del problema
    initial_puzzle = [[6, 2, 8], [4, 7, 1], [0, 3, 5]]
    br = main(initial_puzzle)

    print('Total steps: ', len(br) - 1)

    # Muestra el puzzle en una ventana Tkinter
    show_puzzle_in_window([b['node'] for b in br])

    

