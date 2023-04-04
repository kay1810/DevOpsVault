- Filesystem hierarchy: Understanding the Linux filesystem hierarchy, including the purpose of each directory such as /etc, /bin, /usr, /var, etc.
- Users and Groups: Creating and managing users and groups, understanding the difference between system and regular users.
- Permissions: Understanding Linux file permissions and ownership, including how to modify them using chmod, chown, and chgrp commands.
- Package management: Familiarity with RPM and Yum package management systems, including how to install, remove, and update packages.
- Network configuration: Configuring network interfaces, setting IP addresses, configuring routing, understanding DNS, and troubleshooting network issues.
- Services and daemons: Managing and troubleshooting Linux services and daemons, including starting, stopping, and restarting them.
- Process management: Understanding how to manage Linux processes, including listing running processes, sending signals, and killing processes.
- Bash scripting: Familiarity with basic Bash scripting concepts, including variables, loops, conditional statements, and command-line arguments.
- System logs: Understanding system logging mechanisms and being able to analyze log files for troubleshooting purposes.
- Security: Basic understanding of Linux security concepts, including securing SSH, using firewalls, and managing users with sudo access.


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





