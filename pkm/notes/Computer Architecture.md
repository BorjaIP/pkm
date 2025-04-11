---
title: Computer Architecture
created: Saturday 22nd April 2023 21:55
aliases:
  - arq
tags:
  - arq
---
**Computer architecture** is the design and organization of computing systems, encompassing how hardware components work together to execute instructions and process data. It represents the conceptual blueprint and structural framework that defines a computer system's functionality, performance, and capabilities.
# Fundamentals

## Von Neumann Architecture

- Single memory space for both instructions and data
- Sequential instruction execution
- Characterized by the "von Neumann bottleneck" between processor and memory
- Still forms the foundation of most modern computing systems

## Harvard Architecture

- Physically separate storage and signal pathways for instructions and data
- Allows simultaneous access to both instruction and data memory
- Common in DSPs and microcontrollers
- Reduces the memory bottleneck for certain applications

## Instruction Set Architecture

- ISA: The interface between hardware and software, defining the set of instructions a processor can execute, addressing modes, registers, and data type.
## Instruction Cycle (Fetch-Decode-Execute)
# CPU Design

- ALU (Arithmetic Logic Unit)
- Control Unit
- Registers
- Pipelining & Hazards
# Memory Hierarchy

- Registers
- Cache (L1, L2, L3)
- RAM
- Virtual Memory & Paging
## Memory-Centric Architectures

- Non-von Neumann approaches
- Neuromorphic computing
- In-memory computing
- Near-data processing
# I/O System

- System Buses (Data, Address, Control)
- I/O Interfaces
- Interrupts & DMA
# Performance

- Clock Speed & CPI
- Benchmarks & MIPS/FLOPS
## Parallel Processing Architectures

- **SIMD** (Single Instruction, Multiple Data): Same operation performed on multiple data points simultaneously
- **MIMD** (Multiple Instruction, Multiple Data): Multiple processors executing different instructions on different data
- **Vector Processing**: Specialized for operations on data arrays
- **GPU Architecture**: Optimized for graphics and highly parallel computation
# Modern Architectures

## RISC (Reduced Instruction Set Computer)

- Simple, highly-optimized instruction set
- Fixed instruction length
- Large number of general-purpose registers
- Load-store architecture
- Examples: ARM, RISC-V, early MIPS
## CISC (Complex Instruction Set Computer)

- Rich instruction set with many specialized instructions
- Variable instruction length
- Fewer registers
- Memory-to-memory operations
- Example: x86 architecture
## Superscalar & Out-of-Order Execution

# Specialized Architectures

- **FPGA-based**: Reconfigurable hardware
- **ASIC**: Application-specific integrated circuits
- **Quantum Computing**: Based on quantum mechanical principles
- **AI Accelerators**: Specialized for machine learning workloads (TPUs, NPUs)
