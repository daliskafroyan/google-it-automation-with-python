troubleshoot-and-debug-w1-troubleshooting-concepts

# Troubleshooting and Debugging Techniques
## WEEK 1 - Troubleshooting Concepts

### **Introduction to Debugging**
* * *
#### *What is debugging?*
Troubleshooting is the process of identifying, analyzing, and solving problems. On the flip side, debugging is the process of identifying, analyzing, and removing bugs in a system. We sometimes use troubleshooting and debugging interchangeably. But generally, we say troubleshooting when we're fixing problems in the system running the application, and debugging when we're fixing the bugs in the actual code of the application. 

#### *Problem Solving Steps?*
1. Gathering Information
2. Finding the Root Cause
3. Performing Necessary Remidiation

#### *Silently Crashing Application*
```bash
strace -o <system-log-name> <python-program.py>
less <system-log-name
```
It's useful when a program shutting down by identifying the system calls. System Calls are the calls that the programs running on our computer make to the running kernel.

<br/>

### **Understanding the Problem**
* * *
#### *It Doesn't Work*
What were you trying to do? What steps did you follow? What was the expected result? What was the actual result? If the ticketing system your company uses allows this, it's a good idea to include these questions in the form that users have to fill out when reporting an issue. This way we save time and can start asking more specific questions right away. Otherwise, these are almost always going to be the first questions you ask. Another thing to keep in mind is that when debugging a problem, we want to consider the simplest explanations first and avoid jumping into complex or time-consuming solutions unless we really have to.

#### *Creating a Reproduction Case*
When we're dealing with an issue that's tricky to debug, we want to have a clear reproduction case for the problem. A reproduction case is a way to verify if the problem is present or not. 

The example are when a program fails with an error, “No such file or directory.” You create a directory at the expected file path and the program successfully runs. Then the best way to describe the problems are to write a report explaining to open the program without the specific directory on the computer

#### *Finding the Root Cause*
Understanding the root cause is essential for performing the long-term remediation, which is the final result that we want in troubleshooting. Tools available for diagnosing whether a program process generate much input or output are iotop, iostat and vmstat

#### *Dealing with Intermittent Issues*
Issues could easily come and goes. This is an especially annoying type of intermittent issue, nicknamed Heisenbug, in honor of Werner Heisenberg. He's the scientist that first described the observer effect, where just observing a phenomenon alters the phenomenon. Heisenbugs are extra hard to understand, because when we meddle with them, the bug goes away. These bugs usually point to bad resource management.

Maybe the memory was wrongly allocated, the network connections weren't correctly initialized, or the open files weren't properly handled. In these cases, we usually need to just spend time looking at the effected code until we finally figure out what's up. Yet another type of intermittent issue is the one that goes away when we turn something off and on again.

<br/>

### **Binary Searching a Problem**
* * *
#### *What is binary search?*
Usually when trying to find the root cause of a problem, we'll be looking for one answer in a list of many.

One possible approach would be to start from the first entry and then check if the name is the one that we're looking for. If it doesn't match, move to the second element and check again, and keep going until we find the employee with the name we're looking for, or we get to the end of the list. This is called a linear search. This type of search works but the longer the list, the longer it can take. 

If the list is sorted, we can use an alternative algorithm for searching called binary search. Because the list is sorted, we can make decisions about the position of the elements in the list. So the first thing we do is compare the name that we're looking for with the element in the middle of the list and check if it's equal, smaller, or bigger.

#### *Applying Binary Search in Troubleshooting*
By bisecting all of the log available, we could efficiently find the problem