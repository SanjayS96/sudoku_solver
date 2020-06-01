import itertools

def solve_it(board): 
    board = board
    def col():

        rows = board

        rowcol = zip(*board)
        cols = [list(i) for i in rowcol]
        
        box = []
        u,m,b = board[0:3],board[3:6],board[6:9]
        l = [u,m,b]    
        
        for a in l:
            box.append(a[0][:3] + a[1][0:3] + a[2][:3])
            box.append(a[0][3:6] + a[1][3:6] + a[2][3:6])
            box.append(a[0][6:9] + a[1][6:9] + a[2][6:9])
        
        return(rows, cols, box)
    
    def guess(n):
        
        rows, cols, box = col()
        whole_board = itertools.chain.from_iterable(rows)
        
        try:
            empty = list(whole_board).index(0)

            global y,x
            y,x = (divmod(empty,9))
            active_row = rows[y]
            active_col = cols[x]
            
            box_y = divmod(y,3)
            box_x = divmod(x,3)

            box_y = box_y[0]  
            box_x = box_x[0]  

            if box_y != 0:
                box_y = box_y * 3
            
            summed_coordinates = box_y + box_x
            active_box = box[summed_coordinates]

            if n in active_box or n in active_col or n in active_row:
                return False       
            else:
                
                return n

        except ValueError:     
            pass
            

    def tally_all_empty():
        whole_board = itertools.chain.from_iterable(board)
        total = 0

        for i in whole_board:
            if i == 0:
                total +=1

        return total

    last_loc = []
    global count
    count =  0

    def solve(board):
        global count
        count+=1
        for i in range(1,10):
            if guess(i) != False:
                board[y][x] = i
                last_loc.append((y,x))
                
                if tally_all_empty() !=0:
                    solve(board)

        if tally_all_empty() == 0:
            return board
            
        board[y][x] = 0
        a,b = last_loc[-1]
        del last_loc[-1]
        board[a][b] =0
    
    a = solve(board)
    return a