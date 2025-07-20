import csv

with open("tarefas.csv", "r") as arquivo:
  #tarefas = list(csv.reader(arquivo))
  tarefas = list(csv.DictReader(arquivo))

for tarefa in tarefas:
  print()
  for coluna, valor in tarefa.items():
    print(f"{coluna} - {valor}")
  print()