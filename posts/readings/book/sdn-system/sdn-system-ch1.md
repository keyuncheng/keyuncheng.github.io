# Reading Notes: SDN Textbook

Title: Software-Defined-Networks: A Systems Approach (Chapter 1)

Book (SDN): [Link](https://sdn.systemsapproach.org/intro.html)

## Summary

Introduction to SDN's basic concepts

## Details

* SDN goes beyond a point solution; it's a concept

* SDN principles
    * Principle 1: The interfaces between the control planes and data planes
      should be both well-defined and open
    * Principle 2: Complete disaggregation of the control plane and the data plane

* Vertical and Horizontal market
    * Example: Mainframe machine -> Microchips
    * Example: Switches -> 

* A brief introduction to OpenFlow (SIGCOMM CCR'08)
    * Controlling the data plane through the flow table

* Is it suitable to expose SDN by programmable interfaces instead of
  conventional CLI?
    * No, for the generality and performance (configurations in finer-grained
      granularity)
    
* Implementation of the control plane
    * Conventional: implement in switch (e.g. BGP); the distributed control
      plane of the Internet; problem: slow because of the slow-paced
      standardization of network protocols
    * SDN: off switch (e.g., running the controller in the cloud); benefits:
      1. scalability and availability; possible centralized network
         abstractions
        * Scenario: Network OS: logically centralized network topology;
          multiple distributed control apps in the control plane; multiple
          routers storing the flow rules (flow tables) in the data plane

* Implementation of the data plane
    * Routing: packet forwarding (through in-switch software; some high-end
      switches implement a hardware-based forwarding pipeline)
    * fixed pipelines; programmable pipelines
    * Implementation issues
        * Need to be highly efficient (fast)
        * Need to support various changing protocol stacks
    * Example: P4 (to implement forwarding pipelines)

* In short, SDN explores programable control plane and data plane