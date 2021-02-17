from bs4 import BeautifulSoup
import requests
from wiki_parser import articleParsing



def main():
    print('Hey, I\'m a simple wiki parser!')
    print('I\'ll give you some title of an artircle, and you must anwswer would u like to read it or not!')
        
    while 1:
        url = '''https://ru.wikipedia.org/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%A1%D0%BB%D1%83%D1%87%D0%B0%D0%B9%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'''
        response = requests.get(url) 
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('h1', {'id': 'firstHeading'}).text
        
        print()
        print('-' * 50)
        print(f'Would you like to read about {title} ?')
        print('Your anwswer [Y (yes) / N (no) / Q (quit)]: ')
        print('-' * 50)
        
        while 1:
            answer = input(': ').lower()

            if answer == 'q':
                return '\nSee you soon... Have a good day!'

            elif answer == 'n':
                print('I\'m choosing the next article...')
                break

            elif answer == 'y':
                print()
                print(f'\n{articleParsing(soup)}') 
                break

            else:
                print('Choose the correct answer!\n')


    
print(main())
