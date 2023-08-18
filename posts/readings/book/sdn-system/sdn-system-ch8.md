# Reading Notes: SDN Textbook

Title: Software-Defined-Networks: A Systems Approach (Chapters 8)

Book (SDN): [Link](https://sdn.systemsapproach.org/netvirt.html)

## Summary

Network Virtualization with SDN

## Details

* Network virtualization can be implemented on the servers instead of on the
switches in the physical networks.

* The concept of VPN shares common features with SDN. The original VPN did not
  separate the control and data planes as SDN.

* The first work to apply SDN to network virtualization is Nicira (NSDI'14)

* Challenges of network virtualization
    * East-to-west data traffic between servers (virtual servers)
    * Server virtualization is much quicker; the bottleneck is enabling
      the network virtualization
    * Mobility of network virtualization; applications need to be
      reconfigured when an IP is changed from one server to another server
        * Solution: decouple the addresses from the physical servers, but use
          virtual networks; thus no matter how the VM is migrated between
          physical servers, the IP can remain unchanged
        * Rationale: The IP addresses of VMs should be independent of the
          physical network topology (i.e, locations the VM resides in)
        * Implementation: virtual network encapsulations

* Architecture 
    * VLAN; VPN
    * Network Virtualization Apps expose high-level APIs for Cloud Management
      Systems to configure the virtual networks
    * Distributed scenarios
        * Example: Firewall (to avoid central bottleneck)
            * Each server has a local firewall
            * The firewall rules are distributed to the servers
            * The firewall rules are enforced by the local firewalls

* Implementation
    * Virtual Network Encapsulation: GENEVE
    * Virtual Switches: Open vSwitch (NSDI'15), implemented in the data plane
      of the hypervisor
    * Virtual switches has performance issues (e.g., packet processing). E.g.,
      for Open vSwitch, ReadHat Developers have done a measurement.
        * Solutions: Hardware offloading (e.g., DPDK, SmartNICs)

* Example network virtualization system: Open Virtual Network

* Since Nicira's first work, Cisco and VMWare are improving the techs.
    * E.g., microsegmentation (security issue)

  