from BlockChain import BlockChain

# Creating a block chain
block_chain = BlockChain()

# Adding data blocks
block_chain.addBlock("Hi")
block_chain.addBlock("Good")
block_chain.addBlock("Morning")

# Print block chain
print(block_chain)

# Detect of there are any intrusions
block_chain.detect_intrusion()

# Edit a block
block_chain.editBlock(1, "Bad")

# Detect of there are any intrusions
block_chain.detect_intrusion()

# Print block chain
print(block_chain)

# Revert as there was a intrusion detected
block_chain.revert_chain()

# Print block chain after revertion
print(block_chain)
