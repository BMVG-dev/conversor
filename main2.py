import os  # Para manusear melhor os arquivos

import pandas as pd
import xmltodict  # Faz a leitura do xml e permite que o Python a entenda


def get_info(file_name, values):

    with open(f'nfs/{file_name}', 'rb') as xml_file:    # Para que ele abra a pasta
        file_dict = xmltodict.parse(xml_file)   # “parse” que executa essa ação de tornar as informações do xml em um dicionário

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

        values.append([note_number, issuing_company, customer_name, address, gross_weight])


files_list = os.listdir('nfs')

columns = ['note_number', 'issuing_company', 'customer_name', 'address', 'gross_weight']
values = []

for file in files_list:
    get_info(file, values)

table = pd.DataFrame(columns=columns, data=values)
table.to_excel('Tax Invoice.xlsx', index=False)
