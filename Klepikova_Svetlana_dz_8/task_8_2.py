import re


def file_parser(path_file):
    with open(path_file, 'r', encoding='utf-8') as fr:
        try:
            for str in fr.readlines():
                RE_ADDR = re.compile(r'^(\d*[a-zA-Z]*\d*\.{0,1}\:{0,1}){3,}(\d*[a-zA-Z]*\d*)') # уточнила для особенной строки 9093
                RE_DATE = re.compile(r'\d{2}/\w{3,9}/\d{4}:(\d{2}:){2}\d{2} \+0{4}')
                RE_TYPE = re.compile(r'[A-Z]{3,}')
                RE_RES = re.compile(r'[/a-zA-Z\_]+/[a-zA-Z\_]+[0-9]*')
                RE_CODE = re.compile(r'\d{3}(?= \d)')
                RE_SIZE = re.compile(r'(?<=\d{3} )\d{1,8}')
                parsed_raw = RE_ADDR.search(str).group(), RE_DATE.search(str).group(), RE_TYPE.search(str).group(), RE_RES.search(str).group(), RE_CODE.search(str).group(), RE_SIZE.search(str).group()
                print(parsed_raw)
        except AttributeError as e:
            print(f'{e} - ошибка в строке: {str}')


if __name__ == '__main__':
    file_parser('nginx_logs.txt')