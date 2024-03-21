<h2><a href="https://leetcode.com/problems/find-median-from-data-stream/description/">140. Find Median from Data Stream</a></h2>

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

1. For example, for arr = [2,3,4], the median is 3. </br>
2. For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5. </br>

Implement the MedianFinder class:

1. **MedianFinder()** initializes the MedianFinder object. </br>
2. **void addNum(int num)** adds the integer num from the data stream to the data structure. </br>
3. **double findMedian()** returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

**Example 1**:

**Input**: ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"], [[], [1], [2], [], [3], []]

**Output**: [null, null, null, 1.5, null, 2.0]

**Explanation**:

MedianFinder medianFinder = new MedianFinder(); </br>
medianFinder.addNum(1);    // arr = [1] </br>
medianFinder.addNum(2);    // arr = [1, 2] </br>
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2) </br>
medianFinder.addNum(3);    // arr[1, 2, 3] </br>
medianFinder.findMedian(); // return 2.0 </br>

**Constraints**:

    • -10^5 <= num <= 10^5
    • There will be at least one element in the data structure before calling findMedian.
    • At most 5 * 104 calls will be made to addNum and findMedian.

**Follow up**:

    • If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
    • If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?