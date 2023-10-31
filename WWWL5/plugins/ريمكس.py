#الملف بحقوق سورس مارو @M_4_R_0
import asyncio
import random
from asyncio.exceptions import TimeoutError

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from M_4_R_0 import M_4_R_0
from ..helpers.utils import reply_id


@M_4_R_0.on(admin_cmd(outgoing=True, pattern="ريمكس$"))
async def jepvois(vois):
  rl = random.randint(3,267)
  url = f"https://t.me/REMIXv1/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="⎊︙ BY : @M_4_R_0 🎧",parse_mode="html")
  await vois.delete()
