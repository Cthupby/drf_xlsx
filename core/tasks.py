import base64
import pandas

from .models import Bill

def add(excel_file_base64):
    excel_file = base64.b64decode(excel_file_base64)
    df = pandas.read_excel(excel_file)
    filtered_df = df.loc[df['service' or 'client_name' or 'client_org'] != None]
    for row in filtered_df.iterrows():
        r = row[1].to_list()
        if type(r[2] and r[3]) == int:
            Bill.objects.create(client_name=r[0], client_org=r[1], number=r[2],
                                amount=r[3], date=r[4], service=r[5])
