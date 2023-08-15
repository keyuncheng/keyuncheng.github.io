# Reading Notes: SDN Textbook

Title: Software-Defined-Networks: A Systems Approach (Chapter 3)

Book (SDN): [link](https://sdn.systemsapproach.org/arch.html)

## Summary

SDN's basic architecture and open-source software-stack

## Details

* Architecture
    * Network OS (network-wide) <-> switch OS (per switch)
        * virtual switch on the host machine. e.g. Open vSwitch (OVS)
        * SmartNIC assists (or replaces) vSwitch for computations
    * use gRPC as the transport protocol from Network OS to Switch OS

* Hardware
    * Switch: Tofino/Tomahawk

* Switch OS
    * Run API calls issued to the switch from Network OS
    * Example: Stratum (Google), also called as Thin Switch OS

* Network OS
    * Configuring and controlling a network of switches
    * Runs off-switch as a logically centralized SDN controller; maintaining a
      global view of the topology and the state of the network; reflecting the
      status to Control Apps through the Network APIs
    * Example: Open Network OS (ONOS)

* Leaf-spine Fabric
    * Focus on ONOS-hosted SDN Control Apps. e.g. SD-Fabric
        * SD-Fabric is a suite of Control Apps on Network OS (not a single
          App)
    * SD-Fabric is also deployed for SD-RAN for cellular networks