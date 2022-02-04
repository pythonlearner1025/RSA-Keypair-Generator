from Crypto.PublicKey import RSA
import os
import json

def generate_privateKey():
    keyPair = RSA.generate(2048, randfunc=None, e=65539)
    print(keyPair)
    return keyPair 


def write_to_json(pem_file, json_file):
    with open(pem_file, 'r') as f:
        lines = f.readlines()
        no_header = lines[1:-1]
        result = ""
        for seg in no_header:
            result += seg.strip()

        data = {'key': result}
        with open(json_file, 'w') as j:
            json.dump(data, j) 
    

if __name__ == "__main__":
    BASE_DIR = os.getcwd()
    
    if os.path.exists(os.path.join(BASE_DIR, 'output')):
        BASE_DIR = os.path.join(BASE_DIR, 'output')
    else:
        print('making new dir output')
        BASE_DIR = os.path.join(BASE_DIR, 'output')
        os.mkdir(BASE_DIR)
    
    priv_dir = os.path.join(BASE_DIR,'private.pem')
    pub_dir = os.path.join(BASE_DIR,'public.pem')

    keyObj = generate_privateKey()
    privateKey = keyObj.export_key()
    f = open(priv_dir, 'wb')
    f.write(privateKey)
    f.close()

    pubKey = keyObj.publickey().export_key()
    f = open(pub_dir, 'wb')
    f.write(pubKey)
    f.close()

    priv_json_dir = os.path.join(BASE_DIR,'private.json')
    pub_json_dir = os.path.join(BASE_DIR,'pub.json')

    write_to_json(priv_dir, priv_json_dir)
    write_to_json(pub_dir, pub_json_dir)







