const div = document.getElementById("divProducto");

class Productos {
        constructor(vars,producto,precio,imagen){
                this.vars = vars;
                this.producto = producto;
                this.precio = precio;
                this.imagen = imagen;
        }

        productoMostrar(){
                const productRend = [divProducto,imagenProducto,h3Producto,h4Precio,compraA]
                productRend.divProducto = document.createElement("div");
                productRend.divProducto.setAttribute("class" , "producto");
                productRend.imagenProducto = document.createElement("img");
                productRend.imagenProducto.setAttribute("class","producto");
                productRend.imagenProducto.setAttribute("src",`${this.imagen}`);
                productRend.h3Producto = document.createElement("h3");
                productRend.h3Producto.innerHTML = `${this.producto}`;
                productRend.h4Precio = document.createElement("h4");
                productRend.h4Precio.innerHTML = `Precio:${this.precio}`;
                productRend.compraA = document.createElement("button");
                productRend.compraA.setAttribute("class","btn btn-primary");
                // compraA.setAttribute();//Agregar Onclick
                productRend.compraA.innerHTML = "Comprar";
                div.appendChild(productRend.divProducto);
                productRend.forEach(element=> productRend.divProducto.appendChild(element) )
        }
}
{/* <div id="producto">
<img class="producto" src="img/productos/img-cafetera-moulinex.jpg" alt="">
<h3 id="h3h0"></h3>
<h4 id="h4h0"></h4>
<button class="btn btn-primary">Comprar</button>
</div>
<div id="producto">
<img class="producto" src="img/productos/img-tv-samsung-smart.jpg" alt="">
<h3 id="h3h1"></h3>
<h4 id="h4h1"></h4>
<a href="">Comprar</a>
</div>
<div id="producto">
<img class="producto" src="img/productos/img-macbook-pro-2019.jpg" alt="">
<h3 id="h3h2"></h3>
<h4 id="h4h2"></h4>
<a href="">Comprar</a>
</div>
<div id="producto">
<img class="producto" src="img/productos/img-samsung-galaxy-s10.jpg" alt="">
<h3 id="h3h3"></h3>
<h4 id="h4h3"></h4>
<a href="">Comprar</a>
</div> */}

const producto0 = new Productos("producto0","Cafetera Moulinex","20000","img/productos/img-cafetera-moulinex.jpg");
const producto1 = new Productos("producto1","TV Samsung Smart","30000","img/productos/img-tv-samsung-smart.jpg");
const producto2 = new Productos("producto2","Macbook Pro 2019","50000","img/productos/img-macbook-pro-2019.jpg")
const producto3 = new Productos("producto3","Samsung Galaxy S10","10000","img/productos/img-samsung-galaxy-s10.jpg");

producto0.productoMostrar();
producto1.productoMostrar();
producto2.productoMostrar();
producto3.productoMostrar();


