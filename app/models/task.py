from app.backend.db import Base
# импортируется класс Base из модуля app.backend.db
from sqlalchemy import ForeignKey
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

from app.models import user


class Task(Base):
    __tablename__ = 'tasks'
    # задаёт название таблицы для модели в базе данных
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    # определение столбца id в SQLAlchemy, который будет представлять первичный ключ и иметь индекс.
    title: Mapped[Optional[str]]
    # определение столбца в SQLAlchemy, представляет собой обязательную строку
    content: Mapped[Optional[str]]
    priority: Mapped[Optional[int]] = mapped_column(default=0)
    # определение столбца в SQLAlchemy, представляет собой обязательную строку по умолчанию 0
    completed: Mapped[Optional[bool]] = mapped_column(default=False)
    # определение столбца в SQLAlchemy, представляет собой обязательную строку булево по умолчанию False
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False, index=True)
    # определение столбца в SQLAlchemy, представляет собой строку,является внешним ключём
    slug: Mapped[Optional[str]] = mapped_column(unique=True, index=True)
    # определение столбца, представляет строку, уникально, имеет индекс

    user: Mapped['User'] = relationship('user', back_populates='tasks')
    # устанавливает связь между User и Task,
    # где параметр back_populates указывает,
    # что в модели Task будет соответствующий атрибут, который ссылается на модель User.


print(CreateTable(Task.__table__))
