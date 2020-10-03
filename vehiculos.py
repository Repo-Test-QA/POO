class Vehiculo():
    # Vamos a crear el constructor
    def __init__(self,color,marca,velocidad_maxima):
        # Construime un objeto de la clase Automovil, que
        # tenga tales propiedades: color, marca, etc.
        # Self, propiedades propias o dentro de mi clase
        # su scope es dentro de la clase
        # Ayuda a construir un objeto de la clase Automovil
        # Propiedades  = Variables ó valores que vienen de afuera
        # self.color = color
        self.color = color 
        self.marca = marca
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0                   # Es una propiedad cuyo valor es cero,
                                                    # porque no quiero que me la pase el usuario a priori.
                                                    # yo no quiero pasar el valor por fuera, mediante un parámetro,
                                                    # sino que tengan un valor por defecto.
        self.encendido = False 


    def encender_auto(self):
        self.encendido = True
        print("Auto encendido")

    def apagar_auto(self):
        self.encendido = False 
        print("Auto apagado")
        
    def mostrar_velocimetro(self):
        print("La velocidad actual es de " + str(self.velocidad_actual) + " de " + str(self.velocidad_maxima))

        # Considerar, cuando la función esta dentro de una
        # clase se llama Método, cuando la función esta
        # fuera de la clase se llama función

    def acelerar(self,velocidad):
        if (self.encendido == True):
            if self.velocidad_actual + velocidad > self.velocidad_maxima:
                self.velocidad_actual = self.velocidad_maxima
            else:
                self.velocidad_actual = self.velocidad_actual + velocidad
        else:
            print("Para acelerar hay que encender el auto")        
        # Self, es un método de la misma clase, mostrar mi velocimetro, de mi clase.
        self.mostrar_velocimetro()

    def frenar(self,velocidad):
        if self.velocidad_actual - velocidad < 0:
            self.velocidad_actual = 0
        else:
            self.velocidad_actual = self.velocidad_actual - velocidad
            # Self, es un método de la misma clase, mostrar mi velocimetro, de mi clase.
            self.mostrar_velocimetro()




class Camion(Vehiculo):
    # El parámetro => carga_maxima, es de la clase Hija Camion.
    # Los parámetros => color,marca, velocidad_maxima; son de la clase Padre Vehiculo. 
    def __init__(self,carga_maxima,color,marca,velocidad_maxima): 
        # Estas propiedades pueden ser llamadas desde cualquier lado
        # de la clase, porque son propiedades de mi clase.
        self.carga_maxima = carga_maxima                               
        self.carga_actual = 0    
        # Inicializo la clase Padre Vehiculo y le paso las propiedades que va heredar la clase Hija Camion.
        Vehiculo.__init__(self,color,marca,velocidad_maxima)
       
    def cargar(self,cantidad):
        self.carga_actual = self.carga_actual + cantidad 

    
    # Polimorfismo, yo quiero para el Camión que el Velocímetro (método de la clase Padre Vehiculo => mostrar_velocimetro)
    # muestre algo adicional, para este caso la Carga actual (carga_actual). Entonces sobreescribimos el método de
    # la clase Padre. Por tanto, tenemos un comportamiento diferente del Método de la clase Padre => mostrar_velocimetro
    # en la clase Padre Vehiculo, se comportara de una manera y en la clase Hija Camion, se comportara de otra.
    def mostrar_velocimetro(self):
        print("La velocidad actual es de " + str(self.velocidad_actual) + " de " + str(self.velocidad_maxima) + " y la carga es " + str(self.carga_actual))


class Automovil(Vehiculo):
    # El parámetro => puertas, es de la clase Hija Automovil.
    # Los parámetros => color,marca, velocidad_maxima; son de la clase Padre Vehiculo. 
    def __init__(self,puertas,color,marca,velocidad_maxima):        
        self.puertas = puertas
        # Inicializo la clase Padre Vehiculo y le paso las propiedades que va heredar la clase Hija Automovil.
        Vehiculo.__init__(self,color,marca,velocidad_maxima)   

    def abrir_puertas(self,nro_puertas):
        print("Se abren las puertas")


    # Herencia Multiple en Python, la clase Hija X puede Heredar, propiedades, atributos de multiples Clases Padres
    # esto lo vamos a aplicar mas adelante.
    # Considerar, en Java es diferente, se maneja mediante las interfaces.


    
           

mi_auto = Automovil(4,'Verde','Peugeot',180)
# La clase Hija Automovil no tiene el método encender_auto y todos los demás métodos que tiene la clase Padre Vehiculo.
# Yo puedo llamar a los métodos de la Clase Padre Vehiculo, como si fueran propios.
mi_auto.encender_auto()
mi_auto.acelerar(50)


#print(mi_auto.color)
#print(mi_auto.marca)

#mi_auto.encender_auto()
#mi_auto.acelerar(20)
#mi_auto.acelerar(170)
#mi_auto.frenar(5050)
#mi_auto.apagar_auto()

mi_camion = Camion(2000,'Azúl','Scania',120)
mi_camion.encender_auto()
mi_camion.acelerar(20)
#mi_camion.carga_actual = 500
#print(mi_camion.marca)
#print(mi_camion.color)
#print(mi_camion.carga_actual)