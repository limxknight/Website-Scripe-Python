from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def find_all(soup, a, b):
	object_a = soup.find_all('p', b)
	for i in object_a:
		a.append(i.text)
	return a


if __name__ == "__main__":
	soup1 = BeautifulSoup(open("C:\Users\Minxing\Desktop\New folder\ file name1.html").read())
	full_name1 = []
	title1 = []
	company1=[]
	find_all(soup1, full_name1, "full_name")
	find_all(soup1, title1, "title")
	find_all(soup1, company1, "main_descript")
	print len(full_name1), len(title1), len(company1)
	print full_name1
	soup2 = BeautifulSoup(open("C:\Users\Minxing\Desktop\New folder\ file name2.html").read())
	full_name2 = []
	title2 = []
	company2=[]
	find_all(soup2 ,full_name2, "full_name")
	find_all(soup2 ,title2, "title")
	find_all(soup2 ,company2, "main_descript")
	print len(full_name2), len(title2), len(company2)

	# print full_name1, full_name2

	full_name1.extend(full_name2)
	title1.extend(title2)
	company1.extend(company2)
	print len(full_name1), len(title1), len(company1)

	full_name = pd.Series(full_name1)
	title = pd.Series(title1)
	company = pd.Series(company1)

	data = pd.DataFrame([full_name, title, company], index=['full_name', 'title', 'company'])
	data2 = data.transpose()

	data2.index = np.arange(1, len(data2)+1)
	data2.to_csv('filename.csv', encoding='utf-8', index=True)



