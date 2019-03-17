class Block:
    def __init__(self, block_number, nonce, data, hash_value, prev_hash):
        self.block_number = block_number
        self.nonce = nonce
        self.data = data
        self.hash_value = hash_value
        self.prev_hash = prev_hash

    def __str__(self):
        # Here only first 10 digits of the hash values are printed just to have clean single line prints.
        return "Block_number: {}, nonce: {}, data={}, hash_value: {}, prev_hash: {}".format(self.block_number,
                                                                                            self.nonce,
                                                                                            self.data,
                                                                                            self.hash_value[:10],
                                                                                            self.prev_hash[:10])
