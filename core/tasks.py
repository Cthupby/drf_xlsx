import base64
import pandas

from .models import Bill

def add(excel_file_base64):
    excel_file = base64.b64decode(excel_file_base64)
    df = pandas.read_excel(excel_file)
    '''
    • в service не пусто ( пусто так же считается, если вместо текста знак “-”)
    • client_name, client_org не пустые 
    '''
    df_filtered_by_str = df.loc[(df['service' or 'client_name' or 'client_org'] != None) & \
                                (df['service'] != '-')]
    '''
    • значение sum является числом
    • №(номер счет) тип  int
    '''
    df_filtered_by_int = df_filtered_by_str[pandas.to_numeric(df_filtered_by_str['№' and 'sum'], errors='coerce').notnull()]
    '''
    • корректная дата (дата считается корректной, если есть день, месяц и год).
    '''
    filtered_df = df_filtered_by_int[pandas.to_datetime(df_filtered_by_int['date'], format='%d%m%Y', errors='coerce').notnull()]
    for row in filtered_df.iterrows():
        r = row[1].to_list()
        if type(r[2] and r[3]) == int:
            Bill.objects.get_or_create(client_name=r[0], client_org=r[1], number=r[2],
                                amount=r[3], date=r[4], service=r[5])
