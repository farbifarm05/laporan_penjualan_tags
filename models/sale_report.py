from odoo import fields, models

class SaleReport(models.Model):
    _inherit = "sale.report"

    x_sale_tags = fields.Char(
        string='Tags',
        readonly=True
    )
    
    product_name_only = fields.Char(
        string='Nama Produk Bersih',
        readonly=True
    )

    product_category_name = fields.Char(
        string='Kategori Produk',
        readonly=True
    )

    product_default_code = fields.Char(
        string='Kode Produk',
        readonly=True
    )

    def _select_sale(self):
        select_sql = super()._select_sale()
        lang = self.env.context.get('lang') or 'en_US'
        
        select_sql += f""",
            (SELECT string_agg(tag.name->>'{lang}', ', ')
             FROM sale_order_tag_rel rel
             JOIN crm_tag tag ON rel.tag_id = tag.id
             WHERE rel.order_id = s.id) AS x_sale_tags,
             
            (SELECT
                CASE
                    WHEN (pt.name->>'{lang}') LIKE '%%] %%' THEN split_part((pt.name->>'{lang}'), '] ', 2)
                    ELSE (pt.name->>'{lang}')
                END
             FROM product_product p
             JOIN product_template pt ON (p.product_tmpl_id = pt.id)
             WHERE p.id = l.product_id) AS product_name_only,

            (SELECT split_part(pc.name, ' / ', -1)
             FROM product_product p
             JOIN product_template pt ON (p.product_tmpl_id = pt.id)
             JOIN product_category pc ON (pt.categ_id = pc.id)
             WHERE p.id = l.product_id) AS product_category_name,

            (SELECT pp.default_code
             FROM product_product pp
             WHERE pp.id = l.product_id) AS product_default_code
        """
        return select_sql

    def _group_by_sale(self):
        group_by_sql = super()._group_by_sale()
        group_by_sql += ", s.id"
        return group_by_sql

    def _select_pos(self):
        select_sql = super()._select_pos()
        lang = self.env.context.get('lang') or 'en_US'
        
        select_sql += f""",
            NULL AS x_sale_tags,
            (SELECT CASE WHEN (pt.name->>'{lang}') LIKE '%%] %%' THEN split_part((pt.name->>'{lang}'), '] ', 2) ELSE (pt.name->>'{lang}') END FROM product_product p JOIN product_template pt ON (p.product_tmpl_id = pt.id) WHERE p.id = l.product_id) AS product_name_only,
            (SELECT split_part(pc.name, ' / ', -1) FROM product_product p JOIN product_template pt ON (p.product_tmpl_id = pt.id) JOIN product_category pc ON (pt.categ_id = pc.id) WHERE p.id = l.product_id) AS product_category_name,
            (SELECT default_code FROM product_product WHERE id = l.product_id) AS product_default_code
        """
        return select_sql