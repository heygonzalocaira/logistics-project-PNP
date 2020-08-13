function get_areas_destino()
{
    const area_destino = $("#a_destino_index");
    var nombre;
    $.get('/api/v1.0/AreaORI/',{},function(rpta)
	{
		for(var i = 0; i < rpta.length; i++)
		{
		    if(i == 0) nombre = rpta[i].area;
			area_destino.append($('<option>', {value:rpta[i].id, text:rpta[i].area}));
		}
		$("#area_nombre_index").val(nombre);
	});


}

function get_tipos_documento()
{
    const tipo_documento = $("#t_documento_index");
    $.get('/api/v1.0/TipoDocumentos/',{},function(rpta)
	{
		for(var i = 0; i < rpta.length; i++)
		{
			tipo_documento.append($('<option>', {value:rpta[i].id, text:rpta[i].nombre_corto}));
		}
	});
}

function changes()
{
    const area_destino = $("#a_destino_index");
    area_destino.change(function()
    {
        var nombre = area_destino.children("option:selected").text();
        $("#area_nombre_index").val(nombre);
    });
}

function limpiarForm()
{
  $("#Form_add_registro")[0].reset();
}
