# 킹 (1개), 퀸 (1개), 룩 (2개), 비숍 (2개), 나이트 (2개), 폰 (8개)
input_chess_piece = list(map(int, input().split()))
original_chess_piece = [1, 1, 2, 2, 2, 8]

for x, y in zip(input_chess_piece, original_chess_piece):
    piece = y - x # 몇 개의 피스를 더하거나 빼야 되는지 저장
    print(piece, end=' ')