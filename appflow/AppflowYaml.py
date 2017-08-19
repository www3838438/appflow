import json
import os
import yaml
import appflow.AppflowUtils as utils
import re

def get(my_file, key=None):
    pattern = re.compile("^[a-zA-Z\._-]*$")
    if not (pattern.match(my_file)):
        return 'Error: Bad Syntax'
    if not (pattern.match(key)):
        return 'Error: Bad Syntax'
    my_file = my_file.replace('.', '/', 3)
    if (my_file != 'config'):
        file_name = os.getenv("HOME") + "/.appflow/tenant/" + my_file
    else:
        file_name = os.getenv("HOME") + "/.appflow/" + my_file

    if not os.path.exists(file_name):
        return ('Error: No such File or Directory')
    if my_file.split('/').pop() == 'inventory':
        return ('Error: Invalid Request')
    if (os.path.isdir(file_name)):
        for subfile in os.listdir(file_name):
            get(my_file.replace('/', '.', 3) + '.' + subfile)
    else:
        with open(file_name, 'r') as stream:
            conf = yaml.safe_load(stream)
            if (key != None and type(key) != 'NoneType'):
                key = key.split('.')
                return (json.dumps(utils.get_from_dict(conf, key),
                                   ensure_ascii=False, indent=4))
            else:
                return (json.dumps(conf, ensure_ascii=False, indent=4))


def set(my_file, key, value):
    pattern = re.compile("^[a-zA-Z\._-]*$")
    if not (pattern.match(my_file)):
        return 'Error: Bad Syntax'
    if not (pattern.match(key)):
        return 'Error: Bad Syntax'
    my_file = my_file.replace('.', '/', 3)
    key = key.split('.')
    if (my_file != 'config'):
        file_name = os.getenv("HOME") + "/.appflow/tenant/" + my_file
    else:
        file_name = os.getenv("HOME") + "/.appflow/" + my_file
    if not os.path.exists(file_name):
        return ('Error: No such File or Directory')
    if my_file.split('/').pop() == 'inventory':
        return ('Error: Invalid Request')
    with open(file_name, 'r') as stream:
        conf = yaml.safe_load(stream)
        utils.set_in_dict(conf, key, value)
    with open(file_name, 'w') as outfile:
        yaml.dump(conf, outfile, default_flow_style=False,
                  indent=4, default_style='')
    return json.dumps(conf, ensure_ascii=False, indent=4)


def rm(my_file, key):
    pattern = re.compile("^[a-zA-Z\._-]*$")
    if not (pattern.match(my_file)):
        return 'Error: Bad Syntax'
    if not (pattern.match(key)):
        return 'Error: Bad Syntax'
    my_file = my_file.replace('.', '/', 3)
    key = key.split('.')
    if (my_file != 'config'):
        file_name = os.getenv("HOME") + "/.appflow/tenant/" + my_file
    else:
        file_name = os.getenv("HOME") + "/.appflow/" + my_file
    if not os.path.exists(file_name):
        return ('Error: No such File or Directory')
    if my_file.split('/').pop() == 'inventory':
        return ('Error: Invalid Request')
    with open(file_name, 'r') as stream:
        conf = yaml.safe_load(stream)
        utils.rm_in_dict(conf, key)
    with open(file_name, 'w') as outfile:
        yaml.dump(conf, outfile, default_flow_style=False,
                  indent=4, default_style='')
    return json.dumps(conf, ensure_ascii=False, indent=4)


def add(my_file, key, value):
    pattern = re.compile("^[a-zA-Z\._-]*$")
    if not (pattern.match(my_file)):
        return 'Error: Bad Syntax'
    if not (pattern.match(key)):
        return 'Error: Bad Syntax'
    my_file = my_file.replace('.', '/', 3)
    key = key.split('.')
    if (my_file != 'config'):
        file_name = os.getenv("HOME") + "/.appflow/tenant/" + my_file
    else:
        file_name = os.getenv("HOME") + "/.appflow/" + my_file
    if not os.path.exists(file_name):
        return ('Error: No such File or Directory')
    if my_file.split('/').pop() == 'inventory':
        return ('Error: Invalid Request')
    with open(file_name, 'r') as stream:
        conf = yaml.safe_load(stream)
    d = {}
    utils.add_keys(d, key, value)
    my_dicts = [conf, d]
    for a in my_dicts:
        for k, v in a.items():
            conf[k].update(v)
    with open(file_name, 'w') as outfile:
        yaml.dump(conf, outfile, default_flow_style=False,
                  indent=4, default_style='')
    return (json.dumps(conf, ensure_ascii=False, indent=4))