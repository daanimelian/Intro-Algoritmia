"""Una editorial determina el precio de un libro según la cantidad de páginas que
contiene. El costo básico del libro es de $5000, más $32 por página con encuadernación rústica. Si el número de páginas supera las 300 la encuadernación
debe ser en tela, lo que incrementa el costo en $1200. Además, si el número de
páginas sobrepasa las 600 se hace necesario un procedimiento especial de encuadernación que incrementa el costo en otros $3360. Desarrollar un programa
que calcule el costo de un libro dado el número de páginas.
"""
costo_basico = 5000
incremento_tela = 1200
incremento_especial = 3360
costo_pagina = 32
primer_limite = 300
segundo_limite = 600

num_paginas = int(input("Ingresar el numero de paginas del libro: "))

if num_paginas <= primer_limite:
    costo_total = costo_basico + (num_paginas * costo_pagina)
elif num_paginas <= segundo_limite:
    costo_total = costo_basico + incremento_tela + (num_paginas * costo_pagina)
else:
    costo_total = costo_basico + incremento_especial + (num_paginas * costo_pagina)

print("El costo del libro es de: $", costo_total)