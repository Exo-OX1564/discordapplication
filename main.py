q_list = [
    '#add a question here, you may add more by using this as an array ',
    '#add another question here, etc and carry on until you\'re done with the questions you want'
]

a_list = [] #Leave this empty


@client.command(aliases=['staff-application', 'staff-apply', 'apply']) #May add more aliases.
async def staff_application(ctx):
    sendme = client.get_channel() #Enter a channel id for the bot to send the message (check dms and a warning), the message is below. Feel free to update as likings.
    await sendme.send('**Check your DM\'s!** If you have not receieved any dms, make sure your dms are turned **on** and run the command again! Only use the command `once`. If you made a mistake, finish the current application then re-apply.')
    a_list = [] #Keave empty
    submit_channel = client.get_channel() #Enter the channel id where the bot will be able to post the answers.
    channel = await ctx.author.create_dm()

    def check(m):
        return m.content is not None and m.channel == channel

    for question in q_list:
        sleep(.5)
        await channel.send(question)
        msg = await client.wait_for('message', check=check)
        a_list.append(msg.content)

    submit_wait = True
    while submit_wait:
        await channel.send('End of questions - "submit" to finish')
        msg = await client.wait_for('message', check=check)
        if "submit" in msg.content.lower():
            submit_wait = False
            answers = "\n".join(f'{a}. {b}' for a, b in enumerate(a_list, 1))
            submit_msg = f'Application from {msg.author}.\nThe answers are:\n{answers}' #Feel free to add more to your likings.
            await submit_channel.send(submit_msg)


