def includeme(config):
    config.add_static_view("static", "static", cache_max_age=3600)
    config.add_route("home", "/")
    config.add_route("produk", "/api/produk")
    config.add_route("produk_id", "/api/produk/{id}")
