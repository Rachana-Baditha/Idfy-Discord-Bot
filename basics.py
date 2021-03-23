import Idfy_Info 

async def intro(chnl):
    
    await chnl.send(Idfy_Info.Introduction)
    
async def commands(chnl):
    
    await chnl.send(Idfy_Info.Commands)


