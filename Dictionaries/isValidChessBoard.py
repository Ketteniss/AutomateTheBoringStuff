def isValidChessBoard(board):
    properBoard = {
        'figures' : {
            'white' :   [ 'wpawn', 'wknight', 'wbishop', 'wrook', 'wqueen' ],
            'black' :   [ 'bpawn', 'bknight', 'bbishop', 'brook', 'bqueen' ]
        },
        'grid' : [  '1a', '2a', '3a', '4a', '5a', '6a', '7a', '8a', 
                    '1b', '2b', '3b', '4b', '5b', '6b', '7b', '8b', 
                    '1c', '2c', '3c', '4c', '5c', '6c', '7c', '8c', 
                    '1d', '2d', '3d', '4d', '5d', '6d', '7d', '8d', 
                    '1e', '2e', '3e', '4e', '5e', '6e', '7e', '8e', 
                    '1f', '2f', '3f', '4f', '5f', '6f', '7f', '8f', 
                    '1g', '2g', '3g', '4g', '5g', '6g', '7g', '8g', 
                    '1h', '2h', '3h', '4h', '5h', '6h', '7h', '8h'  ]
    }
    # at most 16pieces
    # at most 8 pawns
    properPieces = True
    pieces, pawns = 0, 0
    for player in ['white', 'black']:
        if player == 'white':
            for piece in properBoard['figures']['white']:
                if piece in board.values():
                    pieces += 1
                    if piece == 'wpawn':
                        pawns += 1
        else: 
            for piece in properBoard['figures']['black']:
                if piece in board.values():
                    pieces += 1
                    if piece == 'bpawn':
                        pawns += 1
        if pieces > 16 or pawns > 8:
            properPieces = False
            break

    # all pieces on valid space
    properSpaces = True
    for space in board.keys():
        if space not in properBoard['grid']:
            properSpaces = False
            break

    if properSpaces and properPieces:
        return True
    return False

trueBoard = {'1a': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
falseBoard = {'9a': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(isValidChessBoard(trueBoard))
print(isValidChessBoard(falseBoard))
