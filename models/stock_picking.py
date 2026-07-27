from odoo import fields,models 
class StockPicking(models.Model): 
    _inherit="stock.picking" 
    delivery_note = fields.Char(
        string="Numéro BL"
    )