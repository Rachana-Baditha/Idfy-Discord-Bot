import Impy_Info 

async def intro(chnl):
    
    await chnl.send(Impy_Info.Introduction)
    
async def commands(chnl):
    
    await chnl.send(Impy_Info.Commands)


