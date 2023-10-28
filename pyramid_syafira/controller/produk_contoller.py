from pyramid.view import view_defaults, view_config
from pyramid.request import Request
from pyramid.response import Response
from sqlalchemy.exc import DBAPIError

from ..models import Produk


@view_defaults(route_name="produk", renderer="json")
class ProdukView:
    def __init__(self, request: Request):
        self.request = request

    def server_error(self):
        response = Response("Internal server error")
        response.status_int = 500
        return response

    def not_found(self):
        response = Response("Not found")
        response.status_int = 404
        return response

    @view_config(request_method="GET")
    def get_all_produk(self):
        try:
            query = self.request.dbsession.query(Produk)
            results = query.all()
            return [
                dict(
                    id=row.id,
                    nama=row.nama,
                    jumlah=row.jumlah,
                    harga=row.harga,
                    gambar=row.gambar,
                )
                for row in results
            ]
        except DBAPIError:
            return self.server_error()

    @view_config(request_method="GET", route_name="produk_id")
    def get_produk_by_id(self):
        try:
            query = self.request.dbsession.query(Produk)
            results = query.filter_by(id=self.request.matchdict["id"]).first()
            if results:
                return dict(
                    id=results.id,
                    nama=results.nama,
                    jumlah=results.jumlah,
                    harga=results.harga,
                    gambar=results.gambar,
                )
            return self.not_found()
        except DBAPIError:
            return self.server_error()

    @view_config(request_method="POST")
    def add_produk(self):
        try:
            query = self.request.dbsession.query(Produk)
            new_produk = Produk(
                nama=self.request.json_body["nama"],
                jumlah=self.request.json_body["jumlah"],
                harga=self.request.json_body["harga"],
                gambar=self.request.json_body["gambar"],
            )
            query.add(new_produk)
            return dict(
                id=new_produk.id,
                nama=new_produk.nama,
                jumlah=new_produk.jumlah,
                harga=new_produk.harga,
                gambar=new_produk.gambar,
            )
        except DBAPIError:
            return self.server_error()

    @view_config(request_method="PUT", route_name="produk_id")
    def update_produk(self):
        try:
            query = self.request.dbsession.query(Produk)
            results = query.filter_by(id=self.request.matchdict["id"]).first()
            if results:
                results.nama = self.request.json_body["nama"]
                results.jumlah = self.request.json_body["jumlah"]
                results.harga = self.request.json_body["harga"]
                return dict(
                    id=results.id,
                    nama=results.nama,
                    jumlah=results.jumlah,
                    harga=results.harga,
                    gambar=results.gambar,
                )
            return self.not_found()
        except DBAPIError:
            return self.server_error()
