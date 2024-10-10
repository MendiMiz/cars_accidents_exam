import csv
from database.connect import daily_based, weekly_based, monthly_based
from utils.data_utils import parse_date, extract_year, get_week_start


def read_csv(csv_path):
   with open(csv_path, 'r') as file:
       csv_reader = csv.DictReader(file)
       for row in csv_reader:
           yield row


def init_car_accidents():
   daily_based.drop()
   weekly_based.drop()
   monthly_based.drop()


   for row in read_csv('../data/data.csv'):
       daily = {
           'date': parse_date(row['CRASH_DATE']),
           'area': row['BEAT_OF_OCCURRENCE'],
           'injuries': {
               'total': int(row['INJURIES_TOTAL']),
               'fatal': int(row['INJURIES_FATAL']),
               'non_fatal': int(row['INJURIES_TOTAL']) - int(row['INJURIES_FATAL'])
           },
           'contributing_factor': row['PRIM_CONTRIBUTORY_CAUSE']
       }

       daily_based.insert_one(daily)

       weekly = {
           'week_start': get_week_start(row['CRASH_DATE']),
           'area': row['BEAT_OF_OCCURRENCE'],
           'injuries': {
               'total': int(row['INJURIES_TOTAL']),
               'fatal': int(row['INJURIES_FATAL']),
               'non_fatal': int(row['INJURIES_TOTAL']) - int(row['INJURIES_FATAL'])
           },
           'contributing_factor': row['PRIM_CONTRIBUTORY_CAUSE']
       }

       weekly_based.insert_one(weekly)

       monthly = {
           'month': int(row['CRASH_MONTH']),
           'year': extract_year(row['CRASH_DATE']),
           'area': row['BEAT_OF_OCCURRENCE'],
           'injuries': {
               'total': int(row['INJURIES_TOTAL']),
               'fatal': int(row['INJURIES_FATAL']),
               'non_fatal': int(row['INJURIES_TOTAL']) - int(row['INJURIES_FATAL'])
           },
           'contributing_factor': row['PRIM_CONTRIBUTORY_CAUSE']
       }

       monthly_based.insert_one(monthly)

       print(monthly)

       # car_id = products.insert_one(product).inserted_id
       # if row['CustomerID']:
       #     customer = {
       #         '_id': int(row['CustomerID']),
       #         'country': row['Country']
       #     }
       #     customers.update_one({'_id': int(row['CustomerID'])}, {'$set': customer}, upsert=True)
       #
       # invoice_id = row['InvoiceNo']
       # invoice = invoices.find_one({'_id': invoice_id})
       #
       # # If the invoice already exists, append the product, otherwise create a new invoice
       # if invoice:
       #     invoices.update_one(
       #         {'_id': invoice_id},
       #         {'$push': {
       #             'products': {
       #                 'product_id': row['StockCode'],
       #                 'quantity': int(row['Quantity']),
       #                 'unit_price': float(row['UnitPrice'])
       #             }
       #         }}
       #     )
       # else:
       #     new_invoice = {
       #         '_id': invoice_id,
       #         'invoice_date': row['InvoiceDate'],
       #         'customer_id': int(row['CustomerID']) if row['CustomerID'] else None,
       #         'products': [{
       #             'product_id': row['StockCode'],
       #             'quantity': int(row['Quantity']),
       #             'unit_price': float(row['UnitPrice'])
       #         }]
       #     }
       #     invoices.insert_one(new_invoice)

init_car_accidents()