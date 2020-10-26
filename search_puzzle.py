import hashlib
import time

start = time.time()
puzzleID = "BBSE_E01"
d = "0000"
x = 0

while True:
    result = hashlib.sha256(puzzleID.encode('utf-8') + str(x).encode('utf-8')).hexdigest()
    
    if result[:len(d)] == d:
        res = x
        break
    else:
        x = x + 1

print("Found x: " + str(res) + " with hash value " + str(result) + " in " + str(time.time() - start) + " seconds.")