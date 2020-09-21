#decimal to binary
while True:
     ans = ' ' 
     user_input = input('ENTER NO')
     if user_input == 'done':quit
     int_user = int(user_input)  
     while int_user >= 1:
          g = int_user % 2
          if g == 1:
               j = '1'
          else:
               j = '0'
          ans = j + ans
          
          int_user = int(int_user / 2)
     print(ans)     