from sqlalchemy.schema import Column, ForeignKey  # type: ignore
from sqlalchemy.types import String, Integer, BigInteger, Date, DateTime  # type: ignore
from sqlalchemy.orm import relationship  # type: ignore
from sqlalchemy.sql import func  # type: ignore

from .database import Base


class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    province = Column(String(100), unique=True, nullable=False, comment='省/直辖市')
    country = Column(String(100), unique=True, nullable=False, comment='国家')
    country_code = Column(String(100), unique=True, nullable=False, comment='国家代码')
    country_population = Column(BigInteger, unique=True, nullable=False, comment='人口')
    data = relationship('Data', back_populates='city', comment='数据')
    created_at = Column(DateTime, server_default=func.now(), comment='创建时间')
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment='更新时间')

    __mapper_args__ = {"order_by": country_code}  # 默认是正序，倒序需要加上 .desc() 方法

    def __repr__(self):
        return f'{self.country}_{self.province}'


class Data(Base):
    __tablename__ = 'data'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    city_id = Column(Integer, ForeignKey('City.id'), comment='外键(关联City表id)')
    date = Column(Date, nullable=False, comment='数据日期')
    confirmed = Column(BigInteger, default=0, nullable=False, comment='确诊数量')
    deaths = Column(BigInteger, default=0, nullable=False, comment='死亡数量')
    recovered = Column(BigInteger, default=0, nullable=False, comment='痊愈数量')
    city = relationship('City', back_populates='data')

    created_at = Column(DateTime, server_default=func.now(), comment='创建时间')
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment='更新时间')

    __mapper_args__ = {"order_by": date.desc()}  # 默认是正序，倒序需要加上 .desc() 方法

    def __repr__(self):
        return f'{self.date.__repr__(): 确诊:{self.confirmed}}'