import time



while True:
    x = input('⇥', end='\r')
    time.sleep(1)
    x = input(' ', end='\r')
    time.sleep(1)
    

while True:
            temp = input("\n⇥   ")
            match temp:
                case "1":
                    pos = 1
                    break
                case "2":
                    pos = 0.1
                    break
                case "3":
                    pos = 0.2
                    break    
                case _:
                    print("\nInvalid\n")