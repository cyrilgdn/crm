# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################

from openerp import models, fields, api


class CrmClaim(models.Model):
    _inherit = "crm.claim"

    code = fields.Char(
        string='Claim Number', required=True, default="/", readonly=True)

    _sql_constraints = [
        ('crm_claim_unique_code', 'UNIQUE (code)',
         'The code must be unique!'),
    ]

    @api.model
    def create(self, vals):
        if vals.get('code', '/') == '/':
            vals['code'] = self.env['ir.sequence'].next_by_code('crm.claim')
        return super(CrmClaim, self).create(vals)

    @api.multi
    def copy(self, default=None):
        if default is None:
            default = {}
        results = self.env['crm.claim']
        for record in self:
            default['code'] = self.env['ir.sequence'].next_by_code('crm.claim')
            results |= super(CrmClaim, record).copy(default)

        return results
