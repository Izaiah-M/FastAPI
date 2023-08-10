

async def get_all(db):
    data_cursor = db.find()

    res = []

    async for data in data_cursor:
        res.append(data)
    
    return res

async def get_one(db, query_object : object):
    data = await db.find_one(query_object)

    return data

