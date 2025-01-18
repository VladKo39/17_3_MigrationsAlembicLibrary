from app.backend.db import Base
# импортируется класс Base из модуля app.backend.db
# определяет внешний ключ, указывающий на связь столбца с другой таблицей
from sqlalchemy.orm import Mapped, mapped_column, relationship
# импорт необходимых функций для работы с моделями SQLAlchemy
# Mapped позволяет более лаконично и понятно описывать модели.
# mapped_column — функция создания колонок в моделях SQLAlchemy.
# Она принимает в качестве аргументов тип данных колонки и дополнительные параметры,
# такие как primary_key, nullable, default и так далее.
# relationship позволяет связать объекты друг с другом при создании, и SQLAlchemy
# автоматически определит, к каким записям они относятся.
from sqlalchemy.schema import CreateTable
# генерация оператора CREATE TABLE в SQLAlchemy
from typing import Optional
# Optional позволяет указать, что переменная может принимать
# значения определённого типа T или быть равной None.
# При этом тип опциональной переменной указывается в квадратных скобках


class User(Base):
    __tablename__ = 'users'
    # задаёт название таблицы для модели User в базе данных
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    # определение столбца id, представляет первичный ключ и иметь индекс.
    username: Mapped[Optional[str]]
    # определение столбца
    firstname: Mapped[Optional[str]]
    # определение столбца
    lastname: Mapped[Optional[str]]
    # определение столбца
    age: Mapped[Optional[int]]
    # определение столбца
    slug: Mapped[Optional[str]] = mapped_column(unique=True, index=True)
    # определение столбца, представляет строку, уникально, имеет индекс

    tasks: Mapped['Task'] = relationship('tasks', back_populates='user')
#  tasks: Mapped[List['Task']] = relationship(back_populates='user')

print(CreateTable(User.__table__))
