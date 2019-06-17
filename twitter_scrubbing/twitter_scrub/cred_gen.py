import json

# create a dictionary to store twitter credentials

twitter_cred = dict()

twitter_cred['CONSUMER_KEY'] = 'iQZ4EzYhSuVOqtPGJrWHor6W6'
twitter_cred['CONSUMER_SECRET'] = 'jybJ55o9md5CH4iE72Q0o9BOwBAbaRvbr9c8DNFSLiPrly2LA2'
twitter_cred['ACCESS_KEY'] = '2217857665-qcQZFPvexWLnvnHll7J9oLRL6vQQ7aHMRiwQHjL'
twitter_cred['ACCESS_SECRET'] = 'VbFhAQ1miouN9uVQsfBsuw92Ej3h8C7YLRIk1JaIxguaV'

with open('twitter_credentials.json', 'w') as secret_info:
    json.dump(twitter_cred, secret_info, indent=4, sort_keys=True)
