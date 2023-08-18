# Reading Notes: SDN Textbook

Title: Software-Defined-Networks: A Systems Approach (Chapter 4)

Book (SDN): [Link](https://sdn.systemsapproach.org/switch.html)

## Summary

Introduction to bare-metal switches. I don't read the low-level technical details.

## Details

* Network Processing Unit (NPU)
    * A specialized processor for packet processing
    * Forwarding pipeline + SRAM packet buffers

* Programmable pipeline of packet processing
    * Programmable parser/deparser with P4
    * P4 compiler will allocate the resources to realize the pipeline

* Examples of P4 architecture programs
    * V1Model
    * Tofino

* P4 language
    * Close to C; designed for low-level system codes
    * Headers and metadata, parser, ingress processing, egress processing,
      deparser (opposite to parser)

* Fixed-function pipelines still dominate the markets
    * Example: OpenFlow-Data Plane Abstraction (OF-DPA)
    * Low-level chip interfaces maybe proprietary (e.g. Broadcom SDK)

* Switch Abstraction Interface (SAI)
    * vendor-defined and communinity-defined logical fixed-function pipelines
    * All vendors can agree on
    * The future trend