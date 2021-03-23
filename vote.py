import asyncio

cas_rules = """Voting will now begin. 
Please case your vote by reacting to the candidate you wish to vote for. 
Note: You can vote for multiple candidates. 

Only ✅ reactions will be counted towards the total 
You will be given 7 seconds for each option. 

Let's Begin!

"""
    
async def casual(chnl,client):
    
    await chnl.send("Enter candidates separated by '//' ")
    
    while(True):
        
        options = await client.wait_for('message')
        
        if options.author != client.user:
            break
    
    options = options.content
    
    await chnl.send(cas_rules)
    
    options = options.split("//")
    
    count = []
    
    for i in range( len(options) ):
        
        new_msg = await chnl.send(f"Option #{i+1}: {options[i]}")
        
        await new_msg.add_reaction('✅')
        
        await asyncio.sleep(10)
        
        new_msg = chnl.last_message
        
        count.append( new_msg.reactions[0].count )
        
        
    win_count = max( count )
    win_vote = ''
    
    if win_count == 0:
        
        await chnl.send("Oops! Look's like no one voted for anything!")
    
    else:
    
        for i in range( len(count) ):
        
            if count[i] == win_count:
                win_vote = win_vote + options[i] + ', '
        
        await chnl.send(f"\nWinner(s): {win_vote} \nNumber of Votes: {win_count -1}")

        
    
    
    
    
    


