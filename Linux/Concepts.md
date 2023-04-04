# General Concepts
## Filesystem hierarchy: Understanding the Linux filesystem hierarchy, including the purpose of each directory such as /etc, /bin, /usr, /var, etc.

![image](https://user-images.githubusercontent.com/29191813/229850564-8fb9a5c1-761f-4aee-9e66-2b06f4997143.png)

1.In the FHS, Filesystem Hierarchy Standard, all files and directories appear under the root directory /, even if they are stored on different physical or virtual devices.
 - Every single file and directory starts from the root directory
 - The only root user has the right to write under this directory
 - /root is the root user’s home directory, which is not the same as /
 
2. bin : Essential command binaries that need to be available in single-user mode; for all users, e.g., cat, ls, cp.
 - Contains binary executables
 - Common linux commands you need to use in single-user modes are located under this directory.
 - Commands used by all the users of the system are located here e.g. ps, ls, ping, grep, cp
3.  /boot : Boot loader files, e.g., kernels, initrd. 
4.  /dev : Essential device files, e.g., /dev/null. These include terminal devices, usb, or any device attached to the system
5.  /etc : Host-specific system-wide configuration files.

- Contains configuration files required by all programs.
- This also contains startup and shutdown shell scripts used to start/stop individual programs.
- Example: /etc/resolv.conf, /etc/logrotate.conf.
6. home : Users’ home directories, containing saved files, personal settings, etc. Home directories for all users to store their personal files.
7. /lib : Libraries essential for the binaries in /bin/ and /sbin/. Library filenames are either ld* or lib*.so.*
8. /mnt : Temporarily mounted filesystems. Temporary mount directory where sysadmins can mount filesystems.
9. /opt : Optional application software packages.Contains add-on applications from individual vendors.
10. /sbin : Essential system binaries, e.g., fsck, init, route.

- Just like /bin, /sbin also contains binary executables.
- The linux commands located under this directory are used typically by system administrator, for system maintenance purpose.
- Example: iptables, reboot, fdisk, ifconfig, swapon
11 . /tmp : Temporary files. Often not preserved between system reboots, and may be severely size restricted.

- Directory that contains temporary files created by system and users.
- Files under this directory are deleted when system is rebooted.

12. /usr : Secondary hierarchy for read-only user data; contains the majority of (multi-)user utilities and applications. 
- Contains binaries, libraries, documentation, and source-code for second level programs.
- /usr/bin contains binary files for user programs. If you can’t find a user binary under /bin, look under /usr/bin. For example: at, awk, cc, less, scp
- /usr/sbin contains binary files for system administrators. If you can’t find a system binary under /sbin, look under /usr/sbin. For example: atd, cron, sshd, useradd, userdel
- /usr/lib contains libraries for /usr/bin and /usr/sbin
- /usr/local contains users programs that you install from source. For example, when you install apache from source, it goes under /usr/local/apache2
- /usr/src holds the Linux kernel sources, header-files and documentation.
 


## Users and Groups: Creating and managing users and groups, understanding the difference between system and regular users.

- Linux Primary Groups
A primary group is the default group that a user account belongs to. Every user on Linux belongs to a primary group. A user’s primary group is usually the group that is recorded in your Linux system’s /etc/passwd file. When a Linux user logs into their system, the primary group is usually the default group associated with the logged in account.

You can find a user’s primary group ID by viewing the contents of the your system’s /etc/passwd file.

![image](https://user-images.githubusercontent.com/29191813/229856169-c2263b08-68be-45d5-b722-139a045f4134.png)

- Linux Secondary Groups
Once a user has been created with their primary group, they can be added to secondary groups. Linux system users can have a maximum of 15 secondary groups. A Linux system’s groups are stored in the /etc/group file.

![image](https://user-images.githubusercontent.com/29191813/229856309-efd75a0e-10c2-45a4-8618-ac6a14c13f5b.png)

- Creating and Deleting User Accounts
To create a new standard user, use the useradd command. The syntax is as follows:

useradd name
 
You need to set a password for the new user by using the passwd command. Note, you need root privileges to change a user password. The syntax is as follows:

passwd username
 
 The user is be able to change their password at any time using the passwd command with the syntax. Below is an example:

$ passwd
Changing password for lmartin.
(current) UNIX password:
Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully
 
- To remove a user account, enter the following command:

userdel name
Issuing the command above only deletes the user’s account. Their files and home directory are not be deleted.

To remove the user, their home folder, and their files, use this command:

userdel -r name

## Permissions: Understanding Linux file permissions and ownership, including how to modify them using chmod, chown, and chgrp commands.

File permissions : 
User: the owner of the file (person who created the file).
Group: the group can contain multiple users. Therefore, all users in that group will have the same permissions. It makes things easier than assign permission for every user you want.
Other: any person has access to that file, that person has neither created the file, nor are they in any group which has access to that file.
Example :

![image](https://user-images.githubusercontent.com/29191813/229854103-61c284f7-7db4-4d17-b83f-8b80ac281d7b.png)

“-rw-r–r–”. 
‘r’ = read.
‘w’ = write.
‘x’ = execute.
‘-’ = no permission.

![image](https://user-images.githubusercontent.com/29191813/229854259-5633da32-8f44-49b7-9f7d-ac4c60c8df69.png)

the empty first part means that it is a file. If it were a directory then it will be the letter “d” instead. The second part means that the user “Home” has read and write permissions but he does not have the execute one. The group and others have only the read permission.

![image](https://user-images.githubusercontent.com/29191813/229854449-e589343d-170a-4a4d-bfbf-9236e2c0a705.png)
![image](https://user-images.githubusercontent.com/29191813/229854497-6749908b-84e0-4192-8abe-2226bcb6e319.png)
Then the permissions will be: -rwxrwxrwx.

 remove the execute from the group and the write from other by:

chmod 765 section.txt
The permissions will be: -rwxrw-r-x.

![image](https://user-images.githubusercontent.com/29191813/229855463-dd9b5c2a-0b00-478b-b871-76a81440e79c.png)

![image](https://user-images.githubusercontent.com/29191813/229855077-4616e445-6f1b-4c9d-bdc4-aeaa2c07b24c.png)


## Package management: Familiarity with RPM and Yum package management systems, including how to install, remove, and update packages.
Refer below 

## Network configuration: Configuring network interfaces, setting IP addresses, configuring routing, understanding DNS, and troubleshooting network issues.


## Services and daemons: Managing and troubleshooting Linux services and daemons, including starting, stopping, and restarting them.
Refer below 


## Process management: Understanding how to manage Linux processes, including listing running processes, sending signals, and killing processes.

## Bash scripting: Familiarity with basic Bash scripting concepts, including variables, loops, conditional statements, and command-line arguments.

## System logs: Understanding system logging mechanisms and being able to analyze log files for troubleshooting purposes.


## Security: Basic understanding of Linux security concepts, including securing SSH, using firewalls, and managing users with sudo access.


#  RHEL Specific : 

- All software on a Red Hat Enterprise Linux system is divided into RPM packages, which are stored in particular repositories. When a system is subscribed to the Red Hat Content Delivery Network, a repository file is created in the /etc/yum.repos.d/ directory
- Listing all available repositories:

 subscription-manager repos --list
- Listing all currently enabled repositories:

 yum repolist
- Enabling or disabling a repository:

subscription-manager repos --enable repository
 subscription-manager repos --disable repository
- Searching for packages matching a specific string:

 yum search string
- Installing a package:

yum install package_name
- Updating all packages and their dependencies:

yum update
- Updating a package:

yum update package_name
- Uninstalling a package and any packages that depend on it:

yum remove package_name
- Listing information on all installed and available packages:

 yum list all
- Listing information on all installed packages:

yum list installed

- Service Related :

![image](https://user-images.githubusercontent.com/29191813/229847019-40be5536-ad10-463e-a389-a4facea9f5c9.png)
![image](https://user-images.githubusercontent.com/29191813/229847130-c1c7db0e-25b1-4989-95a1-b426b9256125.png)
![image](https://user-images.githubusercontent.com/29191813/229847330-b1163ac9-70e3-4651-97a1-236888ced6f0.png)
![image](https://user-images.githubusercontent.com/29191813/229847693-d7b38a6b-b60e-40f7-b0af-f12328b1a694.png)
![image](https://user-images.githubusercontent.com/29191813/229847761-101d4530-2595-4b6d-9c34-72d41a8f020f.png)

- Enhancing System Security with a Firewall, SELinux and SSH Logings
Computer security is the protection of computer systems from the theft or damage to their hardware, software, or information, as well as from disruption or misdirection of the services they provide. Ensuring computer security is therefore an essential task not only in the enterprises processing sensitive data or handling some business transactions.
A firewall is a network security system that monitors and controls the incoming and outgoing network traffic based on predetermined security rules. A firewall typically establishes a barrier between a trusted, secure internal network and another outside network.

On Red Hat Enterprise Linux 7, the firewall is provided by the firewalld service, which is automatically enabled during the installation of Red Hat Enterprise Linux.
 
![image](https://user-images.githubusercontent.com/29191813/229848488-f770fb34-a0a9-4538-887a-493c6d2df3dc.png)
 

- Establishing an SSH Connection
Generate a public and a private key:  ssh-keygen
Both keys are stored in the ~/.ssh/ directory:

~/.ssh/id_rsa.pub - public key
~/.ssh/id_rsa - private key

The public key does not need to be secret. It is used to verify the private key. The private key is secret. You can choose to protect the private key with the passphrase that you specify during the key generation process. With the passphrase, authentication is even more secure, but is no longer password-less. You can avoid this using the ssh-agent command. In this case, you will enter the passphrase only once - at the beginning of a session.

Copy the most recently modified public key to a remote machine you want to log into: 
ssh-copy-id USER@hostname

Normal and System Accounts
Normal accounts are created for users of a particular system. Such accounts can be added, removed, and modified during normal system administration.

System accounts represent a particular applications identifier on a system. Such accounts are generally added or manipulated only at software installation time, and they are not modified later.
![image](https://user-images.githubusercontent.com/29191813/229849245-eaaa82e7-f463-4932-87f3-ade2d38535f3.png)

![image](https://user-images.githubusercontent.com/29191813/229849336-a9288756-c6ca-4cce-82b8-ca95f49142fb.png)

- Using the Log Files to Troubleshoot Problems :
The logging system in Red Hat Enterprise Linux 7 is based on the built-in syslog protocol. 

![image](https://user-images.githubusercontent.com/29191813/229849886-02ad1422-8cbd-4d62-8185-a4c913baaa16.png)
![image](https://user-images.githubusercontent.com/29191813/229849948-317f2988-fd45-4808-9cdf-908cd8ae9e78.png)





