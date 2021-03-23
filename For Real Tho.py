import discord
import decide
import greetings
import question
import thanks
import vote
import basics
from Idfy_t import Token

client = discord.Client()

def say_idfy(msg):
    
    if msg.find("idfy") > -1:
        return 1
    
    return 0

@client.event
async def on_ready():
    print(f"{client.user} is now live!")
    
@client.event
async def on_message(message):
    
    msg = message.content.lower()
    chnl = message.channel
    
    if message.author == client.user:
        return
    
    #Basics
    
    elif msg.startswith("idfy, intro"):
        
        await basics.intro(chnl)
        
    elif msg.startswith("idfy, commands"):
        
        await basics.commands(chnl)
    
    #Decisions
    
    elif msg.startswith("idfy, decide between"):
        
        await decide.between(msg,chnl)
        
    elif msg.startswith("idfy, decide among"):
        
        await decide.among(msg,chnl)
        
    elif msg.startswith("idfy, flip a coin"):
        
        await decide.coinflip(chnl)
        
    #Voting
        
    elif msg.startswith("idfy, vote fpp"):
        
        vote.fpp(msg)
        
    elif msg.startswith("idfy, vote av"):

        vote.av(msg)
        
    elif msg.startswith("idfy, vote"):
        
        await vote.casual(chnl,client) 
        
    #Questions
        
    elif msg.startswith("idfy, should"):
        
        await question.should(chnl) 
        
    elif question.check_question(msg):
        
        await question.predict(chnl) 
        
    #Thanks
        
    elif thanks.check_thanks(msg) and say_idfy(msg):
        
        await thanks.response(message,chnl)  
   
    #Greetings
    
    elif greetings.check_greet(msg) and  say_idfy(msg):
        
        
        await greetings.response(message,chnl,message.author.name) 
        
    
client.run(Token)
    


