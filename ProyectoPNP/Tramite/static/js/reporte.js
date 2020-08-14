var libre = true;
$(document).ready(function()
{
    modal_js();
    get_areas_destino();
    area_change();
    nombre_change();
    unidad_change();
    export_excel();

});


function modal_js()
{
    var modal = document.getElementById('id01');

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event)
    {
        if (event.target == modal)
        {
            modal.style.display = "none";
        }
    }

    var generate = document.getElementById("btn-generate").addEventListener("click", onShow);
    var excel = document.getElementById("generar_excel").addEventListener("click", onHidden);
    var cancel = document.getElementById("btn-cancel").addEventListener("click", onHidden);
    onShow();
    onHidden();



}

function onShow()
{
    document.getElementById('id01').style.display='block';
}

function onHidden()
{
    document.getElementById('id01').style.display='none';
}

function get_areas_destino()
{
    const area_destino = $("#a_destino_index");
    var nombre;
    area_destino.append($('<option>', {value:"", text:""}));
    $.get('/api/v1.0/AreaORI/',{},function(rpta)
	{
		for(var i = 0; i < rpta.length; i++)
		{
		    // if(i == 0) nombre = rpta[i].area;
			area_destino.append($('<option>', {value:rpta[i].id, text:rpta[i].area}));
		}
	});
}


function area_change()
{
    const nombre_encargado = $("#encargado_reportes");
    const area_seleccionada = $("#a_destino_index");
    const nombre_unidad = $("#unidad_reportes");
    area_seleccionada.change(function()
    {
        const nombre = area_seleccionada.children("option:selected").text();
        if(nombre.length > 0)
        {
            if(libre)
            {
                libre = false;
                nombre_encargado.attr('disabled','disabled');
                nombre_unidad.attr('disabled','disabled');
            }

        }
        else
        {
            libre = true;
            nombre_encargado.removeAttr('disabled');
            nombre_unidad.removeAttr('disabled');
        }
    });
}

function nombre_change()
{
    const nombre_encargado = $("#encargado_reportes");
    const area_seleccionada = $("#a_destino_index");
    const nombre_unidad = $("#unidad_reportes");
    nombre_encargado.on("input",function()
    {
        nombre = nombre_encargado.val();
        if(nombre.length > 0)
        {
            if(libre)
            {
                libre = false;
                area_seleccionada.attr('disabled',true);
                nombre_unidad.attr('disabled','disabled');
            }

        }
        else
        {
            libre = true;
            area_seleccionada.attr('disabled',false);
            nombre_unidad.removeAttr('disabled');
        }
    });
}

function unidad_change()
{
    const nombre_encargado = $("#encargado_reportes");
    const area_seleccionada = $("#a_destino_index");
    const nombre_unidad = $("#unidad_reportes");
    nombre_unidad.on("input",function()
    {
        nombre = nombre_unidad.val();
        if(nombre.length > 0)
        {
            if(libre)
            {
                libre = false;
                area_seleccionada.attr('disabled',true);
                nombre_encargado.attr('disabled','disabled');
            }

        }
        else
        {
            libre = true;
            area_seleccionada.attr('disabled',false);
            nombre_encargado.removeAttr('disabled');
        }
    });
}


function export_excel()
{
    const button = $("#generar_excel")
    button.click(function()
    {
        generate_cabecera();
        llenar_tabla();

    });

}


function generate_cabecera()
{
    const nombre_encargado = $("#encargado_reportes");
    const area_seleccionada = $("#a_destino_index");
    const nombre_unidad = $("#unidad_reportes");
    var cabecera = $("#data_table thead tr");
    if(nombre_encargado.val().length > 0)
    {
        cabecera.append("<th>Numero de documento </th>");
        cabecera.append("<th>Numero de hoja </th>");
        cabecera.append("<th>Unidad de entrega </th>");
        cabecera.append("<th>Usuario que entrego </th>");
        cabecera.append("<th>Unidad de destino </th>");
        cabecera.append("<th>Fecha de documento </th>");
        cabecera.append("<th>Area de destino </th>");
    }
    else if(nombre_unidad.val().length > 0)
    {
        cabecera.append("<th>Numero de documento </th>");
        cabecera.append("<th>Numero de hoja </th>");
        cabecera.append("<th>Usuario que entrego </th>");
        cabecera.append("<th>Unidad de destino </th>");
        cabecera.append("<th>Encargado </th>");
        cabecera.append("<th>Fecha de documento </th>");
        cabecera.append("<th>Area de destino </th>");
    }
    else
    {
        cabecera.append("<th>Numero de documento </th>");
        cabecera.append("<th>Numero de hoja </th>");
        cabecera.append("<th>Unidad de entrega </th>");
        cabecera.append("<th>Usuario que entrego </th>");
        cabecera.append("<th>Unidad de destino </th>");
        cabecera.append("<th>Encargado </th>");
        cabecera.append("<th>Fecha de documento </th>");
    }
}

function llenar_tabla()
{
    var tabla_cuerpo = $("#data_table tbody");
    const nombre_encargado = $("#encargado_reportes");
    const area_seleccionada = $("#a_destino_index");
    const nombre_unidad = $("#unidad_reportes");
    const fecha = $("#fecha_reportes").val();
    var metodo;
    if(nombre_encargado.val().length > 0) metodo = 1;
    else if (nombre_unidad.val().length > 0) metodo = 2;
    else metodo = 3;
    $.ajax(
    {
        url : '/tramite/reportes/consulta',
        data :
        { id : metodo,
        date: fecha,
        encargado: nombre_encargado.val(),
        unidad: nombre_unidad.val(),
        area: area_seleccionada.val(),
        },
        type : 'GET',
        dataType : 'json',

        success : function(data_rpta)
        {
            for(var i = 0; i < data_rpta.data.length; i++)
            {
                if(metodo == 1)
                {
                    const var_1 = "<td>" + data_rpta.data[i].n_documento +"</td>";
                    const var_2 = "<td>" + data_rpta.data[i].numero_Hoja +"</td>";
                    const var_3 ="<td>" + data_rpta.data[i].unidadEntrega+"</td>";
                    const var_4 ="<td>" + data_rpta.data[i].quien_entrega +"</td>";
                    const var_5 ="<td>" + data_rpta.data[i].unidad_Destino +"</td>";
                    const var_6 ="<td>" + data_rpta.data[i].fecha_documento +"</td>";
                    const var_7 ="<td>" + data_rpta.data[i].area_destino +"</td>";
                    tabla_cuerpo.append("<tr>" + var_1 + var_2 + var_3 + var_4 + var_5 + var_6 + var_7 + "</tr>");
                }
                else if(metodo == 2)
                {
                    const var_1 = "<td>" + data_rpta.data[i].n_documento +"</td>";
                    const var_2 = "<td>" + data_rpta.data[i].numero_Hoja +"</td>";
                    const var_3 = "<td>" + data_rpta.data[i].quien_entrega +"</td>";
                    const var_4 = "<td>" + data_rpta.data[i].unidad_Destino +"</td>";
                    const var_5 = "<td>" + data_rpta.data[i].encargado +"</td>";
                    const var_6 = "<td>" + data_rpta.data[i].fecha_documento +"</td>";
                    const var_7 = "<td>" + data_rpta.data[i].area_destino +"</td>";
                    tabla_cuerpo.append("<tr>" + var_1 + var_2 + var_3 + var_4 + var_5 + var_6 + var_7 + "</tr>");
                }
                else
                {
                    const var_1 = "<td>" + data_rpta.data[i].n_documento +"</td>";
                    const var_2 = "<td>" + data_rpta.data[i].numero_Hoja +"</td>";
                    const var_3 = "<td>" + data_rpta.data[i].unidadEntrega+"</td>";
                    const var_4 = "<td>" + data_rpta.data[i].quien_entrega +"</td>";
                    const var_5 = "<td>" + data_rpta.data[i].unidad_Destino +"</td>";
                    const var_6 = "<td>" + data_rpta.data[i].encargado +"</td>";
                    const var_7 = "<td>" + data_rpta.data[i].fecha_documento +"</td>";
                    tabla_cuerpo.append("<tr>" + var_1 + var_2 + var_3 + var_4 + var_5 + var_6 + var_7 + "</tr>");

                }
            }
            $("#data_table").tableExport(
            {
                headings: true,
                footers: true,
                formats: ["xlsx", "csv", "txt"],
                fileName: "reporte_tramite",
                bootstrap: true,
                position: "buttom" ,
                ignoreRows: null,
                ignoreCols: null,
                ignoreCSS: ".tableexport-ignore"
            });
            $(".xlsx").click();

        },
        error : function(xhr, status) {
            alert('Esta consulta fallo');
        },

    });
}
/*
        n_documento
        numero_Hoja
        unidadEntrega
        quien_entrega
        unidad_Destino
        fecha_documento
        area_destino
        encargado
*/


