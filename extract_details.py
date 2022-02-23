import phonenumbers
from phonenumbers import geocoder
number = ""
# For privacy purposes we recommend saving number
#in another text file and reading it using read function.

ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, "en"))

from phonenumbers import carrier
service_provider = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_provider, "en"))

from phonenumbers import timezone
time_zone = timezone.time_zones_for_number(number)
print("Time Zone: ", time_zone)
valid = phonenumbers.is_valid_number(number)
print("The availability of number being used is: ", valid)

