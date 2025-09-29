from Smartphone import Smartphone


catalog = [
    Smartphone(phone_brand="Xiaomi", phone_model="Poco",
               subscriber_number="«+79999999999»"),
    Smartphone(phone_brand="Realme", phone_model="GT2",
               subscriber_number="«+79998887766»"),
    Smartphone(phone_brand="Samsung", phone_model="Galaxu",
               subscriber_number="«+79987654321»"),
    Smartphone(phone_brand="Xiaomi", phone_model="Realme",
               subscriber_number="«+79123456789»"),
    Smartphone(phone_brand="Apple", phone_model="16 Pro",
               subscriber_number="«+79005553535»"),
    Smartphone(phone_brand="Tecno", phone_model="Spark",
               subscriber_number="«+79999999999»")
]


for smartphone in catalog:
    print(f"{smartphone.phone_brand} {smartphone.phone_model} - {smartphone.subscriber_number}")
