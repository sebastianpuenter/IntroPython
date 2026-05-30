from datetime import date, datetime


def calcular_edad(fecha_nac: date) -> int:
	hoy = date.today()
	edad = hoy.year - fecha_nac.year
	if (hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day):
		edad -= 1
	return edad


def pedir_fecha() -> date:
	texto = input('Ingrese su fecha de nacimiento (DD/MM/AAAA): ').strip()
	try:
		dt = datetime.strptime(texto, '%d/%m/%Y')
		return dt.date()
	except ValueError:
		print('Formato inválido. Use DD/MM/AAAA.')
		return pedir_fecha()


def main():
	fecha = pedir_fecha()
	edad = calcular_edad(fecha)
	print(f'Tiene {edad} años.')


if __name__ == '__main__':
	main()

