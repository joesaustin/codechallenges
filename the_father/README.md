The Father
========================
The Gangsteranos family has been through a lot of trouble lately. With all the quarrels that have been breaking out, the
family is starting to lose its authority on the streets, and it's time to do something about it.

The Father decided to start dealing with the troublemakers without making decisions that are too harsh. To begin with,
he wants to try to split the family into two groups, such that in each group no two members hate one another.

Given haters, the list of family members who hate each other, figure out if it's possible to split them into two groups
like Father wants.



Example
------------
* __For__ `haters = ["Dead_Bowie Fake_Thomas_Jefferson"]`, the output should be
`theFather(haters) = true`.

    Since only two members of the family hate one another, they can be put into separate groups.

* __For__ `haters = ["Dead_Bowie Fake_Thomas_Jefferson", 
          "Fake_Thomas_Jefferson Fury_Leika", 
          "Fury_Leika Dead_Bowie"]`

    The output should be `theFather(haters) = false.`<br/>
    There's no way to split the haters into two groups as Father wants.

Input/Output
-------------

* __[time limit]__ 4000ms (py)

* __[input]__ array.string haters

    An array of pairs of family members who hate one another and can't be put into one group. Each pair is given as a
string, with the two names separated by a single whitespace character. It is guaranteed that no person hates themselves.

    Guaranteed constraints:<br/>
    `1 ≤ haters.length ≤ 13000,`<br/>
    `3 ≤ haters[i].length ≤ 100.`

* __[output]__ boolean<br/>
    Return `true` if it's possible to split the family members into two groups like Father wants, otherwise return `false`.