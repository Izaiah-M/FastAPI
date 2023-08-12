

async def get_all(collection):
    data_cursor = collection.find()

    res = []

    async for data in data_cursor:
        res.append(data)
    
    return res

async def get_one(collection, query_object : object):
    data = await collection.find_one(query_object)

    return data


async def insert_one(collection, query_object : object):
    pass