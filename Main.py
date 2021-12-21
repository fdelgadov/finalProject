import tkinter as tk
from tkinter import ttk
import shortRoutes as sr

def showDijkstra():
  global txtOut
  global cmbVertexN
  global cmbVertex0
  graph = sr.graph
  goal = cmbVertexN.current()
  start = cmbVertex0.current()
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
btnDijkstra = tk.Button(root, text="Aceptar", command=showDijkstra)
btnDijkstra.grid(column=4, row=1)

txtOut = tk.Text(root, height=25, width=125)
txtOut.insert(tk.END, sr.display(sr.graph))
txtOut.grid(column=0, row=2, columnspan=5)

root.mainloop()