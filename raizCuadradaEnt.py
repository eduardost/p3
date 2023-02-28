def raizCuadradaEnt (numero):
		valor=0
		if (numero ==0):
			return numero
		i=1
		while(i*i <= numero): ## complejidad O(log N)
				i*=2 #voy multiplicando por 2
		valor= busquedaBinaria(numero,i//2,i) #cuando me pase, llamo a la busqueda.
        	## uso // pues quiero un resultado entero, sino tendria que castear.
		return valor

def busquedaBinaria(x,i,f): #le paso el numero, inicio y fin. Complejidad O(log N)
	if(i==f):
		return i
	else:
		medio=(i+f)//2
		if(x==medio*medio):
			return medio
		if(x>medio*medio):
			return busquedaBinaria(x,medio,f-1)
		else:
			return busquedaBinaria(x,i,medio-1)


#main
print (raizCuadradaEnt(2))
print (raizCuadradaEnt(9))
print (raizCuadradaEnt(18))
print (raizCuadradaEnt(199))
