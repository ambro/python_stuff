import time
from libs.openexchange import OpenExchangeClient

API_KEY = "dbd0b33ec2e844f4bc1bec8a5edb909d"

client = OpenExchangeClient(API_KEY)
start_time = time.time()
usd_amount = 1000
gbp_amount = client.convert(usd_amount, 'EUR', 'GBP')
end_time = time.time()
print(f"duration = {end_time - start_time}")

start_time = time.time()
gbp_amount = client.convert(usd_amount, 'EUR', 'GBP')
end_time = time.time()
print(f"duration = {end_time - start_time}")


print(f"USD{usd_amount} is GBP{gbp_amount:.2f}")
