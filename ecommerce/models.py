from django.db import models

# Create your models here.

class Customer(models.Model):
    idCustomer = models.IntegerField()
    nombre = models.CharField(max_length=40)
    apellidoPaterno = models.CharField(max_length=20)
    apellidoMaterno = models.CharField(max_length=20)
    emial = models.EmailField()
    
class DireccionesEnvio(models.Model):
    idDireccionDeEnvio = models.IntegerField()
    idCustomer = models.IntegerField()
    calle = models.CharField(max_length=40)
    numeroInt = models.CharField(max_length=20)
    numeroExt = models.CharField(max_length=20)
    localidad = models.CharField(max_length=20)
    municipio = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    pais = models.CharField(max_length=20)
    codigoPostal = models.CharField(max_length=20)
    referencia = models.CharField(max_length=20)

class PaymentAgents(models.Model):
    idPaymentAgents = models.IntegerField()
    razonSocial = models.CharField(max_length=40)

class DeliveryAgents(models.Model):
    idDeliveryAgents = models.IntegerField()
    razonSocial = models.CharField(max_length=40)

class CategoriasProductos(models.Model):
    idCategorias = models.IntegerField()
    categoria = models.CharField(max_length=40)

class MetodosPago(models.Model):
    idCategorias = models.IntegerField()
    metodo = models.CharField(max_length=40)

class Tarjetas(models.Model):
    idTarjeta = models.IntegerField()
    idCustomer = models.IntegerField()
    tarjeta = models.CharField(max_length=16)

class Producto(models.Model):
    idProducto = models.IntegerField()
    idCategoriaProducto = models.IntegerField()
    producto = models.CharField(max_length=40)
    precioUnitario = models.IntegerField()
    unidadDeVenta = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    precio = models.IntegerField()
    existencia = models.IntegerField()
    descripcion = models.CharField(max_length=40)

class ListaDeCompra(models.Model):
    idListaDeCompra = models.IntegerField()
    idProducto = models.IntegerField()
    cantidad = models.IntegerField()

class Carrito(models.Model):
    idCarrito = models.IntegerField()
    idListaDeCompra = models.IntegerField()
    idCustomer = models.IntegerField()
    subtotal = models.IntegerField()
    total = models.IntegerField()

class Compra(models.Model):
    idCompra = models.IntegerField()
    idListaDeCompra = models.IntegerField()
    fecha = models.DateField()
    idCustomer = models.IntegerField()
    subtotal = models.IntegerField()
    idmetodoDePago = models.IntegerField()
    idDireccionDeEnvio = models.IntegerField()
    idPaymentAgents = models.IntegerField()
    idDeliveryAgents = models.IntegerField()

    idCarrito = models.IntegerField()
