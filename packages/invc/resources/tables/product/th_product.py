#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('code')
        r.fieldcell('product_type_id',width='30em')
        r.fieldcell('description',width='30em')
        r.fieldcell('unit_price')

    def th_order(self):
        return 'code'

    def th_query(self):
        return dict(column='description', op='contains', val='')



class Form(BaseComponent):
    py_requires='gnrcomponents/dynamicform/dynamicform:DynamicForm'
    def th_form(self, form):
        bc = form.center.borderContainer()
        self.productData(bc.borderContainer(region='top',datapath='.record',height='180px'))
        tc = bc.contentPane(region='center')
        self.productDynamicFields(tc.contentPane(title='Product details',datapath='.record'))
        self.productSells(tc.contentPane(title='Sells'))

    def productDynamicFields(self,pane):
        pane.dynamicFieldsPane('details')

    def productData(self,bc):
        left = bc.roundedGroup(region='center',title='Product info').div(margin='10px',margin_right='20px')
        fb = left.formbuilder(cols=2, border_spacing='4px',colswidth='auto',fld_width='100%',width='600px')
        fb.field('product_type_id',tag='hdbselect',validate_notnull=True,colspan=2)
        fb.field('code',validate_notnull=True,validate_case='U',validate_nodup=True)
        fb.br()
        fb.field('description',validate_notnull=True,colspan=2)
        fb.field('unit_price',validate_notnull=True)
        fb.field('vat_type_code',validate_notnull=True)
        center = bc.roundedGroup(region='right',title='Image',width='130px')
        center.img(src='^.image_url',crop_height='100px',crop_width='100px',margin='5px',
                    crop_border='2px dotted silver',crop_rounded=6,edit=True,
                    placeholder=True,upload_folder='site:products/images',
                    upload_filename='=#FORM.record.code')

    def productSells(self,pane):
        pane.plainTableHandler(relation='@invoice_rows',viewResource='ViewFromProducts')

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px',duplicate=True)
