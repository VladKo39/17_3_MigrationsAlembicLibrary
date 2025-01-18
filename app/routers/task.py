from fastapi import APIRouter

router=APIRouter(prefix='/task',tags=['task'])

@router.get('/')
async def all_tasks():
    pass

@router.get('/task_id')
async def all_tasks():
    pass

@router.post('/create')
async def creat_tasks():
    pass

@router.put('/update')
async def update_tasks():
    pass

@router.delete('/delete')
async def delete_tasks():
    pass

'''
Задача "Основные маршруты":
Необходимо создать маршруты и написать Pydantic модели для дальнейшей работы.
Маршруты:
В модуле task.py напишите APIRouter с префиксом '/task' и тегом 'task',
 а также следующие маршруты, с пустыми функциями:
1.get '/' с функцией all_tasks.
2.get '/task_id' с функцией task_by_id.
3.post '/create' с функцией create_task.
4.put '/update' с функцией update_task.
5.delete '/delete' с функцией delete_task.

'''