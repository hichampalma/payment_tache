from odoo import fields,models 

class PurchaseOrder(models.Model): 
    _inherit="purchase.order" 
    delivery_note=fields.Char(
        string="Numéro BL"
    ) 
    payment_method=fields.Selection(
        [
            ("check","chèque"),
            ("transfer","virement"),
            ("cash","Espèces"),
        ], 
        string="Mode de paiement"
    )