#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('invoice_id')
        r.fieldcell('product_id')
        r.fieldcell('quantita')
        r.fieldcell('unit_price')
        r.fieldcell('tot_price')

    def th_order(self):
        return 'invoice_id'

    def th_query(self):
        return dict(column='invoice_id', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('invoice_id')
        fb.field('product_id')
        fb.field('quantita')
        fb.field('unit_price')
        fb.field('tot_price')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
