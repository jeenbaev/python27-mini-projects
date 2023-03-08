# import requests
# import csv
# from bs4 import BeautifulSoup

# url = "https://enter.kg/computers/noutbuki_bishkek"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

# notebooks = soup.find_all('div', class_='row')
# data_list = []

# for note in notebooks:
#     title = note.find('div', class_='rows').find('a').text.strip()
#     img = 'https://enter.kg' + note.find('a', class_='product-image-link').find('img').get('src')
#     price = note.find('span', class_='price').text.strip()

#     data_list.append({
#         'title': title,
#         'img': img,
#         'price': price
#     })



# with open('notebooks.csv', 'w', newline='') as csv_file:
#     writer = csv.DictWriter(csv_file, fieldnames=['title', 'img', 'price'], delimiter='/')
#     writer.writeheader()
#     for data in data_list:
#         writer.writerow(data)








