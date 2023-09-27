
from korail2 import *

if __name__ == "__main__":
    
    korail = Korail("", "")
    
    reservations = korail.reservations()
    print(reservations)

    for i in range(0, len(reservations)):
        korail.cancel(reservations[i])

    reservations = korail.reservations()
    print(reservations)
