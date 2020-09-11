from xml.etree import ElementTree
import os
import csv

os.chdir("/Users/stanislav.iliev/Desktop/")

tree = ElementTree.parse('app-id-list.xml')

csv_data = open('output.csv' , 'w+' , newline='' , encoding='utf-8')
csvwriter = csv.writer(csv_data)

col_names = [
    'Name', 'Category', 'Subcategory', 'Risk', 'Technology', 'Standard Ports', 'Characteristics'
]

csvwriter.writerow(col_names)
root = tree.getroot()

for(event) in root[0]:
    event_data = []

    event_id = event.get('name')
    print(event_id)
    event_data.append(event_id) 

    event_title = event.find('Category')
    if event_title != None :
        event_title = event_title.text
    event_data.append(getattr(event.find('category'), 'text', ''))

    event_description = event.find('Subcategory')
    event_data.append(getattr(event.find('subcategory'), 'text', ''))

    event_state = event.find('Risk')
    event_data.append(getattr(event.find('risk'), 'text', ''))

    event_solution = event.find('Technology')
    event_data.append(getattr(event.find('technology'), 'text', ''))


    default_tag = event.find('default')
    if default_tag:
        port = default_tag.find('port')
        if port:
            members = port.findall('member')
            events_member = []
            for member in members :
                events_member.append(member.text)

            delimiter = ' '
            event_data.append(delimiter.join(events_member))


    characteristics_arr = [
    'evasive-behavior',         'consume-big-bandwidth',
    'used-by-malware' ,         'able-to-transfer-file',
    'has-known-vulnerability',  'tunnel-other-application'
    'prone-to-misuse',          'pervasive-use'
    ]

    finalChar_ar = []
    for characteristic in characteristics_arr : 
        event_state = getattr(event.find(characteristic), 'text', 'no')
        if event_state == 'yes':
            finalChar_ar.append(characteristic)

    delimiter = ' '
    event_data.append(delimiter.join(finalChar_ar))

    csvwriter.writerow(event_data)
csv_data.close()
