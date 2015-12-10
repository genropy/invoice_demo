# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('state',pkey='code',name_long='State',name_plural='States',caption_field='code')
        self.sysFields(tbl,id=False)
        tbl.column('code',size='2',name_long='Code',name_short='Code',unique=True,indexed=True)
        tbl.column('name',size=':40',name_long='Name',name_short='Name',unique=True,indexed=True)
        tbl.column('tax_rate',dtype='perc', name_long='Tax rate',name_short='T.R.',unique=True,indexed=True)
