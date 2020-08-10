 function llenar_tabla()
 {
    $("#TablaFiltradora").dataTable({
        "language":{
           "url" : "https://cdn.datatables.net/plug-ins/1.10.20/i18n/Spanish.json"
        },
        'ajax':
		{
			'url': '',

		},
		'columns':[

		    {'data':'id'},
			{'data':'area'},
			{'data':'grupo'},
			{'data':'activo'},
			{'data':'estado'},
			{'data':'tipo'},
			{'defaultContent':"<button type='button' id='Editar' class='btn btn-success' style='padding: 4px 10px;margin: 2px;' ><i class='fa fa-pencil-square-o'></i></button><button type='button' id='Eliminar' style='padding: 4px 10px;' class='btn btn-danger'><i class='fa fa-trash-o'></i></button>",'sWidth':'10%'}
		]

	});
 }
