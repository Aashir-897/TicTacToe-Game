def board(table):
    # For making stracture of table
        for r in range(len(table)):
            print ( " | ".join(table[r]))
            if r< len(table) - 1:
                print('-' * 9)
                
table = [['0','1','2'],
         ['3','4','5'],
         ['6','7','8']]             
     
board(table)                               
# This is maximun move
moves= 9
# This is first move
turn = 'X'
try:
    for i in range(moves):
        a = int(input(f"Enter a number as your move: "))
        if a>8:
             print("Please enter under 8")
             continue
            
        # Claculate row and coloumn from input
        row,col = divmod(a,3)

        # Checking place are already hold or not
        if table[row][col] in ["X","O"]:
            print("This position already taken try again") 
            continue

        # Update the table
        table[row][col] =turn
        print("\nUpdated board:")
        board(table) 

        # Checking winner in rows
        for row in table:
            if row[0] == row[1]  == row[2] and row[0] in['X','O']:
                print(f"{row[0]} is win!")
                break

        # Checking winner in coloumn
        for col in range(3):
            if table[0][col] == table[1][col] == table[2][col] and table[0][col] in['X','O']:
                print(f"{table[0][col]} is win!")
                break

        # Checking winner in right diognal
            if table[0][0] == table[1][1] ==table[2][2] and table[0][0] in ['X','O']:
                print (f'{table[0][0]} is winner!')
                break

        # checking winner in left diognal
            if table[0][2] == table[1][1] ==table[2][0] and table[0][2] in ['X','O']:
                print (f'{table[0][2]} is winner!')
                break
                
        # Turning moves one player to another player
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

      
            
  
except ValueError as e:
     print("Error: Please enter valid integers.")




    

