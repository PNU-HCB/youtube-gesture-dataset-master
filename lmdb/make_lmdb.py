# -*- coding: utf-8 -*-
import lmdb

# map_size defines the maximum storage capacity, the unit is kb, the following defines 1TB capacity
env = lmdb.open("./train", map_size=1099511627776)

txn = env.begin(write=True)

# Add data and key value
txn.put(str('1').encode(), str('aaa').encode())
txn.put(str('2').encode(), str('bbb').encode())
txn.put(str('3').encode(), str('ccc').encode())

# Delete data by key value
#txn.delete(key = '1')

# change the data
#txn.put(key = '3', value ='ddd')

# Submit changes through the commit() function
txn.commit()
env.close()