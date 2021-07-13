

with open("arq_text.txt", "r") as f:
    lines = f.readlines()
with open("arq_text.txt", "w") as f:
    for line in lines:
        if line.strip("\n") != "Testando aqui.":
            f.write(line)