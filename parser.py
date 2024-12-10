fuck = f"""Frame 1: https://lichess.org/editor/1r2k2q/p1p1n3/3p2pb/P2Pp3/1pP1P1QP/3B2P1/PR6/4KR2
Frame 2: https://lichess.org/editor/1r2k2q/p1p1n3/3p2pb/P2Pp3/1pP1P1QP/3B2P1/PR6/4KR2
Frame 3: https://lichess.org/editor/1r2k2q/p1p1n3/3p2pb/P2Pp3/1pP1P1QP/3B2P1/PR6/4KR2
Frame 4: https://lichess.org/editor/1r2k2q/p1p1n3/3p2pb/P2Pp3/1pP1P1NN/3B2P1/PR6/4KR1n
Frame 5: https://lichess.org/editor/1r2k2q/p1p1n3/3p2pb/P2PpQ2/1pP1PNQN/3B4/PR6/4KR1n
Frame 6: https://lichess.org/editor/1r2k2q/p1p1n3/3p2pb/P2PpQ2/1pP1P1NP/3B1PN1/PR6/4KR1n
Frame 7: https://lichess.org/editor/8/1r2k2q/p1p1n3/3pQ1pb/P2PpQ2/1pP1P2P/3B2P1/PR3NP1
Frame 8: https://lichess.org/editor/1r2k2q/p1p1n3/3pQ1pb/P2Pp3/1pP1P2P/3B2P1/PR6/4KR2
Frame 9: https://lichess.org/editor/8/1r2k2q/p1p1n3/3pQ1pb/P2Pp3/1pP1P2P/3B2P1/PR6
Frame 10: https://lichess.org/editor/1r2k2q/p1p1n3/3pQ1pb/P2Pp3/1pP1P2P/3B2P1/PR6/4KR2
Frame 11: https://lichess.org/editor/1r2k2q/p1p1n3/3pQ1pb/P2Pp3/1pP1P2P/3B2P1/PR6/4KR2
Frame 12: https://lichess.org/editor/1r2k2q/p1p1n3/3pQ1pb/P2Pp3/1pP1P2P/3B2P1/PR6/4KR2
Frame 13: https://lichess.org/editor/1r2k2q/p1p1n3/3pQ1pb/P2Pp3/1pP1P2P/3B2P1/PR6/4KR2
Frame 14: https://lichess.org/editor/1r2k2q/p1p1n3/3pQ1pb/P2Pp3/1pP1P2P/3B2P1/PR6/4KR2
Frame 15: https://lichess.org/editor/1r2k2q/p1p1n3/3pQ1pb/P2Pp3/1pP1P2P/3B2P1/PR6/4KR2
Frame 16: https://lichess.org/editor/1r1k3q/p1p1n3/3pN1pb/P2PpN2/1pP1q2P/3B1RP1/PR3p2/4K3
Frame 17: https://lichess.org/editor/1r1k3q/p1p1nN2/3p1PNb/P2PpnQ1/1pP1PnPP/3B1QP1/PR6/4KN2
Frame 18: https://lichess.org/editor/1r1k3q/p1p1nQ2/3p2pb/P2Pp3/1pP1P2P/3B2P1/PR6/4KR2
Frame 19: https://lichess.org/editor/1r1k3q/p3nQ2/2pp2Nb/P2PpQQ1/1pP1P2P/3B4/PR4P1/4KR2
Frame 20: https://lichess.org/editor/1r1k3q/p3n3/2pp2pb/P2Pp3/1pP1P2P/3B2P1/PR3Nn1/4KRnQ
Frame 21: https://lichess.org/editor/1r1k3q/4n3/P1pp2pb/P2Pp3/1pP1P2P/3B2P1/PR3Q2/4KR2
Frame 22: https://lichess.org/editor/1r1k3q/p3n3/3p2pb/P2pp3/1pP1P2P/3B2P1/PR2QQ2/3p1R2
Frame 23: https://lichess.org/editor/1r1k3q/p3n3/3p2pb/P2pp3/pQN1P2P/3B2P1/1R6/4KR2
Frame 24: https://lichess.org/editor/1r1k3q/Q3n3/3p2pb/P2pp3/1pP1P2P/3B2P1/PR6/4KR1Q
Frame 25: https://lichess.org/editor/1r1k3q/Q3n3/3p2pb/P2pp3/1pP1P2P/3B2P1/PR6/4KR2
Frame 26: https://lichess.org/editor/1r1k3q/Q3n3/3p2pb/P2pp3/1pP1P2P/3B2P1/PR6/4KR2
Frame 27: https://lichess.org/editor/2rk3q/Q3n3/3p2pb/P2pp3/1pP1P2P/3B2P1/PR6/4KR2
Frame 28: https://lichess.org/editor/2rk3q/Q3n3/3p2pb/P2pp3/1pP1P2P/3B2P1/PR6/4KR2
Frame 29: https://lichess.org/editor/2rk3q/Q3n3/3p2pb/P2pp3/1pP1P2P/3B2P1/PR6/4KR2
Frame 30: https://lichess.org/editor/2rk3q/Q3n3/3p2pb/P2pp3/1pP1P2P/3B2P1/PR6/4KR2
Frame 31: https://lichess.org/editor/2rk3q/Q3n3/6pb/P2pp3/1RP1P2P/3B2P1/P7/4KR2
Frame 32: https://lichess.org/editor/2rk3q/K7/3p2pb/P2pp3/1R2P2P/3B2P1/P7/4KR2"""


fuck = fuck.replace("https://lichess.org/editor/", "").replace(" ", "").replace("Frame", "").replace("\\n")

print(fuck.split(":")[1::2])


