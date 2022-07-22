# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def randomised_test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
for i in range(30):
    SEL = random.randint(0, 4)
    INP = random.randint(0,30) 
        
        dut.sel.value = SEL
        dut.inp.value = INP
         await Timer(2, units='ns')
            
            dut._log.info(f'INP={INP:30} model={SEL==INP} DUT={int(dut.out.value):30}')
            
            assert dut.out.value == INP, "Randomised test failed with: {INP} = {OUT}".format
            (SEL=dut.sel.value, INP=dut.inp.value, OUT=dut.out.value)
        
