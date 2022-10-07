// Copyright (c) 2022, sammish and contributors
// For license information, please see license.txt

frappe.ui.form.on('Central Kitchen', {
	get_item: function(frm){
		console.log('get item')
		if (cur_frm.doc.bom){
			cur_frm.call({
				doc:cur_frm.doc,
				method:'get_item',
				args:{
				},
			})
		}
		else{
			frappe.throw('please select BOM first')
		}
	}
});
