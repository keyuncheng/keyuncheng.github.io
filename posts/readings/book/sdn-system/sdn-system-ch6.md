# Reading Notes: SDN Textbook

Title: Software-Defined-Networks: A Systems Approach (Chapter 6)

Book (SDN): [Link](https://sdn.systemsapproach.org/onos.html)

## Summary

Network OS with ONOS as the example; only high-level ideas are covered.

## Details

* Most popular open-source: ONOS (Open Network OS)

* ONOS consists of three layers
    * A collection of Northbound Interfaces (NBI) for the information of
      network state and the control of network behavior (for Control Apps on
      top of ONOS). Think of it as an OS exposing some interfaces to the
      applications running on it for device management.
    * A Distributed Core for managing the network state and notification to
      the applications of the state changes. Atomix is the internal KVStore. 
    * A Southbound Interface constructed from a collection of plugins
      including shared protocol libraries and device-specific drivers. (e.g.,
      Cisco, Huawei, Juniper, etc.)

* Sitting on top of ONOS, there are some zero-touch management planes for
  hardware provisioning.

* Information flows both "down" and "up" to ONOS.
    * Applications use ONOS APIs to control the network
    * Southbound plugins pass information to ONOS

* ONOS comprises sub-systems, each of which is responsible for a specific
  function. The implementation is distributed.
    * KVStore: Atomix (in Java)
    * Protocol: Raft
    * Key parts: define a set of tables (maps)

* Scalability and reliability
    * Up to 50 network devices
    * High performance
    * Production systems run at least three instances for availability
        * Each instance runs on a high-performance server (e.g., 32-core CPU /
          128GB RAM)
        * Instances share the network states through Atomix with scalability
          and performance guarantee
    * New version: μONOS scales the sub-systems independently (finer-grained granularity).