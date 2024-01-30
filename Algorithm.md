**Step 1.** Traverse array from last find index i (break-point) which is less then right element, i.e a[i] < a[i+1]. </br>
**Step 2.** If such a break-point i does not exist i.e. if the array is sorted in decreasing order. </br>
**Step 3.** Find smallest (**right most**) number in the right half array which is greater then ith element and swap with ith element. </br>
**Step 4.** Reverse the entire right half array, and finally return the array.</br>