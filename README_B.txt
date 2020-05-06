To fix the log in page in the catamount bank app I
went into password_crack.py, added a salt to the hash_pw
and then specified the salt length in authenticate.

Then I went into bank.py and changed the if statement
at line 61 to utilize authenticate rather than hash_pw.
This is so that the password can be properly verified with
the newly added salt.