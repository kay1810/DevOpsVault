# General Concepts
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





