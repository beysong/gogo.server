

from app.extensions import db
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import func, Boolean, DateTime, Integer

# 定义通用基类
class Base(DeclarativeBase):
    __abstract__ = True  # 声明为抽象基类，不能直接实例化

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime, onupdate=func.now())
    is_delete: Mapped[bool] = mapped_column(Boolean, default=False)

# 将通用基类与 SQLAlchemy 关联
Base.metadata = db.metadata
