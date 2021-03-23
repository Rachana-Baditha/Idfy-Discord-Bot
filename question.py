import random

prediction_words = [
    'will' , 'when' , 'why' , 'how' , 'who' , 'what' , 'where' , 'is' , 'are' , 'am' , 'can'
    ]

async def should(chnl):
    
    positive_response = [
        f"Yeah, I think you should" , 
        f"Go for it!" ,
        f"Absolutely" ,
        f"I think the pros outweight the cons" , 
        f"That would be the best option" , 
        f"Sounds good to me!" ,
        f"I say yes" ,
        f"It's a YES from me" ,
        f"You should!"
        ]
    
    negative_response = [
        f"Nah, I don't think you should" ,
        f"Don't do it, man" , 
        f"Maybe you should reconsider" ,
        f"I don't like the sound of that" ,
        f"I have a bad feeling about it" ,
        f"No... just no..." , 
        f"It's a NO from me" ,
        f"That may not be the best idea" , 
        f"I say no"
        ]
    
    if random.randint(0,1):
        choice = random.choice( positive_response )
    else:
        choice = random.choice( negative_response )
        
    await chnl.send( choice )
    
def check_question(msg):
    
    for qword in prediction_words:
        if msg.startswith( f'idfy, {qword}'):
            return 1
    return 0
    
    
async def predict(chnl):
    
    responses = [
        f"Sorry, I only make decisions. I can't predict the future" , 
        f"I'm as clueless as you are here" , 
        f"I predict... that you've completely forgotten what my purpose as a bot is" , 
        f"Can't help you there, but have you tried consulting your local crystal ball?" ,
        f"I am a decision bot, so I can only make decisions. Maybe clairvoyance will come in a future update..." ,
        f"T'is one of life's greatest mysteries, indeed"
        ]
    
    choice = random.choice( responses )
    
    await chnl.send( choice )

