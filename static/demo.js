// Autor: @jqcaper
// Configuraciones Generales
var nombre_tabla = "tabla_cat";
var nombre_boton_eliminar = ".delete";
var nombre_formulario_modal = "#frmEliminar";
var nombre_ventana_modal = "#modal{{ catalogo.id }}";
// Fin de configuraciones


    $(document).on('ready',function(){
        $(nombre_boton_eliminar).on('click',function(e){
            e.preventDefault();
            var Pid = $(this).attr('id');
            var name = $(this).data('descripcion');
            $('#modal_idProducto').val(Pid);
            $('#modal_name').text(name);
        });

        var options = {
                success:function(response)
                {
                    if(response.status=="True"){
                        alert("Eliminado!");
                        var idProd = response.idEliminar;
                        var elementos= $(nombre_tabla+' >tbody >tr').length;
                        if(elementos==1){
                                location.reload();
                        }else{
                            $('#tr'+idProd).remove();
                            $(nombre_ventana_modal).modal('hide');
                        }

                    }else{
                        alert("Hubo un error al eliminar!");
                        $(nombre_ventana_modal).modal('hide');
                    };
                }
            };

        $(nombre_formulario_modal).ajaxForm(options);
    });