# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

  
sel = 5'b00010 :out
out = inp2

#input driving
dut.sel.value = inp[4:0]
dut.inp.value = inp[1:0]

await Timer(2, units='ns')

assert dut.out.value = inp[1:0], f"result is incorrect: {dut.X.value} != 2"

    cocotb.log.info('##### CTB: Develop your test here ########')
