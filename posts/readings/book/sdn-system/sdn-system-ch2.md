# Reading Notes: SDN Textbook

Title: Software-Defined-Networks: A Systems Approach (Chapter 2)

Book (SDN): [link](https://sdn.systemsapproach.org/uses.html)

## Summary

Use cases of SDN.

## Details

* Deployment
    * Companies (Proprietary)
        * Google, Microsoft, Facebook
    * Network operators
        * AT&T, DT, NTT
        * Comcast (open-source)
    * Adoption of SDN in the enterprise is slow
        * Some of the focus: local control planes centralization
    
* Some solutions of SDN
    * VPN (widely adopted solution of WAN)
    * VLAN (virtualization of address spaces)

* The idea of using SDN to create virtual networks: (NSDI'14 T. Koponen)

* Datacenter switching fabric (leaf-spine topology)
    * Leaf: ToR (Top of Rack) switch
    * Spine: Aggregation switch; usually two for resilience
    * Two hops from any rack to any other rack through a leaf-spine-leaf  

* Traffic engineering
    * Examples: Google B4 (SIGCOMM'18); Microsoft SWAN (SIGCOMM'13)
    * MPLS-based traffic engineering is local; not globally optimal
    * Centralizing the decision-making process and rate-limiting traffic, and
      differentiating classes of traffic, Google and MS reported the link
      utilization to be nearly 100%.

* SD-WAN
    * SD-WAN is a WAN solution that uses SDN to provide a centralized control
      plane for a WAN.
    * The most common approach is MPLS-BGP VPNs. SD-WAN is an alternative with
      centralized control.
        * MPLS requires significant local configurations on both customer
          sites and provider sites.
        * SD-WAN realizes centralized configuration.
        * Security: encrypted tunnels between edge sites.
            * Conventional VPN needs backhaul (travel to the central site
              before sending out to the Internet); For SD-WAN, it doesn't
              need, as the data plane remains fully distributed

* Access Networks
    * Passive Optical Networks (PON) for fiber-to-home networks; Radio Access
      Networks (RANs) for cellular networks
    * Challenges: transform purpose-built devices for Access Networks to
      bare-metal hardware for software control.
    * Concept: SD-RAN (5G-empowered edge cloud; implement SDN in RANs)

* Network Telemetry
    * INT: In-band Network Telemetry
        * INT is a framework for collecting telemetry data from the data plane
          of a network. It encodes the telemetry information into packet
          headers. Each packet collects measurement data as it traverses the
          network.
    * INT can be used for network debugging, traffic engineering, and
      performance monitoring.