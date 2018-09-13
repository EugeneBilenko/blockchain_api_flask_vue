import hashlib as hl
import json


def hash_string_256(string):
    return hl.sha256(string).hexdigest()


def hash_block(block):
    block_type = 'transactions'
    hashable_block = block.__dict__.copy()
    hashable_block[block_type] = [tx.to_ordered_dict() for tx in hashable_block[block_type]]
    return hash_string_256(
        json.dumps(hashable_block, sort_keys=True).encode()
    )

