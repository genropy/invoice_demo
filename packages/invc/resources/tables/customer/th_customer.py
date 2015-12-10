#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('account_name')
        r.fieldcell('street_address')
        r.fieldcell('city')
        r.fieldcell('state')
        r.fieldcell('customer_type_code')
        r.fieldcell('payment_type_code')
        r.fieldcell('notes')
        r.fieldcell('email')

    def th_order(self):
        return 'account_name'

    def th_query(self):
        return dict(column='account_name', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('account_name')
        fb.field('street_address')
        fb.field('city')
        fb.field('state')
        fb.field('customer_type_code')
        fb.field('payment_type_code')
        fb.field('notes')
        fb.field('email')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
