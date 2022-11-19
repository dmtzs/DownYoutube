try:
    from ytLib import tk_methods
except ImportError as eImp:
    print(f"Ocurrió el siguiente error de importación: {eImp}")

if __name__== "__main__":
    try:
        met= tk_methods.TkClass()
        met.GUI()
    except Exception as ex:
        print(f"Ocurrió el ERROR: {ex}")
    except KeyboardInterrupt:
        print("Se presionó Ctrl + C")
    finally:
        print("Finalizando programa")