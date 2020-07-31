def parteAte(string, limite,separador):
	partes = string.split(separador)
	partes = partes[0:limite]
	retorno = ''
	for p in partes:
		retorno += p + separador
	return retorno

def parte(string, parte, separador):
	partes = string.split(separador)
	return partes[parte]