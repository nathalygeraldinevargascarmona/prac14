import sqlite3
print("Hecho por Hernandez Palafox Jeimi Alondra  y Vargas Carmona Nathaly Geraldine 3b ")
CONTRASENA = "12345"
# base de datos y tabla
conexion = sqlite3.connect("productos.db")
cursor = conexion.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Productos (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nombre TEXT NOT NULL,
    Marca TEXT NOT NULL,
    Categoria TEXT NOT NULL,
    Precio REAL NOT NULL,
    Stock INTEGER NOT NULL DEFAULT 0,
    Proveedor TEXT NOT NULL,
    Fecha_Ingreso TEXT NOT NULL,
    Garantia INTEGER DEFAULT 0,
    Estado TEXT DEFAULT 'Activo',
    Descuento REAL DEFAULT 0
)
""")
conexion.commit()
print("Base de datos y tabla creada con éxito.\n")
# registrar productos
def registrar_productos():
    print("\n--- Registro de productos (máximo 10) ---")
    productos = []
    for i in range(10):
        print(f"\nProducto {i + 1}:")
        nombre = input("Nombre del producto: ").strip()
        marca = input("Marca: ").strip()
        categoria = input("Categoría: ").strip()
        precio = float(input("Precio: "))
        stock = int(input("Cantidad en stock: "))
        proveedor = input("Proveedor: ").strip()
        fecha_ingreso = input("Fecha de ingreso (YYYY-MM-DD): ").strip()
        garantia = int(input("Garantía en meses: "))
        estado = input("Estado (Activo/Inactivo): ").strip()
        descuento = float(input("Descuento (%): "))
        productos.append((nombre, marca, categoria, precio, stock, proveedor, fecha_ingreso, garantia, estado, descuento))
        # agregar mas  productos
        continuar = input("\n¿Desea agregar otro producto? (s/n): ").strip().lower()
        if continuar != 's':
            break
    # Insertar los productos deseados
    cursor.executemany("""
    INSERT INTO Productos (Nombre, Marca, Categoria, Precio, Stock, Proveedor, Fecha_Ingreso, Garantia, Estado, Descuento) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, productos)
    conexion.commit()
    print(f"\n{len(productos)} producto(s) registrado(s) correctamente.")
#consultar productos
def consultar_productos():
    print("\n--- Lista de productos ingresados ---")
    cursor.execute("SELECT * FROM Productos")
    productos = cursor.fetchall()
    if productos:
        print("\nID | Nombre     | Marca      | Categoría   | Precio | Stock | Proveedor  | Fecha Ingreso | Garantía | Estado | Descuento")
        print("-" * 110)
        for producto in productos:
            print(f"{producto[0]:<3} | {producto[1]:<10} | {producto[2]:<10} | {producto[3]:<10} | {producto[4]:<6} | {producto[5]:<5} | {producto[6]:<10} | {producto[7]:<12} | {producto[8]:<8} | {producto[9]:<6} | {producto[10]:<8}")
    else:
        print("\nNo hay productos registrados.")
# eliminar todos los productos
def eliminar_productos():
    confirmacion = input("\n¿Está seguro de que desea eliminar todos los productos? (s/n): ").strip().lower()
    if confirmacion == 's':
        cursor.execute("DELETE FROM Productos")
        conexion.commit()
        print("\nTodos los productos han sido eliminados.")
    else:
        print("\nOperación cancelada.")
# acceso con  contraseña
def iniciar_sesion():
    intentos = 3
    while intentos > 0:
        contrasena = input("Introduce la contraseña para acceder: ").strip()
        if contrasena == CONTRASENA:
            print("\nAcceso concedido.\n")
            return True
        else:
            intentos -= 1
            print(f"Contraseña incorrecta. Intentos restantes: {intentos}")
    print("\nAcceso denegado.")
    return False
#menu
def menu():
    while True:
        print("\n--- Menú principal ---")
        print("1. Registrar productos")
        print("2. Consultar productos")
        print("3. Eliminar todos los productos")
        print("4. Salir")

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == '1':
            registrar_productos()
        elif opcion == '2':
            consultar_productos()
        elif opcion == '3':
            eliminar_productos()
        elif opcion == '4':
            print("\nSaliendo del programa.")
            break
        else:
            print("\nOpción no válida. Intente nuevamente.")
#  Ejecutar el programa
if iniciar_sesion():
    menu()
conexion.close()
