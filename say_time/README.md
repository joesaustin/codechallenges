Tell Time
========================
Given a digital time, your task is to return a string that represents this time in regular English.
The time should be rounded to the nearest multiple of 5.

If you need help with time representation in English, check out this [link](http://www.englisch-hilfen.de/en/words/uhr.htm) for reference.


Examples
------------
* __For__ `time_str = "12:00"`, the output should be
`tellTime = "It's twelve o'clock"`.

* __For__ `time_str = "08:42"`, the output should be
`tellTime = "It's twenty to nine"`.


Input/Output
-------------
* __[time limit]__ 4000ms (py)

* __[input]__ string time_str<br/>
    The time in the hh:mm format.
    It is guaranteed that `1 ≤ hh ≤ 12, and 0 ≤ mm ≤ 59`.

* __[output]__ string<br/>
    time_str in common English.