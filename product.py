class Product:
    def __init__(self, name, fec_alta, codigo_zip, credit_card_num, credit_card_ccv, cuenta_numero_direccion, geo_latitud, geo_longitud, color_favorito, foto_dni, auto, auto_modelo, auto_tipo, auto_color):
        self.name = name
        self.fec_alta = fec_alta
        self.codigo_zip = codigo_zip
        self.credit_card_num = credit_card_num
        self.credit_card_ccv = credit_card_ccv
        self.cuenta_numero_direccion = cuenta_numero_direccion
        self.geo_latitud = geo_latitud
        self.geo_longitud = geo_longitud
        self.color_favorito = color_favorito
        self.foto_dni = foto_dni
        self.auto = auto
        self.auto_modelo = auto_modelo
        self.auto_tipo = auto_tipo
        self.auto_color = auto_color

    def toDBCollection(self):
        return{
            'name': self.name,
            'fec_alta': self.fec_alta,
            'codigo_zip': self.codigo_zip,
            'credit_card_num': self.credit_card_num,
            'credit_card_ccv': self.credit_card_ccv,
            'cuenta_numero_direccion': self.cuenta_numero_direccion,
            'geo_latitud': self.geo_latitud,
            'geo_longitud': self.geo_longitud,
            'color_favorito': self.color_favorito,
            'foto_dni': self.foto_dni,
            'auto': self.auto,
            'auto_modelo': self.auto_modelo,
            'auto_tipo': self.auto_tipo,
            'auto_color': self.auto_color
        }
