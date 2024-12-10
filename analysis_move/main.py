from unittest import TestCase
from itertools import chain
import re

import chess
import chess.pgn


def parse(fen_str):
    ranks = fen_str.split(" ")[0].split("/")
    pieces_on_all_ranks = [parse_rank(rank) for rank in ranks]
    return pieces_on_all_ranks

def parse_rank(rank):
    rank_re = re.compile("(\d|[kqbnrpKQBNRP])")
    piece_tokens = rank_re.findall(rank)
    pieces = flatten(map(expand_or_noop, piece_tokens))
    return pieces

def flatten(lst):
    return list(chain(*lst))

def expand_or_noop(piece_str):
    piece_re = re.compile("([kqbnrpKQBNRP])")
    retval = ""
    if piece_re.match(piece_str):
        retval = piece_str
    else:
        retval = expand(piece_str)
    return retval

def expand(num_str):
    return int(num_str)*" "


def test_parse_rank():
    start_pos = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    rank8 = "rnbqkbnr"
    rank7 = "pppppppp"
    rank6 = "8"
    fp = parse(start_pos)
    assert fp.parse_rank(rank8) == ["r","n","b","q","k","b","n","r"]
    assert fp.parse_rank(rank7) == ["p","p","p","p","p","p","p","p"]
    assert fp.parse_rank(rank6) == [" "," "," "," "," "," "," "," "]

def test_parse_starting_position(pos):
    start_pos = pos
    fp = parse(start_pos)
    return fp

cols = ["a", "b", "c", "d", "e", "f", "g", "h"]
rows = ["8", "7", "6", "5", "4", "3", "2", "1"]

def get_state(a, b, c):
    if a == "p" or a == 'P':
        a = ""
    return a.upper() + cols[c] + rows[b]

def check_specific_case(frame_a, frame_b, point_a, point_b):
    character = frame_b[point_b[0]][point_b[1]]

    dx = []
    dy = []
    if character == "N" or character == "n":
        dx = [-2, -1, 1, 2, -2, -1, 1, 2]
        dy = [-1 ,-2, -2, -1, 1, 2, 2, 1]
        
        cnt = 0
        for i in range(len(dx)):
            if point_b[0] + dx[i] < 0 or point_b[0] + dx[i] > 7 or point_b[1] + dy[i] < 0 or point_b[1] + dy[i] > 7:
                continue

            point_c = [point_b[0] + dx[i], point_b[1] + dy[i]]
            if frame_a[point_c[0]][point_c[1]] == character:
                cnt += 1

        if cnt == 2:
            return cols[point_a[1]]
        return ""

    elif character == "R" or character == 'r':
        dx = [
            [-1, -2, -3, -4, -5, -6, -7],
            [1, 2, 3, 4, 5, 6, 7]
        ]
        dy = [
            [0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0]
        ]

        cnt = 0
        for i in range(len(dx)):
            for j in range(len(dx[0])):
                if point_b[0] + dx[i][j] < 0 or point_b[0] + dx[i][j] > 7 or point_b[1] + dy[i][j] < 0 or point_b[1] + dy[i][j] > 7:
                    continue

                point_c = [point_b[0] + dx[i][j], point_b[1] + dy[i][j]]
                if frame_a[point_c[0]][point_c[1]] == character:
                    cnt += 1
                    break
        if cnt == 2:
            return rows[point_a[0]]
                
        dx = [
            [0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0]
        ]
        dy = [
            [-1, -2, -3, -4, -5, -6, -7],
            [1, 2, 3, 4, 5, 6, 7]
        ]

        cnt = 0
        for i in range(len(dx)):
            for j in range(len(dx[0])):
                if point_b[0] + dx[i][j] < 0 or point_b[0] + dx[i][j] > 7 or point_b[1] + dy[i][j] < 0 or point_b[1] + dy[i][j] > 7:
                    continue

                point_c = [point_b[0] + dx[i][j], point_b[1] + dy[i][j]]
                if frame_a[point_c[0]][point_c[1]] == character:
                    cnt += 1
                    break
        if cnt == 2:
            return cols[point_a[1]]
        
        dx = [
            [0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0],
            [-1, -2, -3, -4, -5, -6, -7],
            [1, 2, 3, 4, 5, 6, 7]
        ]
        dy = [
            [-1, -2, -3, -4, -5, -6, -7],
            [1, 2, 3, 4, 5, 6, 7],
            [0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0],
        ]

        cnt = 0
        for i in range(len(dx)):
            for j in range(len(dx[0])):
                if point_b[0] + dx[i][j] < 0 or point_b[0] + dx[i][j] > 7 or point_b[1] + dy[i][j] < 0 or point_b[1] + dy[i][j] > 7:
                    continue

                point_c = [point_b[0] + dx[i][j], point_b[1] + dy[i][j]]
                if frame_a[point_c[0]][point_c[1]] == character:
                    cnt += 1
                    break
        if cnt == 2:
            return cols[point_a[1]]
    return ""

def get_move(frame_a, frame_b, point_a, point_b):
    move = get_state(frame_b[point_b[0]][point_b[1]] ,point_b[0], point_b[1])
        
    if frame_a[point_b[0]][point_b[1]] != ' ':
        if frame_a[point_a[0]][point_a[1]] == "p" or frame_a[point_a[0]][point_a[1]] == "P":
            move = cols[point_a[1]] + "x" + move
            if move[0] == move[2]:
                move = move[:2] + move[3:]
        else:
            move = frame_a[point_a[0]][point_a[1]].upper() + "x" + move
            if move[0] == move[2]:
                move = move[:2] + move[3:]

    move = move[:1] + check_specific_case(frame_a, frame_b, [point_a[0], point_a[1]], [point_b[0], point_b[1]]) + move[1:]
    return move

def replace_king(frame, charector):
    temp = [[], [], []]
    for i in range(0, len(frame)):
        for j in range(0, len(frame[0])):
            if frame[i][j] == charector[0]:
                temp[0].append([i, j])
            elif frame[i][j] == charector[1]:
                temp[1].append([i, j])
            elif frame[i][j] == charector[2]:
                temp[2].append([i, j])
    
    if len(temp[0]) == 0:
        if len(temp[1]) > 0:
            frame[temp[1][0][0]][temp[1][0][1]] = charector[0]
        elif len(temp[2]) > 0:
            frame[temp[2][0][0]][temp[2][0][1]] = charector[0]

def some_shit(frame):
    replace_king(frame, ['k', 'q', 'r'])
    replace_king(frame, ['K', 'Q', 'R'])
        
def get_pgn(frame_a, frame_b):
    frame_a = test_parse_starting_position(frame_a)
    frame_b = test_parse_starting_position(frame_b)
    some_shit(frame_a)
    some_shit(frame_b)
    points = list()

    for i in range(0, len(frame_a)):
        for j in range(0, len(frame_b)):
            if frame_a[i][j] != frame_b[i][j]:
                points.append([i, j])

    if len(points) == 0 or len(points) > 2: return "not_change"

    if frame_b[points[0][0]][points[0][1]] == ' ':
        move = get_move(frame_a, frame_b, points[0], points[1])
    else:
        move = get_move(frame_a, frame_b, points[1], points[0])
    return move

def check_mate(pgn_input):
    # Input PGN without annotations
    # pgn_input = "1. e4 e5 2. Ba6 bxa6 3. Nc3 d5 4. Nxd5 Qxd5 5. exd5 Kd7 6. Qg4 Kd6 7. Qxc8 Nd7 8. Qxa8 Be7 9. Qc6"

    # Parse moves
    moves = pgn_input.replace(".", "").split()

    # Initialize a chess board
    board = chess.Board()

    # Annotate moves
    annotated_moves = []
    for move in moves:
        try:
            chess_move = board.parse_san(move)
            board.push(chess_move)
            if board.is_checkmate():
                annotated_moves.append(f"{move}#")
            elif board.is_check():
                annotated_moves.append(f"{move}+")
            else:
                annotated_moves.append(move)
        except ValueError:
            annotated_moves.append(move)  # In case of invalid move, keep as-is

    # Reconstruct the PGN with annotations
    annotated_pgn = " ".join(annotated_moves)

    # Output
    # print(annotated_pgn)
    return annotated_pgn

def transform_chess_notation(input_moves):
    # Split the input into individual moves
    moves = input_moves.split(" ")
    
    # Filter out any existing numbering
    moves = [move for move in moves if not move.isdigit()]
    
    # Initialize variables for the output string and move counter
    formatted_moves = ""
    move_counter = 1
    
    # Loop through the moves, adding the move counter for every two moves
    for i in range(0, len(moves), 2):
        if i + 1 < len(moves):
            formatted_moves += f"{move_counter}. {moves[i]} {moves[i+1]} "
        else:
            formatted_moves += f"{move_counter}. {moves[i]} "
        move_counter += 1
    
    # Remove the trailing space and return the result
    return formatted_moves.strip()

def main(frame):
    state = "white"
    num = 1
    ans = ""
    for i in range(1, len(frame)):
        state_change = get_pgn(frame[i-1], frame[i])
        if state_change == "not_change":
            continue
        if state == "white":
            state = "black"
            a = state_change
            ans += str(num) + ". " + a + " "
        elif state == "black":
            state = "white"
            b = state_change
            ans += b + " "
            num += 1
    ans = check_mate(ans)
    return transform_chess_notation(ans)