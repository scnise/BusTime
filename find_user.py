import aiosqlite
async def find_user(a):
    async with aiosqlite.connect("bot_data.db") as db:
        cursor = await db.execute("SELECT * FROM users WHERE userid = ?;",(a,))
        res = await cursor.fetchone()
        if res:
            return res
        else:
            return None