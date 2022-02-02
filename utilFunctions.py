#Hello!
#You have found my python file with nothing in it yet because I'm lazy!
#Good on you!
#Have a piece of code that does nothing :D
import asyncio


async def do_nothing(bran, teky, frame):
    if bran.lover == teky:
        await frame.display("They really do love each other!")
    else:
        while bran.in_vc:
            await asyncio.sleep(10)
            outcome = await teky.ask_out(bran)
            if outcome:
                await frame.reload(file="heartimage.png", borders=(10, 15))
                break
        if bran.awake:
            await do_nothing(bran, teky, frame)
        else:
            await frame.close(mood="sad")

