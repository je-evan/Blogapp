import random
import string
import uuid

class GeneratePassword:
    def __init__(self,chars:str=None,char_length:int=8):
        if not chars:
            self.chars=string.ascii_letters+string.digits+string.punctuation
        else:
            self.chars=chars
        self.char_length=char_length

    def generate(self,seed:str=None)->dict:
        seed=str(uuid.uuid4())if seed is None else seed
        random.seed(seed)
        password=''.join(random.choice(self.chars)for i in range(self.char_length))
        return{'seed':seed,'password':password,'chars':self.chars}

    def recovery(self,seed:str)->str:
        random.seed(seed)
        password=''.join(random.choice(self.chars)for i in range(self.char_length))
        return password
