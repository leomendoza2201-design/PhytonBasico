from Enemigo import *
from zombie import *
from Ogro import *

zombie = Zombie(10, 1)
ogro = Ogro(20, 3)

print(f"{Zombie.get_tipo_enemigo()} tiene {zombie.puntos_energia} de energia y puede hacer ataques")
print(f"{Zombie.habla()}")
print(f"{Ogro.get_tipo_enemigo()} tiene {ogro.puntos_energia} de energiay puede hacer ataque")
print(f"{Ogro.habla()}")