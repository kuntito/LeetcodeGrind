# https://leetcode.com/problems/encode-and-decode-tinyurl/description/

# TODO https://neetcode.io/solutions/encode-and-decode-tinyurl
class Codec:
    def __init__(self):
        self.encoder = {}
        self.decoder = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        count = len(self.encoder)
        new_id = f"{count + 1}"
        
        self.encoder[longUrl] = new_id
        # TODO could you put the entire url in `decode` rather than the new_id?
        self.decode[new_id] = longUrl
        
        
        return f'http://tinyurl.com/{new_id}'
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        # TODO split based on forward slash
        
    