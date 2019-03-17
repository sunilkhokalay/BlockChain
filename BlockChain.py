import hashlib, copy

from Block import Block


class BlockChain:
    def __init__(self):
        self.chain = []
        self.validated_chain = []
        self.prefix_n = 4

    def addBlock(self, data):
        if len(self.chain) == 0:
            prev_hash = '0'
        else:
            prev_hash = self.chain[-1].hash_value
            # Genesis block
        hash_val = hashlib.sha256(str(data).encode('utf-8')).hexdigest()
        block = Block(len(self.chain), 0, data, hash_val, prev_hash)
        mined_hash_val, mined_nonce = self.mine(block)
        block.hash_value = mined_hash_val
        block.nonce = mined_nonce
        self.chain.append(block)
        self.validated_chain.append(copy.deepcopy(block))

    def __str__(self):
        return "\n".join([str(b) for b in self.chain])

    def mine_chain(self):
        broken_block = self.get_broken_block_in_chain()
        if broken_block:
            for block in self.chain[broken_block.block_number:]:
                hash_val, nonce = self.mine(block)
                self.chain[block.block_number].hash_value = hash_val
                self.chain[block.block_number].nonce = nonce
                if block.block_number < len(self.chain) - 1:
                    self.chain[block.block_number + 1].prev_hash = hash_val

    def mine(self, block):
        nonce = 0
        hash_tmp = hashlib.sha256((str(nonce) + block.data).encode('utf-8')).hexdigest()
        while hash_tmp[:self.prefix_n] != "0" * self.prefix_n:
            nonce += 1
            hash_tmp = hashlib.sha256((str(nonce) + block.data).encode('utf-8')).hexdigest()
        else:
            return hash_tmp, nonce

    def get_broken_block_in_chain(self):
        for block in self.chain:
            if block.block_number == 0:
                # Genesis block
                if block.hash_value[:self.prefix_n] == "0" * self.prefix_n:
                    pass
                else:
                    return block
            elif block.block_number < len(self.chain) - 1:
                # Rest of blocks
                if block.hash_value[:self.prefix_n] == "0" * self.prefix_n and self.chain[
                            block.block_number + 1].prev_hash == block.hash_value:
                    pass
                else:
                    return block
            else:
                if block.hash_value[:self.prefix_n] == "0" * self.prefix_n:
                    pass
                else:
                    return block

    def detect_intrusion(self):
        if len(self.chain) > 0:
            if self.get_broken_block_in_chain():
                print("Intrusion detected!!!")
            else:
                print("No intrusion detected.")

    def editBlock(self, block_number, data):
        self.chain[block_number].data = data
        self.chain[block_number].hash_value = hashlib.sha256(str(data).encode('utf-8')).hexdigest()
        print("Block #{} edited".format(block_number))

    def revert_chain(self):
        self.chain = self.validated_chain[:]
        print("Chain reverted.")
