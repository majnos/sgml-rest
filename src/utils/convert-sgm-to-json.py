from bs4 import BeautifulSoup
import os
import json
from os.path import join, isfile, dirname

sgmDataDirPath = join(dirname(__file__), '../../sgm-data')
jsonDataDirPath = join(dirname(__file__), '../../json-data')


def xml_node_to_json(node):
    textNode = node.find('text')

    return {
        'metadata.topics': node.get('topics'),
        'metadata.lewissplit': node.get('lewissplit'),
        'metadata.cgisplit': node.get('cgisplit'),
        'metadata.oldid': node.get('oldid'),
        'metadata.newid': node.get('newid'),

        'date': node.find('date').text,
        'unknown': node.find('unknown').text if node.find('unknown') else '',
        'fulltext.dateline': textNode.find('dateline').text if textNode.find('dateline') else '',
        'fulltext.body': textNode.find('body').text if textNode.find('body') else '',
        'fulltext.title': textNode.find('title').text if textNode.find('title') else '',

        'listitems.topics': [elem.text for elem in node.find('topics').findAll('d')],
        'listitems.people': [elem.text for elem in node.find('people').findAll('d')],
        'listitems.places': [elem.text for elem in node.find('places').findAll('d')],
        'listitems.orgs': [elem.text for elem in node.find('orgs').findAll('d')],
        'listitems.exchanges': [elem.text for elem in node.find('exchanges').findAll('d')],
        'listitems.companies': [elem.text for elem in node.find('companies').findAll('d')]
    }

files = [f for f in os.listdir(sgmDataDirPath) if isfile(join(sgmDataDirPath, f))]

for sgmName in files:
    jsonName = sgmName.replace('.sgm', '.json')
    with open(join(sgmDataDirPath, sgmName), encoding="utf8", errors='ignore') as rf:
        with open(join(jsonDataDirPath, jsonName), mode='w') as wf:
            print('working on', sgmName)
            content = BeautifulSoup(rf,'html.parser')

            jsonDocs = []
            for entry in content.findAll('reuters'):
                data = xml_node_to_json(entry)
                jsonDocs.append(data)

            json.dump(jsonDocs, wf, indent=4, sort_keys=True)
            print("Done with", sgmName)