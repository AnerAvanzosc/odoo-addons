# Copyright 2022 Daniel Campos - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Purchase Last Price Extension",
    "version": "18.0.2.0.0",
    "category": "Purchase",
    "summary": "Añade información de costos y precios históricos en líneas de pedido de compra",
    "description": """
        Extensión para módulos de compras que muestra:
        - Precio de costo actual del producto
        - Último precio de compra histórico
        - Subtotales calculados para ambos precios
        - Categoría del producto en las líneas
    """,
    "license": "AGPL-3",
    "author": "AvanzOSC",
    "website": "https://github.com/avanzosc/odoo-addons",
    "depends": [
        "purchase_last_price_info",
        "purchase_order_line_input",
    ],
    "data": [
        "views/purchase_order_line_views.xml",
    ],
    "installable": True,
    "application": False,
}