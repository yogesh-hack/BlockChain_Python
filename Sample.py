import hashlib

import json

class Block:

    def __init__(self, index, timestamp, data, previous_hash):

        self.index = index

        self.timestamp = timestamp

        self.data = data

        self.previous_hash = previous_hash

        self.hash = self.calculate_hash()

    def calculate_hash(self):

        """

        Calculate the SHA-256 hash of the block's data

        """

        block_string = json.dumps(self.__dict__, sort_keys=True)

        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:

    def __init__(self):

        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):

        """

        Create the first block in the blockchain

        """

        return Block(0, "01/01/2020", "Genesis Block", "0")

    def add_block(self, new_block):

        """

        Add a new block to the blockchain

        """

        new_block.previous_hash = self.chain[-1].hash

        new_block.hash = new_block.calculate_hash()

        self.chain.append(new_block)

