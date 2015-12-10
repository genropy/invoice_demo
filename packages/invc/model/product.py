#!/usr/bin/env python
# encoding: utf-8

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('product', pkey='id', name_long='!!Product', name_plural='!!Prodocts',caption_field='description')
        self.sysFields(tbl)
        tbl.column('code' ,size=':10',name_long='!!Code')
        tbl.column('description' ,size=':50',name_long='!!Description')
        tbl.column('product_type_id',size='22' ,group='_',name_long='!!Product type',name_short='Type').relation('product_type.id',relation_name='products',mode='foreignkey',onDelete='raise')
        tbl.column('price',dtype='money',name_long='!!Price',name_short='Price')
        tbl.column('image_url' ,dtype='P',name_long='!!Image',name_short='Img')
        tbl.column('details',dtype='X',name_long='!!Details',subfields='product_type_id')