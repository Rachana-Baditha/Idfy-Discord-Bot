import random

greet_list = [
    'hello' , 'hi' , 'hey' , 'yo'
    ]

def check_greet(msg):
    
    for greet in greet_list:
        if msg.find(greet) > -1:
            return 1
    return 0

async def response(message, chnl, friend):
    
    await message.add_reaction("😊")
    
    responses = [
        f"Hello there, {friend}!" , 
        f"Hey {friend}!" , 
        f"Nice to see you, {friend}!" , 
        f"Hello to you too, {friend}!" ,
        f"Hiiiiiiiiiiiii {friend}!"
        ]
    
    choice = random.choice(responses)
    
    await chnl.send( choice )


