# Below I have my user credentials I am trying to discover. They are encrypted so I do not know what they actually are.
# I have a wordlist of hundreds of words that may be the password, I encrypt each one with the same encryption that I
# believe was used in the data set I am trying to access. The program then compares these ecrypted words to see if any are
# a match with the users I am looking for. If it is, that must be there password.

# This is a good example of why passwords should not just be one word that can be easily guesses.

# jjones,   1234,   dd3a8eb2892b6380d53f9defea3c70bd3a1e10cf
# msmith,   5678,   dc68db2fcc09a6aca8db2eefba025f6461c31115
# epickle,  4321,   2a14da4ad8952d069b9cc4abca60077b63435d94
# qwarthog, 7777,   096392411c601d3017486dff9de7a5f78d3c9caa

import hashlib

wordlist = open("wordlist800.txt", 'r')

jjones = ''
msmith = ''
epickle = ''
qwarthog = ''
for i in wordlist:

    i_hashed = hashlib.sha1(((i.rstrip()).encode())).hexdigest()
    #print(i_hashed)
    if i_hashed == "dd3a8eb2892b6380d53f9defea3c70bd3a1e10cf":
        jjones = i
        print('jjones: ' + jjones)
    elif i_hashed == "dc68db2fcc09a6aca8db2eefba025f6461c31115":
        msmith = i
        print('msmotch: ' + msmith)
    elif i_hashed == "2a14da4ad8952d069b9cc4abca60077b63435d94":
        epickle = i
        print('epickle: ' + epickle)
    elif i_hashed == "096392411c601d3017486dff9de7a5f78d3c9caa":
        qwarthog = i
        print('qwarthog: '+ qwarthog)

#print(jjones + '\n' + msmith + '\n' + epickle + '\n' + qwarthog)
