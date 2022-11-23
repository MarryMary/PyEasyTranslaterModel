import Tokenizer

def main():
    path = "sample"
    with open(path) as f:
        s = f.read()
    tokenizer = Tokenizer.Tokenizer()
    #tokenizer.token_debug()
    tokenized = tokenizer.tokenize(s)
    print(tokenized)

main()