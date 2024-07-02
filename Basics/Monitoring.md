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


-   Observability: Although not strictly defined, observability is a general term used to describe processes and techniques related to increasing awareness and visibility into systems. This can include monitoring, metrics, visualization, tracing, and log analysis.
-   Resource: In the context of monitoring and software systems, a resource is any exhaustible or limited dependency. What is considered a resource can vary greatly based on part of the system being discussed.
-   Latency: Latency is a measure of the time it takes to complete an action. Depending on the component, this can be a measure of processing, response, or travel time.
-   Throughput: Throughput represents the maximum rate of processing or traversal that a system can handle. This can be dependent on software or hardware design. Often there is an important distinction between theoretical throughput and practical observed throughput.
-   Performance: Performance is a general measure of how efficiently a system is completing work. Performance is an umbrella term that often encompasses work factors like throughput, latency, or resource consumption.
-   Saturation: Saturation is a measure of the amount of capacity being used. Full saturation indicates that 100% of the capacity is currently in use.
-   Visualization: Visualization is the process of presenting metrics data in a format that allows for quick, intuitive interpretation through graphs or charts.
-   Log aggregation: Log aggregation is the act of compiling, organizing, and indexing log files to allow for easier management, searching, and analysis. While separate from monitoring, aggregated logs can be used in conjunction with the monitoring system to identify causes and investigate failures.
-   Data point: A data point is a single measurement of a single metric.
-   Data set: A data set is a collection of data points for a metric.
-   Units: Units are the context for a measured value. A unit defines the magnitude, scope, or quantity of a measurement to understand extent and allow comparison.
-   Percentage Units: Percentage units are measurements that are taken as a part of a finite whole. A percentage unit indicates how much a value is out of the total possible amount.
-   Rate Units: Rate units indicate the magnitude of a metric over a constant period of time.
-   Time series: Time series data is a series of data points that represent changes over time. Most metrics are best represented by a time series because single data points often represent a value at a specific time and the resulting series of points is used to show changes over time.
-   Sampling rate: Sample rate is a measurement of how often a representative data point is collected in lieu of continuous collection. A higher sampling rate more accurately represents the measured behavior, but requires more resources to handle the extra data points.
-   Resolution: Resolution refers to the density of data points that make up a data set. Collections with higher resolutions over the same time frame indicate a higher sample rate and a more granular view of the same behavior.
-   Instrumentation: Instrumentation is the ability to track the behavior and performance of software. This is accomplished by adding code and configuration to software to output data that can then be consumed by a monitoring system.
-   The observer effect: The observer effect is the impact of the monitoring system itself on the phenomena being observed. Since monitoring takes up resources, the act of measuring behavior and performance will alter the values produced. Monitoring systems seek to avoid adding unnecessary overhead to minimize this impact.
-   Over-monitoring: Over-monitoring occurs when the quantity of metrics and alerts configured is inversely related to their usefulness. Over-monitoring can cause stress on the infrastructure, make it difficult to find relevant data, and cause teams to lose trust in their monitoring and alerting systems.
-   Alert fatigue: Alert fatigue is the human response of desensitivity that results from frequent, unreliable, or improperly prioritized alerts. Alert fatigue can cause operators to ignore severe problems and is usually an indication that alert conditions need to be reevaluated.
-   Threshold: When alerting, a threshold is the boundary between acceptable and unacceptable values which triggers an alert if exceeded. Often alerts are configured to trigger when a value exceeds the threshold for a certain period of time, in order to avoid sending an alert for temporary spikes.
-   Quantile: A quantile is a dividing point used to separate a dataset into distinct groups based on their values. Quantiles are used to put values into "buckets" that represent segments of a population of data. Often, this is used to separate common values from outliers to better understand what constitutes representative and extreme cases.
-   Trend: A trend is the general direction that a set of values is indicating. Trends are more reliable than single values in determining the general state of the component being tracked.
-   White-box monitoring: White-box monitoring is a term used to describe monitoring that relies on access to internal state of the components being measured. White-box monitoring can provide a detailed understanding of system state and is helpful for identifying causes of problems.
-   Black-box monitoring: Black-box monitoring is monitoring that observes the external state of a system or component by looking only at its inputs, outputs, and behavior. This type of monitoring can closely align with a user's experience of a system, but is less useful for finding the cause of problems.
