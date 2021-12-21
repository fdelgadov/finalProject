import tkinter as tk
from tkinter import ttk
import shortRoutes as sr
import tabulate as tb

def showRes():
  global txtOut
  global cmbVertexN
  global cmbVertex0
  global cmbAlg
  graph = sr.graph
  goal = cmbVertexN.current()
  start = cmbVertex0.current()
  alg = cmbAlg.current()

  out = ""
  if alg == 0:
    distances, routes = sr.dijkstra(graph, start)
    if distances[goal] != float('inf'):
      out = f'Distancia: {distances[goal]} km'

      rute = ""
      for i in sr.interpretRoute(routes, goal):
        if i == -1:
          i = start
        rute = f'{rute}{regions[i]} -> '

      out = f'{out}\nLa ruta es: {rute[:-4]}'
    else:
      out = f'No existe la ruta'
  else:
    distances = sr.BellmanFord(graph, start)
    out = f'Distancia: {distances[goal]} km'

  txtOut.delete(0.0, tk.END)
  txtOut.insert(0.0, out)

def showFloydWarshall():
  global txtOut
  table = sr.floydWarshall(sr.graph)
  legend = []
  j = 0
  for i in table:
    i.insert(0, regionsAbbreviated[j])
    legend.append([regions[j], regionsAbbreviated[j]])
    j += 1

  legend = tb.tabulate(legend, headers=["Capital", "Abreviatura"])
  table = tb.tabulate(table, headers=[""] + regionsAbbreviated)

  out = f'{legend}\n\n{table}'

  txtOut.delete(0.0, tk.END)
  txtOut.insert(0.0, out)

regions = [
  "Abancay",
  "Arequipa",
  "Ayacucho",
  "Cajamarca",

  "Cerro de Pasco",
  "Chachapollas",
  "Chiclayo",
  "Cusco",

  "Huancavelica",
  "Huancayo",
  "Huánuco",
  "Huaraz",

  "Ica",
  "Iquitos",
  "Lima",
  "Mollobamba",

  "Moquegua",
  "Piura",
  "Pucallpa",
  "Puerto Maldonado",
  
  "Puno",
  "Tacna",
  "Trujillo",
  "Tumbes"]

regionsAbbreviated = [
  "Aba",
  "Are",
  "Aya",
  "Caj",

  "CeP",
  "Cha",
  "Chi",
  "Cus",

  "Hca",
  "Hyo",
  "Hco",
  "Haz",

  "Ica",
  "Iqu",
  "Lim",
  "Mol",

  "Moq",
  "Piu",
  "Puc",
  "PuM",
  
  "Pun",
  "Tac",
  "Tru",
  "Tum"]

root = tk.Tk()
root.title("Rutas cortas")

tk.Label(root, text="Calcular ruta más corta").grid(column=0, row=0)
tk.Label(root, text="Desde ").grid(column=0, row=1)
cmbVertex0 = ttk.Combobox(root)
cmbVertex0["values"] = regions
cmbVertex0.set("Abancay")
cmbVertex0.grid(column=1, row=1)
tk.Label(root, text=" hasta ").grid(column=2, row=1)
cmbVertexN = ttk.Combobox(root)
cmbVertexN["values"] = regions
cmbVertexN.set("Abancay")
cmbVertexN.grid(column=3, row=1)
cmbAlg = ttk.Combobox(root)
cmbAlg["values"] = ["Dijkstra", "BellmanFord"]
cmbAlg.set("Dijkstra")
cmbAlg.grid(column=4, row=1)
tk.Button(root, text="Aceptar", command=showRes).grid(column=5, row=1)

tk.Label(root, text="Calcular todas rutas").grid(column=0, row=2)
tk.Button(root, text="Aceptar", command=showFloydWarshall).grid(column=1, row=2)

txtOut = tk.Text(root, height=175, width=175)
txtOut.insert(tk.END, sr.display(sr.graph))
txtOut.grid(column=0, row=3, columnspan=6)

root.mainloop()