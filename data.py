import json

def load_json(filename):
    path=f'data/{filename}.json'
    with open(path,'rb') as fp:
        data=json.load(fp)
    fp.close()
    return data


def get_data(filename,key):
    LINUX_TERMS=['FILE COMMANDS','PROCESS MANAGEMENT','FILE PERMISSIONS','SSH','SEARCHING','SYS INFO','COMPRESSION','NETWORK']
    PYTHON_TERMS=['FUNCTIONS','LIST','TUPLE','DICTIONARY','SET','STRING','EXCEPTIONS','KEYWORDS']
    data=load_json(filename)
    if filename == 'linux': keyword = LINUX_TERMS[key-1]
    elif filename == 'python' : keyword = PYTHON_TERMS[key-1]
    return data[keyword]