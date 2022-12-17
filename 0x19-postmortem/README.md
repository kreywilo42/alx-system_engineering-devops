# <p align="center"> **POSTMORTEM** </p>

## Issue Summary:
On the 5th of November 2022, from 10:48 AM to 11:30 AM, all requests made to access the Catfish API resulted in an internal server error.
100% of traffic was affected. Clients were not able to gain access to the API due to the service being down. The root cause of the problem was the server being overloaded with client requests.

<img src="./images/Untitled (1).jpg"
     alt="picture decipting a server error">

## Timeline (UTC):
- 10:48 AM monitoring system alerted system engineer of the crash
- 10:53 AM checked the power supply
- 10:57 AM examined server for any hardware failure
- 11:10 AM installed a HAproxy load balancer
- 11:17 AM set up another nginx server
- 11:22 AM server back up and running
- 11:30 AM traffic back to 100%


## Root Cause:
At 10:45 AM UTC the monitoring system alerted our system engineer who began to investigate the issue before it escalated.

At 10:53 AM we attempted to start the server by checking if a power supply outage was causing the crash. However, the power supply was already in good condition.

At 10:57 AM the server was examined for any hardware failure. By 11:08, the crash was reported to have been caused by the server receiving too many client requests. Due to this reason, All client requests were automatically queued. Another server was set up and we had a load balancer installed, in order to distribute the traffic between the two servers.

The servers were started by 11:22 AM, 100% of the traffic that was automatically queued were routed to the servers by the load balancer.


## Corrective and Preventive Measures
During the analysis of the crash, the following tasks were developed in order to prevent another occurrence and to improve recovery time.

- Install a load balancer to distribute client request
- Set up more nginx servers in cause of outage or crash in one
- Install another load balancer to avoid SPOF
- monitor each load balancer
- Add monitoring on each server memory
- Add monitoring on each load balancer
- Increase server memory space
- set up a server for database
- create a master-slave replication
- add monitoring on both master-slave database replication


<img src="./images/Untitled (2).jpg"
     alt="picture decipting a server error">






