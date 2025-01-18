from fastapi import APIRouter

router=APIRouter(prefix='/user',tags=['user'])

@router.get('/')
async def all_users():
    pass

@router.get('/user_id')
async def user_by_id():
    pass

@router.post('/create')
async def create_user():
    pass

@router.put('/update')
async def update_user():
    pass

@router.delete('/delete')
async def delete_user():
    pass

'''
Задача "Основные маршруты":
Необходимо создать маршруты и написать Pydantic модели для дальнейшей работы.
Маршруты:
В модуле user.py напишите APIRouter с префиксом '/user' и тегом 'user',
 а также следующие маршруты, с пустыми функциями:
1.get '/' с функцией all_users.
2.get '/user_id' с функцией user_by_id.
3.post '/create' с функцией create_user.
4.put '/update' с функцией update_user.
5.delete '/delete' с функцией delete_user.
'''