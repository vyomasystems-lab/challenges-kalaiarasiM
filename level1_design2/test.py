# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Develop your test here! ######')
    @cocotb.coroutine
    def always_block(dut):
        while True:
            yield RisingEdge(dut.clk)
            if dut.inp_bit.value != 1:
                assert TestFailure("Failure!")
            yield RisingEdge(dut.clk)
            if dut.inp_bit.value != 0:
                assert TestFailure("Failure!")
            yield RisingEdge(dut.clk)
            if dut.inp_bit.value != 1:
                raise TestFailure("Failure!")
            yield RisingEdge(dut.clk)
            if dut.inp_bit.value != 1:
                raise TestFailure("Failure!")
    @cocotb.test()
    def test(dut):
        thread = cocotb.fork(always_block(dut))
