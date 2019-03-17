# BlockChain basic demo

```
Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from BlockChain import BlockChain
>>> block_chain = BlockChain()
>>> block_chain.addBlock("Hi")
>>> block_chain.addBlock("Good")
>>> block_chain.addBlock("Morning")
>>> print(block_chain)
Block_number: 0, nonce: 72542, data=Hi, hash_value: 0000c66d29, prev_hash: 0
Block_number: 1, nonce: 44622, data=Good, hash_value: 0000c76918, prev_hash: 0000c66d29
Block_number: 2, nonce: 2386, data=Morning, hash_value: 0000bfeb30, prev_hash: 0000c76918
>>>
>>> block_chain.detect_intrusion()
No intrusion detected.
>>> block_chain.editBlock(1, "Bad")
Block #1 edited
>>>
>>> block_chain.detect_intrusion()
Intrusion detected!!!
>>>
>>> print(block_chain)
Block_number: 0, nonce: 72542, data=Hi, hash_value: 0000c66d29, prev_hash: 0
Block_number: 1, nonce: 44622, data=Bad, hash_value: 6fe7d7112c, prev_hash: 0000c66d29
Block_number: 2, nonce: 2386, data=Morning, hash_value: 0000bfeb30, prev_hash: 0000c76918
>>>
>>> block_chain.revert_chain()
Chain reverted.
>>>
>>> print(block_chain)
Block_number: 0, nonce: 72542, data=Hi, hash_value: 0000c66d29, prev_hash: 0
Block_number: 1, nonce: 44622, data=Good, hash_value: 0000c76918, prev_hash: 0000c66d29
Block_number: 2, nonce: 2386, data=Morning, hash_value: 0000bfeb30, prev_hash: 0000c76918
>>>
>>> exit()


```
