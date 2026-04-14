import hashlib

class BloomFilter:
    """
    Bloom Filter implementation for IP blacklist checking
    - Space-efficient probabilistic data structure
    - No false negatives (if IP is in filter, it will be found)
    - Possible false positives (may say IP is in filter when it's not)
    """
    
    def __init__(self, size=1000, hash_count=3):
        """
        Initialize Bloom Filter
        
        Args:
            size: Size of the bit array
            hash_count: Number of hash functions to use
        """
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size
        self.items_added = 0
    
    def _hash(self, item, seed):
        """Generate hash value for an item with a seed"""
        hash_input = f"{item}{seed}".encode('utf-8')
        hash_digest = hashlib.md5(hash_input).hexdigest()
        return int(hash_digest, 16) % self.size
    
    def add(self, item):
        """Add an item to the Bloom Filter"""
        for i in range(self.hash_count):
            index = self._hash(item, i)
            self.bit_array[index] = 1
        self.items_added += 1
    
    def check(self, item):
        """
        Check if an item might be in the Bloom Filter
        
        Returns:
            True: Item might be in the filter (or false positive)
            False: Item is definitely NOT in the filter
        """
        for i in range(self.hash_count):
            index = self._hash(item, i)
            if self.bit_array[index] == 0:
                return False
        return True
    
    def get_stats(self):
        """Get Bloom Filter statistics"""
        bits_set = sum(self.bit_array)
        load_factor = bits_set / self.size
        
        # Estimate false positive rate
        # FPR ≈ (1 - e^(-k*n/m))^k
        # where k=hash_count, n=items_added, m=size
        import math
        if self.items_added > 0:
            fpr = (1 - math.exp(-self.hash_count * self.items_added / self.size)) ** self.hash_count
        else:
            fpr = 0
        
        return {
            'size': self.size,
            'hash_count': self.hash_count,
            'items_added': self.items_added,
            'bits_set': bits_set,
            'load_factor': round(load_factor, 4),
            'estimated_fpr': round(fpr, 6)
        }
