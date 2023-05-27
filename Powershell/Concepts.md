Basics :
- Windows PowerShell is a command-line shell and associated scripting language created by Microsoft. It is built on the .NET framework. The commands in the Windows PowerShell are called cmdlets, which allow you to manage the computer from the command line.
- It is the new shell of Microsoft which combines the old command prompt (CMD) functionality with a new scripting instruction set with built-in system administration functionality.
- It is designed especially for the system administrators. Its analogue in Linux OS is called as a Bash scripting.
- There are four different types of execution policy in PowerShell
   1.Restricted: In this policy, no script is executed.
   2.RemoteSigned: In this policy, only those scripts are run, which are downloaded from the Internet, and these must be signed by the trusted publisher.
   3.Unrestricted: All the scripts of Windows PowerShell are run.
   4.AllSigned: Only those scripts can be run, which are signed by a trusted publisher.
   5.Bypass
- command to update execution policy : Set-ExecutionPolicy "type"
- The matching operators are those operators, which compare the strings using regular expression or wildcard characters to find a match.
