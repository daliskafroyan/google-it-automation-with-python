python-os-w2-programming-with-files

# Using Python to Interact with the Operating System
## WEEK 2 - Programming with Files
* * *
### **Reading and Writing Files**
#### *Programming with Files*
Every Operating System does have a full path to resource in the file system called Absolute Path. When Relative Paths is correlation with current working directory

<br/>

#### *Reading Files*
Opening the files using one of the method available in Python. Remember to close the files after working with them.
There are two approach to open the files, using *with* or using *read* or *readline* method

<br/>

#### *Iterating Through Files*

```python
with open('spider.txt') as file:
	for line in file:
		print(line.strip())
```
Use *strip* method to remove newline character, because python is reading through a file line by line, causing weird space in every line it read.

<br/>

#### *Writing Files*
```python
with open('log.txt','w') as file:
	file.write('Tested Already')
```
Here, we have *write* method to adding the string into the log. Beside our log file inside *open* method,there is a mode which in this case are "w" which means write, and It would wipe out the previous content. To only append the string, use "a" which means append

<br/>

### **Reading and Writing Files**
#### *Working with Files*
We're gonna using *os* module to provide the layer of abstraction between python and the operating system, whatever it is
~~~python
import os
os.remove('log.txt')
os.rename('exist_log.txt','renamed_log.txt')
os.path.exist('renamed_log.txt') # use path submodule
~~~

<br/>

#### *More File Information*
To get much more information about a file, use the *path* module. 
```python
os.path.getsize('log.txt')
os.path.getmtime('log.txt') # timestamp when you work eith DB
os.path.abspath('log.txt') # construct the absolute path of a file

# use code below to make the timestamp readable 
import datetime
timestamp = os.path.getmtime('log.txt')
datetime.datetime.fromtimestamp(timestamp)
# it says, using fromtimestamp method of the datetime class -
# inside the datetime module
```

<br/>

#### *Directories*
```python
print(os.getcwd()) # which current directory your Python program is executing in
os.mkdir('newdir') # create new directory
os.chdir('newdir') # change the relative directory
os.getcwd() # pointing to newdir

os.listdir('newerdir') # listing all of files in directory

# below are function to separate file and folder, with it's pattach attached
dir = 'newdir'
for name in os.listdir(dir):
	fullname = os.path.join(dir,name)
	if os.path.isdir(fullname):
		print('directory')
	else:
		print('is file')
```

<br/>

### **Reading and Writing Files**
#### *What is CSV file?*
CSV or comma separated values is a very common data format used to store data as segment of text separated by commas. In the Python standard library, you'll find classes and modules for working with many of these data formats, including CSV and HTML.

Parsing means using rules to understand a file or datastream as structured data.

<br/>

#### *Reading CSV file*
```python
import csv
f = open('csv_file.txt')
csv_f = csv.reader(f)
for row in csv_f:
	name, phone, role = row
	print('name: {}, Phone: {}, Role: {}'.format(name, phone, role))
f.close()
```

<br/>

#### *Generating CSV*
```python
import csv
hosts = [['workstation.local','192.168.23.23'],['webserver.cloud','10.2.2.2']]
with open('hosts.csv','w') as hosts_csv:
	csv.writer(hosts_csv).writerows(hosts)
```