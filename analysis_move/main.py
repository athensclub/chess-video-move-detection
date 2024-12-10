import chess

def analysis_move(fen_positions):
    # Initialize the board
    board = chess.Board()

    # List to store moves in SAN format
    san_moves = []

    # Iterate through FEN positions
    for i in range(len(fen_positions) - 1):
        board.set_fen(fen_positions[i])  # Set the current board position
        next_board = chess.Board(fen_positions[i + 1])  # Set the next board position
        
        # Find the move that leads to the next position
        correct_move = None
        for move in board.legal_moves:
            board.push(move)
            if board.fen() == fen_positions[i + 1]:
                correct_move = move
                board.pop()  # Undo the move
                break
            board.pop()  # Undo the move if not matching
        
        if correct_move:
            san_moves.append(board.san(correct_move))  # Append the correct move in SAN format
            board.push(correct_move)  # Apply the correct move to the board

    # Join moves into a single string
    result_string = " ".join(san_moves)
    # print(result_string)
    return result_string

def main(fen_positions):
    return analysis_move(fen_positions)

# test_case
test_case = [
    "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
    "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1",
    "rnbqkbnr/pppp1ppp/8/4p3/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2",
    "rnbqkbnr/pppp1ppp/B7/4p3/4P3/8/PPPP1PPP/RNBQK1NR b KQkq - 1 2",
    "rnbqkbnr/p1pp1ppp/p7/4p3/4P3/8/PPPP1PPP/RNBQK1NR w KQkq - 0 3",
    "rnbqkbnr/p1pp1ppp/p7/4p3/4P3/2N5/PPPP1PPP/R1BQK1NR b KQkq - 1 3",
    "rnbqkbnr/p1p2ppp/p7/3pp3/4P3/2N5/PPPP1PPP/R1BQK1NR w KQkq - 0 4",
    "rnbqkbnr/p1p2ppp/p7/3Np3/4P3/8/PPPP1PPP/R1BQK1NR b KQkq - 0 4",
    "rnb1kbnr/p1p2ppp/p7/3qp3/4P3/8/PPPP1PPP/R1BQK1NR w KQkq - 0 5",
    "rnb1kbnr/p1p2ppp/p7/3Pp3/8/8/PPPP1PPP/R1BQK1NR b KQkq - 0 5",
    "rnb2bnr/p1pk1ppp/p7/3Pp3/8/8/PPPP1PPP/R1BQK1NR w KQ - 1 6",
    "rnb2bnr/p1pk1ppp/p7/3Pp3/6Q1/8/PPPP1PPP/R1B1K1NR b KQ - 2 6",
    "rnb2bnr/p1p2ppp/p2k4/3Pp3/6Q1/8/PPPP1PPP/R1B1K1NR w KQ - 3 7",
    "rnQ2bnr/p1p2ppp/p2k4/3Pp3/8/8/PPPP1PPP/R1B1K1NR b KQ - 0 7",
    "r1Q2bnr/p1pn1ppp/p2k4/3Pp3/8/8/PPPP1PPP/R1B1K1NR w KQ - 1 8",
    "Q4bnr/p1pn1ppp/p2k4/3Pp3/8/8/PPPP1PPP/R1B1K1NR b KQ - 0 8",
    "Q5nr/p1pnbppp/p2k4/3Pp3/8/8/PPPP1PPP/R1B1K1NR w KQ - 1 9",
    "6nr/p1pnbppp/p1Qk4/3Pp3/8/8/PPPP1PPP/R1B1K1NR b KQ - 2 9"
]

