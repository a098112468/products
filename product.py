import os

#讀取檔案
def read_file(filename):	
	products = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
					continue
			name, price = line.strip().split(',')
			products.append([name, price])
	return products

# 讓使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入產品價格: ')
		products.append([name, price])
	print(products)
	return products

#印出商品和價格
def name_price(products):
	for p in products:
		print(p[0], '的價錢是', p[1])	

#寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile('products.csv'): #檢查檔案是否存在
		print('找到檔案')
		products = read_file('products.csv')
	else:
		print('未找到檔案')
		products = []

	products = user_input(products)
	name_price(products)
	write_file('products.csv', products)

main()