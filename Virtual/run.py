#encoding: utf-8

import os

dependences = str(raw_input('Deseja instalar as dependencias do projeto?  \n S/N: ' ))


if dependences == "s":
	os.system("pip install tk")
	os.system("pip install time")
	os.system("pip install playsound")
	run_script = str(raw_input('Deseja rodar o programa?  ' ))
	if run_script == "s":
     	   os.system("python program/virtual.py")

	elif run_script != "s":
        	print("Ok, sem problemas \n Até a próxima")
elif dependences != "s":
	program_run2 = str(raw_input("Se já instalou as dependências, deseja rodar o programa? "))
        if program_run2 == "s":
            os.system("python program/virtual.py")
        else:
            print("Ok, sem problemas, até a próxima")

