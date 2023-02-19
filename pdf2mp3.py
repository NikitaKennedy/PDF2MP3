from gtts import gTTS
import pdfplumber
from pathlib import Path
from art import tprint


def pdf_to_mp3(file_path='test.pdf', language='en'):
    ''' check the file  path/format and read thith licke a str and conver it to mp3'''
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        print(f'Original file: {Path(file_path).name}')
        print('Processing...')
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages] #пробегаемся по страницам в файле и извлекаем текст
        text = ''.join(pages)
        text = text.replace('\n', '')

        audio = gTTS(text=text, lang=language)
        file_name = Path(file_path).stem
        audio.save(f'{file_name}.mp3')
        return f'>>> {file_name}.mp3 saved successfull!\n ---Have a nice day!---'
    else:
        return 'file not exists, pls check the path'

def main():
    tprint('PDF 2 MP3', font='tarty2')
    file_path = input('\n Enter a file path: ')
    language = input('\n Choosw a lang, for example "en" or "ru: " ')
    print(pdf_to_mp3(file_path=file_path, language=language))

if __name__ == '__main__':
    main()
