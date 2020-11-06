from PIL import Image, ImageDraw #Подключим необходимые библиотеки.


image = Image.open("1.bmp") #Открываем изображение.
image=image.convert('RGB')
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования.
width = image.size[0] #Определяем ширину.
height = image.size[1] #Определяем высоту.
pix = image.load() #Выгружаем значения пикселей.

#маски углов в прямоугольнике
rec1=[[255,255,255],[255,0,0],[255,0,255]]
rec2=[[255,255,255],[0,0,255],[255,0,255]]
rec3=[[255,0,255],[0,0,255],[255,255,255]]
rec4=[[255,0,255],[255,0,0],[255,255,255]]

#вычисление значений соседних пикселей
def findNeighbors(l,m):
	a = [[0] * 3 for i in range(3)]
	for i in range(3):
		for j in range(3):
			a[i][j]=pix[j+m-1,i+l-1][0]
	print(a)
	return a


# функция для поиска первого черного пикселя
def findBlack(): #
	for i in range(width):
		for j in range(height):
			if (pix[i,j]==(0,0,0)):
				return i,j

def findFig():
	count=0
	for i in range(width):
		for j in range(height):
			if(pix[i, j] == (0, 0, 0)):
				a=findNeighbors(i,j)
				if (findNeighbors(i,j) in (rec1,rec2,rec3,rec4)):
					count=count+1
	if (count==4):
		print("прямоугольник")



findFig()