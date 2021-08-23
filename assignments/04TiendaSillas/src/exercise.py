
def precio_antes_descuento(tipo_silla, cantidad) :
    if tipo_silla == "B" :
       # precio = 
    elif tipo_silla == "E" :
       # precio = 
    else :
       # precio = 
    return precio

def calcula_descuento(precio, tipo_cl) :
    if tipo_cl == "F" :
      #  desc = 
    else :
        if precio >= 10000 and precio < 20000 :
        #    desc = 
        elif precio >= 20000 :
        #    desc =
        else :
       #     desc = 
    return desc

def main() :
    # pido el tipo de silla (B E L)
    tipo_silla = input("Tipo silla: ")
    # pido el tipo de cliente (N F)
    tipo_cl = input("Tipo cliente: ")
    cantidad = int(input("Cantidad de sillas: "))

    subtotal = precio_antes_descuento(tipo_silla, cantidad)
    desc = calcula_descuento(subtotal, tipo_cl)
    total = subtotal - desc
    print(f"Total sin dcto.  ${subtotal:>7}")
    print(f"Descuento        ${desc:>7}")
    print(f"Total a pagar    ${total:>7}")



if __name__=='__main__':
    main()
