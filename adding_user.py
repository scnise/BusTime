import asyncio
import aiosqlite
async def adding_user(a,b,c):
     async with aiosqlite.connect("bot_data.db") as db:
          cursor = await db.execute("SELECT * FROM users WHERE userid = ?;",(a,))
          res = await cursor.fetchone()
          if not res:
               await db.execute("INSERT INTO users (userid, username, start_time) VALUES (? , ?, ?);", (a,b,c))
               await db.commit()