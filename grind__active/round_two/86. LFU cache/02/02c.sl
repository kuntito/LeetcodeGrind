i want to write a class.

they call it LFU cache,
least frequently used cache.

it stores numbers using key-value pairs.
the keys point to the numbers.

it has a max capacity,
and when full, adding a new key
means removing the least frequently used key.

what counts as a use?
whenever the key is retrieved
or repurposed for a new number.

every get, and every put.

like, hash maps, a key can be re-used.
a number can be fetched by it's key.

so, to add a new key when the cache is full.
the least frequently used key is removed.

and if there's a tie, among the tied keys,
the least recently used gets removed.

adding a key should happen in O(1) time.
removing a key should happen in O(1) time.

# TODO rewrite and make sure it captures the essence of the question.