import re
import random

class Markov:
    def __init__(self, dataset: list):
        self.dataset = dataset
        self.model = {}
        self.pattern = r'CHAPTER\s[A-Z]{1,2}'

    def read_tokens(self):
        for i in range(0, len(self.dataset), 100):
            print(self.dataset[i:i+100], flush=True)
            if input() != '':
                break

    def tokenize_chapters(self):
        r = re.split(self.pattern, self.dataset, maxsplit=99)
        for i in r:
            print(i)
            input()

    def build_model(self):
        for i in range(len(self.dataset) - 1):
            if self.dataset[i] not in self.model:
                self.model[self.dataset[i]] = [self.dataset[i+1]]
            else:
                self.model[self.dataset[i]].append(self.dataset[i+1])

        print('Model Built')
#       for i in self.model.items():
#           yield i

    def generate_text(self, initial: str, length: int):
        generated_string = initial 
        for i in range(length - 1):
            initial = random.choice(self.model[initial])
            generated_string += ' ' + initial

        generated_string += '.'
        print(generated_string)
    

if __name__ == '__main__':
    with open('pride_cleaned', 'r') as file:
        data = file.read()

    tokenize = data.split(' ')

    m = Markov(tokenize)

    m.build_model()

    m.generate_text("The", 20)
    
