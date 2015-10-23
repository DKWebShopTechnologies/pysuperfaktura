__author__ = 'backslash7 <lukas.stana@it-admin.sk>'

from pysuperfaktura.exceptions import SFAPIException


class SFInvoiceItem:
    """

    """

    def __init__(self, params):
        """

        """
        self.params = params


class SFInvoice:
    def __init__(self, client, params, items=None):
        self.client = client
        self.params = params
        self.items = items
        self.id = params.get('id', None)

    def add_item(self, item):
        """
        @param item:SFInvoiceItem instance
        """
        if not isinstance(SFInvoiceItem, item):
            raise SFAPIException('Passed object is not a SFInvoiceItem instance')

        if self.items:
            self.items.append(item)
        else:
            self.items = [item]




class SFInvoiceClient:
    def __init__(self, params):
        self.params = params

class SFInvoicePayment:
    def __init__(self, invoice, params):
        self.client = invoice.client
        self.invoice = invoice
        self.params = params
        self.params['invoice_id'] = invoice.id

    def save(self):
        invoice = self.invoice
        data = {'Client': invoice.client.params, 'Invoice': invoice.params, 'InvoiceItem': []}

        retv = self.send_request('invoice_payments/add/ajax:1/api:1', method='POST', data={'data': json.dumps(data)})
