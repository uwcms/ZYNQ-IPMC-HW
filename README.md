! The ZYNQ-IPMC Software Framework resides [here](https://github.com/uwcms/IPMC).

# ZYNQ-IPMC Official Hardware Repository
Department of Physics, University of Wisconsin-Madison, USA

![](Documents/ZYNQ_IPMC%20revB.png)

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [ZYNQ-IPMC Official Hardware Repository](#zynq-ipmc-official-hardware-repository)
	- [1. Overview](#1-overview)
	- [2. Altium Symbol and Footprint Library](#2-altium-symbol-and-footprint-library)
	- [3. Picking between Zynq-7014S and Zynq-7020](#3-picking-between-zynq-7014s-and-zynq-7020)
	- [4. Bring-up and Testing](#4-bring-up-and-testing)
	- [5. Fabrication and Assembly](#5-fabrication-and-assembly)
		- [5.1. Fabrication Package](#51-fabrication-package)
		- [5.2. Assembly Package](#52-assembly-package)
	- [6. Disclaimer and Licensing](#6-disclaimer-and-licensing)

<!-- /TOC -->

## 1. Overview

ZYNQ-IPMC is a high versatile open-source self-contained Intelligent Platform
Management Controller (IPMC) in a miniDIMM-244 mezzanine form factor with
extended monitoring features targeted for Advance Telecommunications Computing
Architecture (ATCA) applications in accordance with the PICMG 3.x standard.

A Xilinx Zynq-7000 System-on-Chip (SoC) powers the ZYNQ-IPMC. Coupled with 256Mbytes of DDR3, fast
ADCs and a large number of GPIOs that can take any standard protocol natively,
forms an ideal solution to monitor and log voltages, currents, temperatures and others
metrics in ATCA applications.

**For detailed information of the hardware check the PDF datasheet
[here](Documents/ZYNQ-IPMC%20hw%20datasheet.pdf).**

## 2. Altium Symbol and Footprint Library

The Altium project with the ZYNQ-IPMC symbol and footprint can be found
[here](AltiumLib/).

## 3. Picking between Zynq-7014S and Zynq-7020

Both Zynq-7014S and Zynq-7020 are pin-compatible and can be assembled in the ZYNQ-IPMC.
The primary different is that the Zynq-7014S is a single core and has roughly
20% less resources than the Zynq-7020. The Zynq-7014S is also cheaper.

ZYNQ-IPMC framework only uses a single-core and won't benefit from an additional
core nor FPGA resources. Therefore, the Zynq-7014S is recommended for most applications.

From tests and experimentation a medium to high populated ZYNQ-IPMC solution requires
around 25% of resources from a Zynq-7020.

## 4. Bring-up and Testing

Standard electrical checks for hardware bring-up should be followed (e.g. visual
inspection, ohm-meter tests, voltage levels, etc.) before inserting the IPMC on a
carrier.

The [ZYNQ-IPMC Test Board](TestBoard) can be used for these tests and additional
connectivity tests.

## 5. Fabrication and Assembly

All files required to fabrication and assembly are included in this repository.
They can be found at [here](Project%20Outputs%20for%20ZYNQ_IPMC/revB1).

Recommendations on how to prepare packages for each fabrication step is below.

### 5.1. Fabrication Package

The following folders and files are recommended to be sent the PCB fabrication house:
 - Gerbers (either Gerber or GerberX2)
 - NC Drill
 - Test Points
 - PCB drawings (ZYNQ_IPMC-PCB.PDF)
 - Drill drawings (ZYNQ-IPMC-DrillDrawing.PDF)


### 5.2. Assembly Package

The following folders and files are recommended to be sent the assembly house:
 - Gerbers (either Gerber or GerberX2)
 - Bill of Materials (BOM)
 - Pick and Place
 - Assembly drawings (ZYNQ_IPMC-Assembly.PDF)

## 6. Disclaimer and Licensing

The project is distributed as-in under the MIT license agreement as seen [here](LICENSE.md).
