document.getElementById("header").innerHTML =  `<nav class="navbar navbar-expand-sm navbar-ligth bg-light">
<div class="container">
  <a class="navbar-brand" href="index.html">MuscleClub</a>
  <button class="navbar-toggler d-lg-none" type="button" data-bs-toggle="collapse" data-bs-target="#collapsibleNavId" aria-controls="collapsibleNavId"
      aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="collapsibleNavId">
      <ul class="navbar-nav me-auto mt-2 mt-lg-0">
          
          <li class="nav-item">
              <a class="nav-link" href="#">Registrarse</a>
          </li>
          <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="dropdownId" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">CRUD</a>
              <div class="dropdown-menu" aria-labelledby="dropdownId">
                  <a id="adminLink" class="dropdown-item" href="#">Admin</a>
                  <a class="dropdown-item" href="#">Ver Carrito</a>
              </div>
          </li>
      </ul>
    <form class="d-flex my-2 my-lg-0">
        <input id="searchInput" class="form-control me-sm-2" type="text" placeholder="Search">
        <button class="btn btn-outline-success my-2 my-sm-0" type="button" onclick="searchPage()">Search</button>
    </form>


  </div>
  <!-- Agrega este script en el head o antes de cerrar el body -->


</div>

</nav>`

//Validacion Usuario Administrador
function validateAdmin() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    if (username === "admin" && password === "admin") {
    // Credenciales correctas, redirigir a productos.html o realizar alguna acción
        window.location.href = "productos.html";
    } else {
            alert("Credenciales incorrectas. Por favor, inténtelo de nuevo.");
    }

    // Cierra el modal después de validar
    $('#adminModal').modal('hide');
}

// Mostrar el formulario emergente al hacer clic en el enlace "Admin"
document.getElementById('adminLink').addEventListener('click', function () {
    $('#adminModal').modal('show');
});

//Funcion para busqueda en barra de Navegacion
function searchPage() {
    var searchQuery = document.getElementById("searchInput").value.toLowerCase();
    var pageContent = document.body.innerHTML.toLowerCase();

    if (pageContent.includes(searchQuery)) {
        var highlightedContent = pageContent.replace(new RegExp(searchQuery, 'gi'), match => `<mark>${match}</mark>`);
        document.body.innerHTML = highlightedContent;
    } else {
        alert("Palabra no encontrada en la página.");
    }
}
