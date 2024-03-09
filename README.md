<h2><a href="https://leetcode.com/problems/lru-cache/description/">79. LRU Cache</a></h2>

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

1. LRUCache(int capacity) Initialize the LRU cache with positive size capacity. </br>
2. int get(int key) Return the value of the key if the key exists, otherwise return -1. </br>
3. void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key. </br>

The functions get and put must each run in O(1) average time complexity.

**Example 1**:

**Input**
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"] </br>
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

**Output**: [null, null, null, 1, null, -1, null, -1, 3, 4]

**Explanation**
LRUCache lRUCache = new LRUCache(2); </br>
lRUCache.put(1, 1); // cache is {1=1} </br>
lRUCache.put(2, 2); // cache is {1=1, 2=2} </br>
lRUCache.get(1);    // return 1 </br>
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3} </br>
lRUCache.get(2);    // returns -1 (not found) </br>
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3} </br>
lRUCache.get(1);    // return -1 (not found) </br>
lRUCache.get(3);    // return 3 </br>
lRUCache.get(4);    // return 4 </br>

**Constraints**:

    • 1 <= capacity <= 3000
    • 0 <= key <= 10^4
    • 0 <= value <= 10^5
    • At most 2 * 10^5 calls will be made to get and put