(function () {
const btnEliminacion = document.querySelectorAll('.btn-eliminacion');

btnEliminacion.forEach(btn => {
    btn.addEventListener('click', (e) => {
        const confirmacion = confirm('¿Estás seguro de eliminar el producto?');
        if(!confirmacion){
            e.preventDefault();
        }
    });
});
})();
