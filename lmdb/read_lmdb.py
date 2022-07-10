import lmdb

env = lmdb.open('./train/')
with env.begin() as txn:
    cursor = txn.cursor()
    for key, value in cursor:
        print((key, value))