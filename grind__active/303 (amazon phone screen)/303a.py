from typing import List


class IPChecker:
    def __init__(self, addresses: List[str]) -> None:
        # the difference between the addresses is based on the last octet
        
        self.plain_addresses = set()
        self.range_addresses = {}
        
        for add in addresses:
            firstPart, lastOctet = add.rsplit(".")
            
            # if hyphen is in the last octet, it's in type two
            if "-" in lastOctet:
                self.range_addresses[firstPart] = lastOctet
            else:
                self.plain_addresses.add(add)
                
        # this way i can handle the plain addresses and the ones with ranges
        
    def isAddressExist(self, add):
        # check if address is type one
        if add in self.plain_addresses:
            return True
        
        # check if address is type two
        firstPart, lastOctet = add.rsplit(".")
        if firstPart in self.range_addresses:
            rng = self.range_addresses[firstPart]
            
            low, high = rng.split("-")
            low = int(low)
            high = int(high)
            
            lastOctet = int(lastOctet)
            
            return low <= lastOctet <= high
            
            
        