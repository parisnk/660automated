def countDown(n):
    factorial = '!'
    while n > 0:
        print('...{0}!'.format(n))
        n = n - 1
        if(n == 0):
           print('Blast off!')
              
countDown(5)              