import random

responses = [
        f"No problem!" ,
        f"Any time!" ,
        f"Glad I could help!" , 
        f"Just doing my job! " ,
        f"You're welcome!" ,
        f"Lemme know if there is anything else I can help with!"
        ]

async def response(message,chnl):
    
    await message.add_reaction('😉')
    
    choice = random.choice( responses )

    await chnl.send(choice)

def check_thanks(msg):
    
    if msg.find("thank") > -1:
        return 1
    
    return 0

