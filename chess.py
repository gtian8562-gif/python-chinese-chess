# ==========================================
# 1. 初始化棋盤 (10 行 x 9 列)
# ==========================================
board = [[0 for _ in range(9)] for _ in range(10)]

# 擺放黑棋 (Row 0 ~ 3)
board[0] = ["車", "馬", "象", "士", "將", "士", "象", "馬", "車"]
board[2][1], board[2][7] = "砲", "砲"
board[3][0], board[3][2], board[3][4], board[3][6], board[3][8] = (
    "卒",
    "卒",
    "卒",
    "卒",
    "卒",
)

# 擺放紅棋 (Row 6 ~ 9)
board[9] = ["俥", "傌", "相", "仕", "帥", "仕", "相", "傌", "俥"]
board[7][1], board[7][7] = "炮", "炮"
board[6][0], board[6][2], board[6][4], board[6][6], board[6][8] = (
    "兵",
    "兵",
    "兵",
    "兵",
    "兵",
)


# ==========================================
# 2. 畫出帶座標的棋盤與輔助函式
# ==========================================
def print_board(board):
    print("\n  0 1 2 3 4 5 6 7 8")
    print(" ------------------")
    for r in range(10):
        print(f"{r}|", end="")
        for c in range(9):
            piece = board[r][c]
            print(". " if piece == 0 else f"{piece}", end="")
        print()


def is_same_team(p1, p2):
    """判斷兩個棋子是否屬於同一方"""
    if p1 == 0 or p2 == 0:
        return False
    red_pieces = ["帥", "仕", "相", "傌", "俥", "炮", "兵"]
    black_pieces = ["將", "士", "象", "馬", "車", "砲", "卒"]

    is_p1_red = p1 in red_pieces
    is_p2_red = p2 in red_pieces
    return is_p1_red == is_p2_red


def get_jiang_shuai_pos(board):
    """搜尋將與帥的位置"""
    jiang_pos, shuai_pos = None, None
    for r in range(0, 3):
        for c in range(3, 6):
            if board[r][c] == "將":
                jiang_pos = (r, c)
    for r in range(7, 10):
        for c in range(3, 6):
            if board[r][c] == "帥":
                shuai_pos = (r, c)
    return jiang_pos, shuai_pos


def is_flying_general(board):
    """飛將（將帥對照）檢查"""
    jiang, shuai = get_jiang_shuai_pos(board)
    if not jiang or not shuai or jiang[1] != shuai[1]:
        return False
    col = jiang[1]
    for row in range(jiang[0] + 1, shuai[0]):
        if board[row][col] != 0:
            return False
    return True  # 同路且中間無棋子，違規！


# ==========================================
# 3. 棋子移動規則判斷
# ==========================================
def is_valid_move(piece, from_r, from_c, to_r, to_c):
    if from_r == to_r and from_c == to_c:
        return False
    if piece == 0:
        return False

    target_piece = board[to_r][to_c]
    if is_same_team(piece, target_piece):
        return False

    dr = abs(to_r - from_r)
    dc = abs(to_c - from_c)

    # 1. 士 / 仕
    if piece in ["士", "仕"]:
        in_black_palace = (0 <= to_r <= 2) and (3 <= to_c <= 5)
        in_red_palace = (7 <= to_r <= 9) and (3 <= to_c <= 5)
        if not (in_black_palace or in_red_palace):
            return False
        return dr == 1 and dc == 1

    # 2. 將 / 帥
    if piece in ["將", "帥"]:
        in_black_palace = (0 <= to_r <= 2) and (3 <= to_c <= 5)
        in_red_palace = (7 <= to_r <= 9) and (3 <= to_c <= 5)
        if not (in_black_palace or in_red_palace):
            return False
        return (dr == 1 and dc == 0) or (dr == 0 and dc == 1)

    # 3. 象 / 相
    if piece in ["象", "相"]:
        if dr == 2 and dc == 2:
            if piece == "象" and to_r > 4:
                return False
            if piece == "相" and to_r < 5:
                return False
            mid_r = (from_r + to_r) // 2
            mid_c = (from_c + to_c) // 2
            if board[mid_r][mid_c] != 0:
                return False
            return True
        return False

    # 4. 馬 / 傌
    if piece in ["馬", "傌"]:
        if (dr == 2 and dc == 1) or (dr == 1 and dc == 2):
            if dr == 2:
                leg_r = from_r + (1 if to_r > from_r else -1)
                leg_c = from_c
            else:
                leg_r = from_r
                leg_c = from_c + (1 if to_c > from_c else -1)
            if board[leg_r][leg_c] != 0:
                return False
            return True
        return False

    # 5. 車 / 俥
    if piece in ["車", "俥"]:
        if from_r != to_r and from_c != to_c:
            return False
        count = 0
        if from_r == to_r:
            step = 1 if to_c > from_c else -1
            for c in range(from_c + step, to_c, step):
                if board[from_r][c] != 0:
                    count += 1
        else:
            step = 1 if to_r > from_r else -1
            for r in range(from_r + step, to_r, step):
                if board[r][from_c] != 0:
                    count += 1
        return count == 0

    # 6. 炮 / 砲
    if piece in ["炮", "砲"]:
        if from_r != to_r and from_c != to_c:
            return False
        count = 0
        if from_r == to_r:
            step = 1 if to_c > from_c else -1
            for c in range(from_c + step, to_c, step):
                if board[from_r][c] != 0:
                    count += 1
        else:
            step = 1 if to_r > from_r else -1
            for r in range(from_r + step, to_r, step):
                if board[r][from_c] != 0:
                    count += 1
        if target_piece == 0:
            return count == 0
        else:
            return count == 1

    # 7. 兵 / 卒
    if piece == "兵":
        if to_r > from_r:
            return False
        if from_r >= 5:
            return dr == 1 and dc == 0
        else:
            return (dr == 1 and dc == 0) or (dr == 0 and dc == 1)

    if piece == "卒":
        if to_r < from_r:
            return False
        if from_r <= 4:
            return dr == 1 and dc == 0
        else:
            return (dr == 1 and dc == 0) or (dr == 0 and dc == 1)

    return False


# ==========================================
# 4. 遊戲主迴圈
# ==========================================
current_player = "red"
red_pieces = ["帥", "仕", "相", "傌", "俥", "炮", "兵"]
black_pieces = ["將", "士", "象", "馬", "車", "砲", "卒"]

while True:
    print_board(board)

    player_name = "🔴 紅方" if current_player == "red" else "⚫ 黑方"
    print(f"\n【當開啟回合：{player_name}】")
    user_input = input("請輸入指令 (例如 6050，或輸入 q 退出)：").strip()

    if user_input.lower() == "q":
        print("遊戲結束！")
        break

    if len(user_input) == 4 and user_input.isdigit():
        from_r = int(user_input[0])
        from_c = int(user_input[1])
        to_r = int(user_input[2])
        to_c = int(user_input[3])

        piece = board[from_r][from_c]

        if piece == 0:
            print("\n❌ 選取的起點沒有棋子！")
            continue

        if current_player == "red" and piece not in red_pieces:
            print("\n⚠️ 現在是紅方的回合，不能走黑棋！")
            continue
        if current_player == "black" and piece not in black_pieces:
            print("\n⚠️ 現在是黑方的回合，不能走紅棋！")
            continue

        if is_valid_move(piece, from_r, from_c, to_r, to_c):
            target_piece = board[to_r][to_c]

            board[to_r][to_c] = piece
            board[from_r][from_c] = 0

            if is_flying_general(board):
                print("\n⚠️ 違規！將帥不能照面！移動已取消！")
                board[from_r][from_c] = piece
                board[to_r][to_c] = target_piece
            else:
                action_text = (
                    f"吃了 {target_piece}" if target_piece != 0 else "移動"
                )
                print(
                    f"\n✅ {player_name} {piece} {action_text} 至 ({to_r},{to_c})"
                )
                current_player = (
                    "black" if current_player == "red" else "red"
                )
        else:
            print("\n❌ 不合法的移動，請重新輸入！")
    else:
        print("\n⚠️ 輸入格式錯誤！請精準輸入 4 個數字（例如：6050）")
