from sqlalchemy import (
    Column,
    Integer,
    Text,
)

from .meta import Base


class Pembeli(Base):
    __tablename__ = "pembeli"
    pembeli_id = Column(Integer, primary_key=True)
    pembeli_nama = Column(Text)
    pembeli_kontak = Column(Text)
    pembeli_alamat = Column(Text)
    pembeli_pesan = Column(Text)
