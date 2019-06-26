# ZYNQ-IPMC Test Board

This is dual-layer board intended for bring-up and light development of ZYNQ-IPMC.
The Test Board was designed for ZYNQ-IPMC revAs but it works just as well with revBs.

## Power from 3.3V

The Test Board uses a custom DC/DC power converter that converts from 12V to 3.3V.
This can be bypassed by wired a benchtop power supply set to 3.3V directly to the
3.3V pins as marked on the PCB silkscreen.

## Control and IPMC slots

The Control slot on the Test Board is to be used as a simulated Shelf endpoint -
this was never developed however. It is still used for testing with the Python Test
Suite as described below.

The IPMC slot is where the target ZYNQ-IPMC under-testing should be placed.

## Python Test Suite

The [Python test script](ipmc_testsuite.py) expects the serial COM to the IPMC to be
available in ```/dev/ttyUSB0``` and the Control IPMC in ```/dev/ttyUSB1```. Both need to
be booted into ***fallback firmware***. This can be changed my modifying the script.

Several connectivity tests between both cards will be executed and a final status
report will be presented. This is useful to verify if pins are shorted/floating.
