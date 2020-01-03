import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]
z = [200, 25, 400, 330, 100]

titulo = "Scatterplot: Gráfico de Dispersão"
eixox = "Eixo X"
eixoy = "Eixo Y"

#Legendas
plt.title (titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.scatter(x, y, label = "Pontos", color='k', marker="o", s=z)
plt.plot(x, y, color='#000000', linestyle = "--")
plt.legend()
plt.show()
#plt.savefig("figura1.png", dpi=300) #Comando para salvar figura - 300dpi é para garantir uma qualidade maior