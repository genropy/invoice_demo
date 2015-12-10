#!/usr/bin/env python
# encoding: utf-8
from decimal import Decimal

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('invoice', pkey='id', name_long='!!Invoice', name_plural='!!Invoice', caption_field='inv_number')
        self.sysFields(tbl)
        tbl.column('inv_number' ,size='10',name_long='!!Invoice number', name_short='Inv N')
        tbl.column('customer_id',size='22' ,group='_',name_long='!!Customer'
                                        ).relation('customer.id',
                                                    relation_name='invoices',
                                                    mode='foreignkey',
                                                    onDelete='raise')
        tbl.column('date',dtype='D',name_long='!!Date')
        tbl.column('tax_rate', dytpe='perc', name_long='Tax Rate', name_short='T.R.')
        tbl.column('total',dtype='money',name_long='!!Total')
        tbl.column('taxes',dtype='money',name_long='!!Taxes')
        tbl.column('gross_total',dtype='money',name_long='!!Gross total')

    def calculateTotals(self,invoice_id):
        with self.recordToUpdate(invoice_id) as record:
            total = self.db.table('invc.invoice_row').readColumns(columns="""SUM($tot_price)""",
                                                                                 where='$invoice_id=:invoice_id',
                                                                                 invoice_id=invoice_id)
            total=Decimal(total)
            hundred=Decimal(100)
            record['total'] = total
            record['taxes'] = Decimal((total*record['tax_rate'])/hundred)
            record['gross_total'] = record['total'] + record['taxes']

    def defaultValues(self):
        return dict(data = self.db.workdate)

    def counter_inv_number(self,record=None):
        return dict(format='$K$YY/$NNNNNN',code='I',period='YY',date_field='data',showOnLoad=True,recycle=True)