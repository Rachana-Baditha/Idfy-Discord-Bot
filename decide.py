import random

#Decision Functions 

async def between(msg,chnl):
    
    options = msg.partition(" between ")[2]
    
    options = options.split(" and ")
    
    choice = random.choice(options).lstrip()
    
    await chnl.send( response(choice) )

async def among(msg,chnl):
    
    options = msg.partition(" among ")[2]
    
    options = options.split(",")
    
    choice = random.choice(options).lstrip()
    
    await chnl.send( response(choice) )

async def coinflip(chnl):
    
    if random.randint(0,1):
        choice = "Heads"
    
    else:
        choice = "Tails"
    
    await chnl.send( response_coin(choice) )

def response(choice):
    
    responses = [
        f"I choose {choice}" ,
        f"Let's go with {choice}",
        f"Maybe {choice}" ,
        f"How about {choice}?",
        f"I think {choice} would work well" ,
        f"{choice} sounds good to me!" ,
        f"I like {choice}!" , 
        f"I'd have to say {choice}" , 
        f"I think I'll go with {choice}" ,
        f"I'm really vibing with {choice}"
        ]
    
    return random.choice(responses)

def response_coin(choice):
    responses =  [
        f"It says {choice}",
        f"{choice} it is!" ,
        f"You got {choice}" ,
        f"{choice}!"
        ]
    
    return random.choice(responses)