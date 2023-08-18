# Reading Notes: SDN Textbook

Title: Software-Defined-Networks: A Systems Approach (Chapter 7)

Book (SDN): [Link](https://sdn.systemsapproach.org/trellis.html)

## Summary

Leaf-Spine Fabric for SDN. Use SD-Fabric for example.

## Details

* SD-Fabric has three main features
    * Supports VLANs
    * Supports IPv4 and IPv6 for both unicast and multicast addresses
    * High availability in the face of link or switch failures

* Link aggregation and ECMP
    * Link aggregation: combine multiple physical links into a single logical
      link (more than one egress port; port groups)
    * ECMP: Equal-cost multi-path routing; multiple paths to the same
      destination with the same cost
    * Scalability: up to 120k routes and 250k flows

* Do not go into the technical details of the implementation of SD-Fabrics