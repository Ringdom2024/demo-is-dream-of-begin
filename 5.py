import os


def print_board(board, size):
    """打印棋盘"""
    print("  " + " ".join([chr(ord('A') + i) for i in range(size)]))
    for i in range(size):
        row_str = str(i).zfill(2) + " "
        for j in range(size):
            row_str += board[i][j] + " "
        print(row_str)


def check_win(board, size, player, row, col):
    """检查是否有玩家获胜"""
    # 定义8个方向（水平、垂直、对角线）
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

    for dr, dc in directions:
        count = 1
        # 向一个方向检查
        for i in range(1, 5):
            r, c = row + i * dr, col + i * dc
            if 0 <= r < size and 0 <= c < size and board[r][c] == player:
                count += 1
            else:
                break
        # 向相反方向检查
        for i in range(1, 5):
            r, c = row - i * dr, col - i * dc
            if 0 <= r < size and 0 <= c < size and board[r][c] == player:
                count += 1
            else:
                break
        if count >= 5:
            return True
    return False


def play_gomoku():
    size = 15  # 棋盘大小，可以调整
    board = [['.' for _ in range(size)] for _ in range(size)]
    current_player = 'X'  # 'X' 代表黑子，'O' 代表白子
    moves = 0
    max_moves = size * size

    print("欢迎来到五子棋游戏！")
    print("玩家 'X' 是黑子，玩家 'O' 是白子。")
    print("请输入坐标，例如 'A5' 表示第5行A列。")

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # 清屏
        print_board(board, size)
        print(f"当前轮到玩家 {current_player} 落子。")

        try:
            move_input = input("请输入你的落子坐标（例如 A5）：").upper()
            if len(move_input) < 2:
                raise ValueError

            col_char = move_input[0]
            if not 'A' <= col_char <= chr(ord('A') + size - 1):
                raise ValueError("列坐标超出范围。")

            col = ord(col_char) - ord('A')
            row = int(move_input[1:])

            if not (0 <= row < size):
                raise ValueError("行坐标超出范围。")

            if board[row][col] != '.':
                print("该位置已经有子了，请重新选择。")
                input("按回车键继续...")
                continue

            board[row][col] = current_player
            moves += 1

            if check_win(board, size, current_player, row, col):
                os.system('cls' if os.name == 'nt' else 'clear')
                print_board(board, size)
                print(f"恭喜玩家 {current_player} 获胜！")
                break

            if moves == max_moves:
                os.system('cls' if os.name == 'nt' else 'clear')
                print_board(board, size)
                print("平局！棋盘已满。")
                break

            current_player = 'O' if current_player == 'X' else 'X'

        except (ValueError, IndexError):
            print("无效的输入，请使用正确的格式，例如 A5。")
            input("按回车键继续...")
        except Exception as e:
            print(f"发生错误：{e}")
            input("按回车键继续...")


if __name__ == "__main__":
    play_gomoku()