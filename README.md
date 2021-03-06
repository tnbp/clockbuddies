# clockbuddies
Automatically generate clock buddies for your language classroom

**Clock Buddies** is a system for learning environments that involve lots of partnered activities.

By default, when beginning a partnered activity, a teacher has two options:
1. Assign each pair of two individually
2. Have everyone work with their right or left neighbor

Option 1 takes up a lot of time and is often met with disapproval from students, since the teacher's decision can seem arbitrary. Option 2 saves time, but results in everyone always working with the same partner.

Using the Clock Buddy system, the teacher creates 12 different sets of pairs of two. Every student now has a total of 12 different possible partners. When beginning a partnered activity, the teacher simply states which set to use this time, for example by saying *"Work with your 7 o'clock partners."* Every student can then consider their "clock" (which can be manually designed or printed out) to find out whom they should work with today. By using different numbers every time, teachers can ensure that pairs are formed quickly but without students restricting themselves to only ever using the same partner.

However, there is one catch: Generating 12 distinct sets of pairs that each include every single student is a computationally difficult task. Hence, this python script to automatically generate 12 pairs and therefore facilitate the use of this system.

More information can be found anywhere on the web, such as here: http://www.montgomeryschoolsmd.org/uploadedFiles/schools/ritchieparkes/staff/What%20Are%20Clock%20Buddies.pdf

# Usage notes
1. **Download** the generator script **clockbuddies.py**.
2. Tell your installation of Python 3 to **run it**: `python3 clockbuddies.py`
(You can execute it with Python 2, but the output will look slightly strange.)
3. Pairings will be **printed to *stdout***. 

# Example output:
```
Pairings for 1 o'clock:
         Heidi and Erin
         Judy and Ted
         Alice and Olivia
         Walter and Mallory
         Victor and Frank
         Xaver and Bob
         Sybil and Grace
         Pat and Dave
         Carol and ** NOBODY **

************************

Pairings for 2 o'clock:
         Victor and Dave
         Grace and Heidi
         [etc...]
```

# Code quality and participation
This script has worked for any case I have thrown at it so far. It is not efficient--if it encounters a problem, it will just try again as often as it needs to. Execution should be near-instantaneous on any halfway modern computer.

Comments and ideas for improvement welcome.
