from processing import process
from preprocessing import preprocess

def safe_(command, blocks, preprocessed):
    blocks = "\n".join([block.text for block in blocks])
    tags = process(preprocess(command.text, False)).split("\n") if any(command.text) else ['', '']
    return f"{tags[0]}\n{blocks}\n{tags[1]}"