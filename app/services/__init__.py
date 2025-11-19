from uuid import uuid4

def crud_create(db, item):
    item_id = str(uuid4())
    db[item_id] = item.dict()
    return {"id": item_id, **db[item_id]}

def crud_read_all(db):
    return [{"id": k, **v} for k, v in db.items()]

def crud_read_one(db, item_id):
    return {"id": item_id, **db[item_id]}

def crud_update(db, item_id, item):
    db[item_id] = item.dict()
    return {"id": item_id, **db[item_id]}

def crud_delete(db, item_id):
    del db[item_id]
    return {"success": True}