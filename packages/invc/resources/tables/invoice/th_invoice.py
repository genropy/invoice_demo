#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('inv_number')
        r.fieldcell('customer_id')
        r.fieldcell('date')
        r.fieldcell('tax_rate')
        r.fieldcell('total')
        r.fieldcell('taxes')
        r.fieldcell('gross_total')

    def th_order(self):
        return 'inv_number'

    def th_query(self):
        return dict(column='inv_number', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer()
        top = bc.contentPane(region='top',datapath='.record')
        fb = top.formbuilder(cols=2, border_spacing='4px')
        fb.field('inv_number')
        fb.field('customer_id')
        fb.field('date')
        fb.field('tax_rate')
        fb.field('total')
        fb.field('taxes')
        fb.field('gross_total')
        center = bc.contentPane(region='center')
        center.plainTableHandler(relation='@rows')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
