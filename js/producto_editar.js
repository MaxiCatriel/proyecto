console.log(location.search); // Lee los argumentos pasados a este formulario
var id = location.search.substr(4); // producto_update.html?id=1
console.log(id);
const { createApp } = Vue;
createApp({
    data() {
        return {
            id: 0,
            nombre: "",
            descripcion: "",
            imagen: "",
            stock: 0,
            precio: 0,
            url: 'http://maximilianovm.pythonanywhere.com/productos/' + id,
            producto: [],
            carrito: [],

        };
    },
    methods: {
        fetchData(url) {
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    console.log(data);
                    this.id = data.id;
                    this.nombre = data.nombre;
                    this.descripcion = data.descripcion;
                    this.imagen = data.imagen;
                    this.stock = data.stock;
                    this.precio = data.precio;
                })
                .catch(err => {
                    console.error(err);
                    this.error = true;
                });
        },
        modificar() {
            let producto = {
                nombre: this.nombre,
                descripcion: this.descripcion,
                precio: this.precio,
                stock: this.stock,
                imagen: this.imagen
            };
            var options = {
                body: JSON.stringify(producto),
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                redirect: 'follow'
            };
            fetch(this.url, options)
                .then(() => {
                    alert("Registro modificado");
                    window.location.href = "./productos.html"; // Navega a productos.html
                })
                .catch(err => {
                    console.error(err);
                    alert("Error al modificar");
                });
        },
        regresar() {
            window.location.href = "./productos.html";
        },
    },

        
        created() {
            this.fetchData(this.url);
        }
    
}).mount('#app');
