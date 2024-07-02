## What Are Metrics, Monitoring and Alerting?
- Metrics represent the raw measurements of resource usage or behavior that can be observed and collected throughout your systems. These might be low-level usage summaries provided by the operating system, or they can be higher-level types of data tied to the specific functionality or work of a component, like requests served per second or membership in a pool of web servers. Some metrics are presented in relation to a total capacity, while others are represented as a rate that indicates the “busyness” of a component.
- the easiest metrics to begin with are those already exposed by your operating system to represent the usage of underlying physical resources. Data about disk space, CPU load, swap usage, etc. are already available, provide value immediately, and can be forwarded to a monitoring system without much additional work
- For other components, especially your own applications, you may have to add code or interfaces to expose the metrics you care about. Collecting and exposing metrics is sometimes known as adding instrumentation to your services.

- While metrics represent the data in your system, monitoring is the process of collecting, aggregating, and analyzing those values to improve awareness of your components’ characteristics and behavior. The data from various parts of your environment are collected into a monitoring system that is responsible for storage, aggregation, visualization, and initiating automated responses when the values meet specific requirements.
- Alerting is the responsive component of a monitoring system that performs actions based on changes in metric values. Alerts definitions are composed of two components: a metrics-based condition or threshold, and an action to perform when the values fall outside of the acceptable conditions
- While notifying responsible parties is the most common action for alerting, some programmatic responses can be triggered based on threshold violations as well. For instance, an alert that indicates that you need more CPU to process the current load can be responded to with a script that auto-scales that layer of your application.

### Host-Based Metrics
- CPU
- Memory
- Disk space
- Processes

### Application Metrics
- Error and success rates
- Service failures and restarts
- Performance and latency of responses
- Resource usage

### Network and Connectivity Metrics
- important gauges of outward-facing availability, but are also essential in ensuring that services are accessible to other machines for any systems that span more than one machine

- Connectivity
- Error rates and packet loss
- Latency
- Bandwidth utilization
