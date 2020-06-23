from base64 import b32encode
from hashlib import sha1
from random import random
import pytz


TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

def random_pk():
	random_string = str(random()).encode()
	sha1_hash = sha1(random_string).digest()
	pk = b32encode(sha1_hash).upper()[:9]
	return pk.decode()
