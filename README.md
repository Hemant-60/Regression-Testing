# Regression-Testing
Python Implementation of Regression Testing
<br><br>
<b>Input Format:</b><br>
Enter number of test cases: 3<br>
Enter lines covered : 1 2 3 4 5<br>
Enter lines covered : 3 4 5 6 7<br>
Enter lines covered : 5 6 7 8 9<br>
Enter changed lines : 2 4 6<br>

<b>Output Format:</b><br>
Changed Lines :  [2, 4, 6]<br>
Covered Lines by each Test cases :  [[2, 4], [4, 6], [6]]<br>
Priority :  [2, 2, 1]<br>
T 0  , T 1  ,<br> <br>
<b>&#8613;</b>&nbsp; &nbsp;Required Test cases in order<br><br>
<b>Note:</b><br>
<ol type=1>
  <li>i<sup>th</sup> input by name 'Enter lines covered' represents lines covered by i<sup>th</sup> test case.
  <li>i<sup>th</sup> element in 'Covered Lines by each test cases' or variable 'covereLines' consists of i lists representing      altered lines covered by i<sup>th</sup> test case.
  <li>Priority list stores the priority assigned to each test cases after the changes.
</ol>
  
