import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure
@cocotb.test()
def test_mux(dut):
    """Test for mux2"""
    cocotb.log.info('##### CTB: Develop your test here ########')
    dut.inp0.value = 0
    dut.inp1.value = 3
    dut.inp2.value = 1
    dut.inp3.value = 2
    dut.inp4.value = 2
    dut.inp5.value = 2
    dut.inp6.value = 2
    dut.inp7.value = 2
    dut.inp8.value = 2
    dut.inp9.value = 3
    dut.inp10.value = 0
    dut.inp11.value = 2
    dut.inp12.value = 2
    dut.inp13.value = 3
    dut.inp14.value = 3
    dut.inp15.value = 2
    dut.inp16.value = 0
    dut.inp17.value = 3
    dut.inp18.value = 0
    dut.inp19.value = 0
    dut.inp20.value = 0
    dut.inp21.value = 0
    dut.inp22.value = 1
    dut.inp23.value = 0
    dut.inp24.value = 0
    dut.inp25.value = 0
    dut.inp26.value = 0
    dut.inp27.value = 0
    dut.inp28.value = 0
    dut.inp29.value = 0
    dut.inp30.value = 3  

    dut.sel.value = 1
    yield Timer(1, "ns") 
    if  dut.out.value != 3:
        raise TestFailure("Failure!")