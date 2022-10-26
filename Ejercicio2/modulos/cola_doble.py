# Importo la LDE para inicializar la Cola Doble
from Ejercicio1.modulos.LDE import ListaDobleEnlazada

class ColaDoble():
    def  __init__(self):
        self.items = ListaDobleEnlazada()
        
    def tamanio(self):
        '''
        Método para conocer el tamaño de la Cola Doble.

        Returns
        -------
        int
            Retorna tamaño de la Cola Doble.

        '''
        return self.items._tamanio
    
    def __str__(self):
        '''
        Muestra todos los Nodos de la Cola Doble.

        Returns
        -------
        string
            Retorna una lista de los Nodos dentro 
            de la Cola Doble.

        '''
        lista = [str(nodo) for nodo in self]
        return str(lista)
    
    def __iter__(self):
        '''
        Método para iterar la Cola Doble.
        '''
        return iter(self.items)
    
    def esta_vacia(self):
        '''
        Comprueba si el tamaño de la Cola Doble
        es igual a 0.
        
        Returns
        -------
        boolean
            Devuelve True si la Cola Doble está vacía.
        
        '''
        return self.items.esta_vacia()
    
    
    def agregarFrente(self, item):
        '''
        Agrega un nuevo ítem al frente de la Cola Doble.
        
        Parameters
        ----------
        item : any type
            Dato que se va a almacenar en un nuevo Nodo.
       
        Returns
        -------
        None.
        
        ''' 
        return self.items.anexar(item)
    
    
    def agregarFinal(self, item):
        '''
        Agrega un nuevo ítem al final de la Cola Doble.
       
        Parameters
        ----------
        items : any type
            Dato que se va a almacenar en un nuevo Nodo.
        
        Returns
        -------
        None.
        
        ''' 
        return self.items.agregar(item)
    
    
    def removerFrente(self):
        ''' 
         Elimina el ítem del frente de la Cola Doble 
         y lo devuelve.
        
         Returns
         -------
         temp : reference
             Retorna el ítem extraido de la Cola Doble.
             
        '''
        return self.items.extraer(self.items.tamanio-1)
    
    
    def removerFinal(self):
       ''' 
        Elimina el ítem del final de la Cola Doble 
        y lo devuelve.
       
        Returns
        -------
        temp : reference
            Retorna el ítem extraido de la Cola Doble.
            
       '''
       return self.items.extraer(0)    
        
    


if __name__=='__main__':
    
    pruebaColaDoble= ColaDoble()
    
    pruebaColaDoble.agregarFinal(25)
    pruebaColaDoble.agregarFinal(6)
    pruebaColaDoble.agregarFrente(8)
    
    print(pruebaColaDoble)
    print(pruebaColaDoble.removerFinal())
    
    print(pruebaColaDoble)
    print(pruebaColaDoble.removerFrente())
    
    print(pruebaColaDoble)
    
