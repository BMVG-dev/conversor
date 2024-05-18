import xmltodict
import os
import json


def get_info(file_name):
    print(f'got information {file_name}')
    with open(f'nfs/{file_name}', 'rb') as xml_file:
        file_dict = xmltodict.parse(xml_file)
        # print(file_dict)

        try:
            if 'NFe' in file_dict:
                infos_nf = file_dict['NFe']['infNFe']
            else:
                infos_nf = file_dict['nfeProc']['NFe']['infNFe']
            note_number = infos_nf['@Id']
            issuing_company = infos_nf['emit']['xNome']
            customer_name = infos_nf['dest']['xNome']
            address = infos_nf['dest']['enderDest']
            if 'vol' in infos_nf['transp']:
                gross_weight = infos_nf['transp']['vol']['pesoB']
            else:
                gross_weight = 'zero weight'

            print(note_number, issuing_company, customer_name, address, gross_weight, sep='\n')
        except Exception as e:
            print(e)
            print(json.dumps(file_dict, indent=4))


files_list = os.listdir('nfs')

for file in files_list:
    get_info(file)
    # break
