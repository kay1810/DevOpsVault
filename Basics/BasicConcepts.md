- [Basic Security Concepts](#BasicSecurityConcepts)
  * [Certificate setup](#CertificateSetup)
  * [service mesh in service to service communication ex gRPC Protocol](#service mesh in service to service communication ex gRPC Protocol)
 
- [Basic Software Concepts](https://github.com/kay1810/DevOpsVault/blob/main/Basics/BasicConcepts.md#basic-software-concepts)
  * [web server vs application server vs database server](https://github.com/kay1810/DevOpsVault/blob/main/Basics/BasicConcepts.md#web-server-vs-application-server-vs-database-server)
  * [Dotnet Application](#Dotnet Application)
  * [Nodejs Application](#Nodejs Application)
  * [Java Application](#Java Application)

- [Basic Networking Concepts](#Basic Networking Concepts)
  * [Sub-heading](#sub-heading-2)
  


## BasicSecurityConcepts


### CertificateSetup



## Basic Software Concepts


### web server vs application server vs database server

Web Server -

Server on which your website is hosted. This server will have installed web servers such as IIS, apache, etc.

Application Server -

Server on which your created applications which are utilizing your database, web service, etc. This application server will host business layer (wrapped with web services), scheduled jobs, windows services, etc.

Database Server -

Database server will have your one or more database hosted such as Oracle, Sql Server, MySql, etc.

Web, application and database server software can all run on the same physical server machine, or be distributed across multiple physical machines. Most large websites have multiple machines; most "consumer" hosting packages run on a single box.

The logical separation is as follows.

The Web server deals with HTTP(S) requests, and passes these requests on to "handlers". They have built-in handlers for file requests - HTML pages, images, CSS, JavaScript etc. You can add additional handlers for requests that they cannot manage - e.g. dynamic pages delivered by the application server. Web servers implement the HTTP specification, and know how to manage request and response headers.

The application server handles requests which create dynamic pages. So instead of serving an HTML page that is stored on the hard drive, they dynamically generate the HTML sent to the end user. Common languages/frameworks for this are Java/JSP, .Net (aspx), PHP, Ruby (on Rails or not), Python etc. Most of the time, this application server software is running on the same physical server machine as the web server.

The database server software is where the application stores its structured information. Typically, this means custom software which allows the application server to ask questions like "how many items does user x have in their basket?", using a programming language. Examples are MySQL, SQL Server, Oracle (all "relational databases"), and MongoDB, Redis and CouchDB ("NoSQL" solutions).

The database software can run on the same physical machine as the web server, but it's usually the first thing that gets hosted on separate physical hardware when the site needs to scale.

![image](https://user-images.githubusercontent.com/29191813/227700803-5e4fae38-16d8-4a05-9a0f-d57ce0d38890.png)

### Dotnet Application


### Nodejs Application


### Java Application

## Basic Networking Concepts

