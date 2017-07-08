Convert String
===============
You are given the string `s`. Your friend just asked you if it's possible to change the string from `s` to a string `t`
by removing some characters from it. You're a pro at programming, so you decided to create a program to determine this.

Example
----------

For `s = "ceoydefthf5iyg5h5yts"` and `t = "codefights"`, the output should be
`convertString(s, t) = true`.
For `s = "addbyca"` and `t = "abcd"`, the output should be
`convertString(s, t) = false`.

Input/Output
--------------

* __[time limit] 4000ms (py)__
* __[input] string s__

    A string with alphanumeric characters.

    Guaranteed constraints:
    1 ≤ s.length ≤ 1000.

* __[input] string t__

    A string with alphanumeric characters.

    Guaranteed constraints:
    '1 ≤ t.length ≤ 1000'.

* __[output] boolean__

    Return true if it is possible to convert s to t, otherwise return false.