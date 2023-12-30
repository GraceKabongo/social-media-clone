from fastapi import APIRouter, HTTPException
from models.userModel import UserModel, UpdateUserModel,user_serializer
from db import user_collection
from pymongo import ReturnDocument

from bson import ObjectId

router = APIRouter(prefix="/user")


@router.get("/")
async def get_all_users():
    users = []
    
    async for user in user_collection.find():
        users.append(user_serializer(user))
    
    return users


@router.get("/{userID}")
async def get_user(userID: str):
    
    if not ObjectId.is_valid(userID):
        raise HTTPException(status_code=404, detail=f"UNKNOWN ID : {userID}")
    else:
        user = await user_collection.find_one({"_id" : ObjectId(userID)})
        if not user:
            raise HTTPException(status_code=404, detail=f"COULDN'T FIND USER : {userID}")
    
    return user_serializer(user)


@router.post("/")
async def create_user(user: UserModel):
    username = await user_collection.find_one({"username": user.username})
    email = await user_collection.find_one({"email": user.email})
    
    if username or email :
        raise HTTPException(status_code=400, detail="USERNAME OR EMAIL ALREADY TAKEN")
    
    user = await user_collection.insert_one(dict(user))
    new_user = await user_collection.find_one({"_id": user.inserted_id})
    
    return user_serializer(new_user)



@router.put("/{userID}")
async def update_user(userID: str, data: UpdateUserModel):
    if not ObjectId.is_valid(userID):
        raise HTTPException(status_code=404, detail=f"UNKNOWN ID : {userID}")
    else: 

        user = await user_collection.find_one_and_update(
                                                {
                                                    "_id" : ObjectId(userID)
                                                }, 
                                                {
                                                    "$set" : 
                                                    {
                                                        "fullname": data.fullname,
                                                        "bio" : data.bio
                                                    }
                                                }
                                                , return_document=ReturnDocument.AFTER)
        
        if not user:
            raise HTTPException(status_code=404, detail=f"COULDN'T FIND USER : {userID}")
    
    print (type(user))
    return user_serializer(user)


@router.delete("/{userID}")
async def delete_user(userID: str):
    if not ObjectId.is_valid(userID):
        raise HTTPException(status_code=404, detail=f"UNKNOWN ID : {userID}")
    else:
        user = await user_collection.find_one_and_delete({"_id": ObjectId(userID)})
        if not user:
            raise HTTPException(status_code=404, detail=f"COULDN'T FIND USER : {userID}")
        
    return {"Message" : f"{userID} HAS BEEN DELETED"}
