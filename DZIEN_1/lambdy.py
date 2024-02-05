nb = [45,1,2,-7,0,46,12,9,0,133,-44,14]

#utwórz nową listę nbparzyste do której pobierz wartości parzyste z listy nb
#utwórz nową listę cube do której zamapujesz wartości z listy nb podniesione do potęgi trzeciej

nbparzyste = list(filter(lambda x:x%2==0,nb))

cube = list(map(lambda x:x**3,nb))
