from Address import Address
from Mailing import Mailing

to_address = "614051", "Пермь", "Уинская", "7", "12"
from_address = "620014", "Екатеринбург", "Проспект Ленина", "8", "13"
cost = (536)
track = ("TR8227711")

mailing = Mailing (to_address, from_address, cost, track)

print(mailing)

