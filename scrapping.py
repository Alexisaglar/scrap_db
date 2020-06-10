import requests
import json
import pandas

token = "45d25785-210b-4e93-b772-d1c29dd7db8c"

def scrap():
    r = requests.get("https://www.inegi.org.mx/app/api/denue/v1/consulta/BuscarEntidad/inmobiliaria/14/1/1000/" + token)
    data = r.json()
    df = pandas.DataFrame(data).to_excel("output.xlsx")

def main():
    #user = sys.argv[1]
    scrap()



if __name__ == "__main__":
    main()
