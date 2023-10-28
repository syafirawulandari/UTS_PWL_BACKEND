from sqlalchemy import (
    Column,
    Integer,
    Text,
)

from .meta import Base


class Produk(Base):
    __tablename__ = "produk"
    id = Column(Integer, primary_key=True)
    nama = Column(Text, nullable=False)
    jumlah = Column(Integer, nullable=False)
    harga = Column(Text, nullable=False)
    gambar = Column(Text, nullable=False)
