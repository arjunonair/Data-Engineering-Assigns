## Big Data (HDFS) Assignment
### Problem Statement: Using Command line of HDFS, perform following tasks.

#### a) Create a directory /hadoop/hdfs/ in HDFS
```bash
hdfs dfs -mkdir -p /hadoop/hdfs
```
![alt text](image-4.png)

#### b) Create a temp directory in Hadoop. Run HDFS command to delete “temp” directory.

```bash
hdfs dfs -mkdir /hadoop/temp

hdfs dfs -rmdir /hadoop/temp
```
![alt text](image-5.png)
![alt text](image-6.png)

#### c) List all the files/directories for the given hdfs destination path.
```bash
hdfs dfs -ls /
```
![alt text](image-7.png)

#### d) Command that will list the directories in /hadoop folder.
```bash
hdfs dfs -ls /hadoop
```
![alt text](image-8.png)

#### e) Command to list recursively all files in hadoop directory and all subdirectories in hadoop directory
```bash
hdfs dfs -ls -R /hadoop
```
![alt text](image-9.png)

#### f) List all the directory inside /hadoop/hdfs/ directory which starts with 'dir'.
- approach one:
```bash
hdfs dfs -ls -d /hadoop/hdfs/dir*
```
![alt text](image-10.png)

#### g) Create a temp.txt file. Copies this file from local file system to HDFS
```bash
sudo nano test.txt
hdfs dfs -put /home/hadoop/test.txt /hadoop/hdfs/
```
![alt text](image-11.png)

#### h) Copies the file from HDFS to local file system.
```bash
hdfs dfs -get /hadoop/hdfs/temp.txt .
```
![alt text](image-12.png)

#### i) Command to copy from local directory with the source being restricted to a local file reference.
```bash
hdfs dfs -put ./file.txt /hadoop/hdfs
```
![alt text](image-13.png)

#### j) Command to copies to local directory with the source being restricted to a local file reference.
```bash
hdfs dfs -get ./file.txt .
```
![alt text](image-15.png)

#### k) Command to move from local directory source to Hadoop directory.
```bash
hdfs dfs -moveFromLocal ./file.txt /hadoop/hdfs/
```
![alt text](image-16.png)

#### l) Deletes the directory and any content under it recursively.
```bash
hdfs dfs -rm -r /hadoop/hdfs/
```
![alt text](image-17.png)

#### m) List the files and show Format file sizes in a human-readable fashion.
```bash
hdfs dfs -ls -h /hadoop/
```
![alt text](image-18.png)

#### n) Take a source file and outputs the file in text format on the terminal.
```bash
cat test.txt
```
![alt text](image-19.png)

#### o) Display the content of the HDFS file test on your /user/hadoop2 directory.
```bash
hdfs dfs -cat /hadoop/test.txt
```
![alt text](image-20.png)
#### p) Append the content of a local file test1 to a hdfs file test2.
```bash
hdfs dfs -appendToFile /home/hadoop/file.txt /hadoop/test.txt
```
![alt text](image-21.png)

#### q) Show the capacity, free and used space of the filesystem
```bash
hdfs dfs -df
```
![alt text](image-24.png)

#### r) Shows the capacity, free and used space of the filesystem. Add parameter Formats the sizes of files in a human-readable fashion.
```bash
hdfs dfs -df -h
```
![alt text](image-23.png)

#### s) Show the amount of space, in bytes, used by the files that match the specified file pattern.
```bash
hdfs dfs -du -s /hadoop/hdfs/*txt
```
![alt text](image-25.png)

#### t) Show the amount of space, in bytes, used by the files that match the specified file pattern. Formats the sizes of files in a human-readable fashion.
```bash
hdfs dfs -du -h /hadoop/hdfs/*txt
```
![alt text](image-26.png)

#### u) Check the health of the Hadoop file system.
```bash
hdfs fsck /
```
![alt text](image-27.png)

#### v) Command to turn off the safemode of Name Node.
```bash
hdfs dfsadmin -safemode leave
```
![alt text](image-28.png)

#### w) HDFS command to format NameNode.
```bash
hdfs namenode -format
```

#### x) Create a file named hdfstest.txt and change it number of replications to 3.
```bash
hdfs dfs -setrep 3 /hadoop/hdfstest.txt
```
![alt text](image-29.png)

#### y) Write command to display number of replicas for hdfstest.txt file.
```bash
hdfs dfs -stat %r /hadoop/hdfstest.txt
```
![alt text](image-30.png)

#### z) Write command to Display the status of file “hdfstest.txt” like block size, filesize in bytes.
```bash
hdfs dfs -stat /hadoop/hdfstest.txt
```
![alt text](image-31.png)

#### aa) Write HDFS command to change file permission from rw – r – r to rwx-rw-x for hdfstest.txt.
```bash
hdfs dfs -chmod 761 /hadoop/hdfstest.txt
```
![alt text](image-32.png)
