(function(){

let itemTemplate = "<tr id={{id}}><td>{{id}}</td><td>{{title}}</td><td>{{description}}</td><td><button onclick='fn.destroyItem({{id}})'>X</button></td><tr>";

let fn = {};

fn.getAllItems = () => {
	$.ajax({
        type: 'GET',
	    url: '/api/v1/item/all'
	}).done(
		(items) => {
			let itemTable = $('#itemsTable');
			items.forEach(function(item){
				itemTable.append(Mustache.render(itemTemplate, item));
			})
		}
	).fail(
		(err) => {

	    }
	)	 
}

fn.clearTable = () => {
	let itemTable = $('#itemsTable');	
	itemTable.empty();
	itemTable.append('<tbody></tbody>');
	itemTable.append('<tr><th>ID</th><th>Title</th><th>Title</th><th>Delete</th></tr>');
}

fn.destroyItem = (id) =>{
	$.ajax({
		type: 'DELETE',
		data: {"id": id},
		url: '/api/v1/item/delete'
	}).done(
		() => {
			//$('#'+id).remove();
			fn.clearTable();
			fn.getAllItems();
		}
	).fail(
		(err) => {

	    }
	)
}

fn.addItem = () => {
	let title = $('#title').val();
	let description = $('#description').val();
	$.ajax({
        type: 'POST',
        data: {"title": title, "description": description},
	    url: '/api/v1/item/new'
	}).done(
		() => {
			fn.clearTable();
			fn.getAllItems();
		}
	).fail(
		(err) => {

	    }
	)
}

window.fn = fn;
window.onload = fn.getAllItems;

}())