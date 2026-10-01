productos = []
opciones_totales = 5
RESET = "\033[0m"
NEGRO = "\033[30m"
ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
MAGENTA = "\033[95m"
CIAN = "\033[96m"
BLANCO = "\033[97m"
SUBRAYADO = "\033[4m"

while True:
    menu_texto = (
        f"\n-------------------------------------------------"
        f"\n|{MAGENTA}\t📋 Sistema de Gestión de Productos{RESET} {MAGENTA}{RESET}\t|"
        f"\n-------------------------------------------------\n\n"
        f"{AMARILLO}➕\t(1) Agregar producto{RESET}\n"
        f"{VERDE}📊\t(2) Mostrar productos{RESET}\n"
        f"{CIAN}🔍\t(3) Buscar producto{RESET}\n"
        f"{ROJO}❌\t(4) Eliminar producto{RESET}\n"
        f"{AZUL}🚪\t(5) Salir{RESET}\n"
        f"\n-------------------------------------------------\n"
        f"{BLANCO}{SUBRAYADO}Ingrese número de opción deseada (1-5): {RESET}"
        )
    opcion_menu_str = input(menu_texto).strip().title()
    if opcion_menu_str.isdigit() and opcion_menu_str != "": 
        opcion_valida = int(opcion_menu_str)
        if 1 <= opcion_valida <= opciones_totales:
            if opcion_valida == 1:
                while True: 
                    print(f"Usted esta en la sección: {AMARILLO}(1)\n➕{SUBRAYADO} Agregar producto{RESET}")
                    while True:
                        productos_nombres = input(f"{AMARILLO}🏷️\tIngrese nombre del producto: {RESET}").strip().capitalize()
                        if productos_nombres.isalpha() and productos_nombres != "": 
                            break
                        else:
                            print(f"{ROJO}⚠️\tNombre no válido, no se permiten números ni campos vacíos.Ingrese nuevamente nombre del producto.{RESET}")
                            continue
                    while True:
                        productos_categorias = input(f"{CIAN}📁\tIngrese categoría del producto: {RESET}").strip().capitalize()
                        if productos_categorias.isalpha() and productos_categorias != "":  
                            break
                        else:
                            print(f"{ROJO}⚠️\tCategoría no válida, no se permiten números ni campos vacíos.Ingrese nuevamente categoría del producto.{RESET}")
                            continue                                    
                    while True:
                        productos_precios_str = input(f"{VERDE}💲\tIngrese precio del producto{ROJO}(Sólo números enteros){VERDE}: {RESET}").strip().capitalize() 
                        if productos_precios_str.isdigit() and productos_precios_str != "": 
                            precio = int(productos_precios_str) 
                            break
                        else:
                            print(f"{ROJO}⚠️\tPrecio no válido, evite usar campos vacíos, letras y números decimales.Ingrese nuevamente el precio del producto.{RESET}")
                            continue
                    productos_sublistas = [productos_nombres, productos_categorias, precio] 
                    productos.append(productos_sublistas)
                    print(f"{VERDE}{SUBRAYADO}\n¡Producto agregado con éxito!🚮{RESET}")
                    seguir_agregando = False   #-Decidir si quiere seguir agregando
                    while True:
                        options = (
                            f"\n{AMARILLO}¿Desea seguir agregando productos?🛒"
                            f"\n{MAGENTA}Pulse 1 para seguir agregando productos"
                            f"\n{BLANCO}Pulse 2 para volver al menú principal: {RESET}"
                        )
                        opt_str = input(options).strip()
                        if opt_str.isdigit() and opt_str != "":
                            opt = int(opt_str)
                            if opt == 1:
                                break 
                            elif opt == 2:
                                print(f"{ROJO} ⚠️\tSaliendo de la sección {AMARILLO}(1)\t➕{SUBRAYADO} Agregar producto{RESET}")
                                print("="*80)
                                seguir_agregando = True
                                break 
                            else:
                                print(f"{ROJO}{SUBRAYADO}⚠️\tOpción inválida. Ingrese (1) ó (2) para continuar operando.{RESET}")
                                continue
                        else:
                            print(f"{ROJO}{SUBRAYADO}⚠️\tOpción inválida. Ingrese (1) ó (2) para continuar operando.NO SE PERMITEN LETRAS NI CAMPOS VACÍOS{RESET}")
                            continue
                    if seguir_agregando:
                        break
            elif opcion_valida == 2:
                print(f"Usted esta en la sección: {VERDE}(2)\n📊{SUBRAYADO} Mostrar productos{RESET}")
                if not productos:
                    print(f"{ROJO} ⚠️\tNo hay elementos ingresados en la lista.{RESET}")
                else:
                    print("="*100)
                    print(f"\n{MAGENTA}\t\t\t-------- LISTA DE PRODUCTOS --------{RESET}")
                    for posicion in range(len(productos)):
                        print("="*100)
                        print(f"{BLANCO}\n| Producto N° {posicion + 1} {ROJO}(Para eliminar por índice ingrese este número en la opción 4 del menú principal)\n{AMARILLO}| Nombre: {productos[posicion][0]}\n{CIAN}| Categoría: {productos[posicion][1]}\n{VERDE}| Precio: $ {productos[posicion][2]}{RESET}")       
                        print("="*100)                 
            elif opcion_valida == 3:
                print(f"Usted esta en la sección: {CIAN}(3)\n🔍{SUBRAYADO} Buscar producto{RESET}")
                if not productos: 
                    print(f"{ROJO} ⚠️\tNo hay productos en la lista para realizar la búsqueda.{RESET}")
                else:
                    producto_buscado = input(f"{CIAN}\n👀\tIngrese nombre exacto del producto a buscar: {RESET}").strip().title()
                    if producto_buscado.isalpha() and producto_buscado != "": 
                        encontrado = False 
                        for p in range(len(productos)):
                                prod = productos[p][0]
                                num_prod = p + 1
                                if prod == producto_buscado:
                                    print("="*80)
                                    print(f"{VERDE}\t\t\t\t¡Producto hallado!🎯{MAGENTA}\n\t\tMostrando información completa de la búsqueda...{RESET}")
                                    print("="*80)
                                    print(f"{BLANCO}\n| Producto N° {num_prod} {ROJO}\n{AMARILLO}| Nombre: {productos[p][0]}\n{CIAN}| Categoría: {productos[p][1]}\n{VERDE}| Precio: $ {productos[p][2]}{RESET}\n")
                                    print("="*80)
                                    encontrado = True 
                                    break 
                        if not encontrado: 
                            print(f"{ROJO}⚠️\tProducto no encontrado...\n⚠️\tFin de la búsqueda.{RESET}")
                            print("="*80)
                    else:
                        print(f"{ROJO}⚠️\tNombre no válido. Solo se permiten letras.Evite números y campos vacíos.{RESET}")
            elif opcion_valida == 4:
                print(f"Usted esta en la sección: {ROJO}(4)\n❌ Eliminar producto{RESET}")
                if not productos: 
                    print(f"{ROJO}⚠️\tNo hay productos en la lista para eliminar.{RESET}")
                else:
                    indice_prod_eliminar = input(f"{ROJO}🗑️\tIngrese {SUBRAYADO}número de índice del producto{RESET}{ROJO} que desea eliminar de la lista: {RESET}").strip()
                    if indice_prod_eliminar.isdigit() and indice_prod_eliminar != "": 
                        indice_usuario = int(indice_prod_eliminar) 
                        indice_real = indice_usuario - 1 
                        if 0 <= indice_real < len(productos):
                            producto_eliminado = productos.pop(indice_real)
                            print(f"{VERDE}\t✅  ¡Se hallaron coincidencias!")
                            print(f"{AMARILLO}| Producto eliminado:{BLANCO} {producto_eliminado[0]}{CIAN}\n| Categoría:{BLANCO} {producto_eliminado[1]}{VERDE}\n| Precio:{BLANCO} ${producto_eliminado[2]}{RESET}")
                            print(f"\t✅  {SUBRAYADO}¡Operación realizada con éxito!{RESET}")
                        else:
                            print(f"{ROJO}⚠️\tEl índice ingresado está fuera del rango.{RESET}")
                    else:
                        print(f"{ROJO}⚠️\tElemento no encontrado, vuelva a escribir el índice del producto. EVITE CAMPOS VACÍOS Y LETRAS.{SUBRAYADO}SOLO NÚMEROS POSITIVOS{RESET}")
                    
            elif opcion_valida == 5:
                print(f"{AZUL}✨ ¡Gracias por utilizar nuestro Sistema de Gestión de Productos!✨\n\t\t¡Te esperamos nuevamente!😀👋{RESET}")
                break    
        else:
            print(f"{ROJO} ⚠️\tOpción inválida.Ingrese nuevamente opción (1 a 5).{RESET}")
            continue
    else:
            print(f"{ROJO} ⚠️\tOpción inválida.Ingrese nuevamente opción (1 a 5). No se permiten letras, ni campos vacíos.{RESET}")
            continue