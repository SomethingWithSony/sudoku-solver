def print_board(board):
  line = ""
  v = 0
  h = 0
  for row in board:

    if h == 3:
      print(" ")
      h = 0

    for col in row:
      v += 1
      if v == 3:
        line += str(col) + "  "
        v = 0
      else:
        line += str(col) + " "

    print(line)
    line = ""
    h += 1


def find_zero(board):
  for row in range(len(board)):
    for col in range(len(board[row])):
      if board[row][col] == 0:
        return [row, col]


def is_valid_placement(board, row, col, value):
  # Check Same Row
  if value in board[row]:
    return False

  # Check Same Column
  if value in [board[i][col] for i in range(len(board))]:
    return False

  # Get Quadrant
  start_row, start_col = 3 * (row // 3), 3 * (col // 3)

  # Check 3x3
  for i in range(start_row, start_row + 3):
    for j in range(start_col, start_col + 3):
      if board[i][j] == value:
        return False

  # Return true if all checks pass
  return True


def solve(board):
  empty_cell = find_zero(board)
  if not empty_cell:
    return board  # Board is solved

  row, col = empty_cell

  for num in range(1, 10):
    if is_valid_placement(board, row, col, num):
      board[row][col] = num

      if solve(board):
        return board  # If a solution is found, return it

      board[row][
          col] = 0  # If the current assignment does not lead to a solution, backtrack

  return None  # If no solution is found for any number, backtrack to the previous empty cell
