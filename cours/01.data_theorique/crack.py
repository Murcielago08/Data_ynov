from hashlib import md5
from rich.pretty import pprint

passlist = ["123456",
"12345",
"123456789",
"password",
"ilovkqsjdqQLM12MLKLMKeyou",
"princess",]

pprint(passlist)

hashed_lol = [md5(p.encode()).hexdigest() for p in passlist]

pprint(hashed_lol)

hashed_lol_reduced = [h[:4] for h in hashed_lol]

pprint(hashed_lol_reduced)

hashed_lol = [md5(p.encode()).hexdigest() for p in passlist]

pprint(hashed_lol)

hashed_lol_reduced = [h[:4] for h in hashed_lol]

pprint(hashed_lol)

{
    "123456": "e10adc3949ba59abbe56e057f20f883e",
    "123456": "e10adc3949ba59abbe56e057f20f883e",
}