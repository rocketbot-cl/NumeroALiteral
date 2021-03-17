# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""
base_path = tmp_global_obj["basepath"]
cur_path = base_path + "modules" + os.sep + "NumeroALiteral" + os.sep + "libs" + os.sep
sys.path.append(cur_path)
from numero_letras import *

"""
    Obtengo el modulo que fue invocado
"""

module = GetParams("module")

if module == "numeroALetra":
    numero = GetParams("number")
    numero = int(numero)
    result = GetParams("result")
    try:
        literal = numero_a_letras(numero)
        print("el numero es:",literal)
        SetVar(result, literal)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e
