# Reading Notes: SDN Textbook

Title: Software-Defined-Networks: A Systems Approach (Chapter 5)

Book (SDN): [link](https://sdn.systemsapproach.org/stratum.html)

## Summary

Switch OS (with Stratum as an example); only high-level ideas are covered.

## Details

* Most popular: Open Network Linux (ONL), Stratum, SONiC

* Focus: the Northbound Interface (NBI) exported by the Switch OS to the
  control plane

* NBI for Stratum
    * P4Runtime, gNMI, gNOI
    * P4Runtime is used to control the switch's forwarding behaviors
    * gNMI is used to configure the switch
    * gNOI is to access other operational variables on the switch

* Another Switch OS example: SONiC
    * Vendor-agnostic getting attention in the industry
    * NBI: gNMI, gNOI