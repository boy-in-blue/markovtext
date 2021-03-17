import requests

def download(url, output: str = 'text'):
    r = requests.get(url)
    if r.status_code == 200:
        with open(output, 'w') as file:
            file.write(r.text)
        print(f'{r.text[:100]}\n...\n{r.text[-100:]}\nwritten to file {output}')




if __name__ == '__main__':
    download('http://www.gutenberg.org/files/1342/1342-0.txt', 'pride') 
