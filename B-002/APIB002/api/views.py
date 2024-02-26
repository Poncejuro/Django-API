
from django.http import  JsonResponse
from django.http.response import HttpResponse as HttpResponse
from django.views import View
from .models import CryptoCurrency, CryptoCurrencyHistory
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime

# Create your views here.
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .models import CryptoCurrency

class CryptoCurrencyView(View):
    """
    A view to handle CRUD operations for CryptoCurrency objects.
    """

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        """
        Dispatch method to handle CSRF exemption and call superclass dispatch.
        """
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, ID=0):
        """
        Handle GET request to retrieve CryptoCurrency(s) based on ID.
        """
        try:
            if ID > 0:
                currency = CryptoCurrency.objects.get(ID=ID)
                data = {'message': "Success", 'currency': {'ID': currency.ID, 'name': currency.name, 'image': currency.image}}
            else:
                currencies = CryptoCurrency.objects.all()
                if currencies:
                    data = {'message': "Success", 'currencies': [{'ID': currency.ID, 'name': currency.name, 'image': currency.image} for currency in currencies]}
                else:
                    data = {'message': 'Currency not found'}
        except CryptoCurrency.DoesNotExist:
            data = {'message': 'Currency not found'}
        return JsonResponse(data)

    def post(self, request):
        """
        Handle POST request to create a new CryptoCurrency object.
        """
        try:
            jd = json.loads(request.body)
            CryptoCurrency.objects.create(name=jd['name'], image=jd['image'])
            data = {'message': "Success"}
        except json.JSONDecodeError:
            data = {'message': 'Invalid JSON data'}
        except KeyError:
            data = {'message': 'Missing name or image in JSON data'}
        return JsonResponse(data)

    def put(self, request, ID):
        """
        Handle PUT request to update an existing CryptoCurrency object.
        """
        try:
            jd = json.loads(request.body)
            currency = CryptoCurrency.objects.get(ID=ID)
            currency.name = jd['name']
            currency.image = jd['image']
            currency.save()
            data = {'message': "Success", 'currency': {'ID': currency.ID, 'name': currency.name, 'image': currency.image}}
        except CryptoCurrency.DoesNotExist:
            data = {'message': 'Currency not found'}
        except json.JSONDecodeError:
            data = {'message': 'Invalid JSON data'}
        except KeyError:
            data = {'message': 'Missing name or image in JSON data'}
        return JsonResponse(data)

    def delete(self, request, ID):
        """
        Handle DELETE request to delete a CryptoCurrency object based on ID.
        """
        try:
            currency = CryptoCurrency.objects.get(ID=ID)
            currency.delete()
            data = {'message': "Success"}
        except CryptoCurrency.DoesNotExist:
            data = {'message': 'Currency not found'}
        return JsonResponse(data)




class CryptoCurrencyHistoryView(View):
    """
    A view to handle CRUD operations for CryptoCurrencyHistory objects.
    """

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        """
        Dispatch method to handle CSRF exemption and call superclass dispatch.
        """
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, ID=0):
        """
        Handle GET request to retrieve CryptoCurrencyHistory(s) based on ID.
        """
        try:
            if ID > 0:
                currency_history = CryptoCurrencyHistory.objects.get(ID=ID)
                data = {'message': "Success", 'currency_history': {'ID': currency_history.ID, 'currency_id': currency_history.currency_id, 'date': currency_history.date, 'price': currency_history.price}}
            else:
                currency_histories = CryptoCurrencyHistory.objects.all()
                if currency_histories:
                    data = {'message': "Success", 'currency_histories': [{'ID': currency_history.ID, 'currency_id': currency_history.currency_id, 'date': currency_history.date, 'price': currency_history.price} for currency_history in currency_histories]}
                else:
                    data = {'message': 'Currency history not found'}
        except CryptoCurrencyHistory.DoesNotExist:
            data = {'message': 'Currency history not found'}
        return JsonResponse(data)

    def post(self, request):
        """
        Handle POST request to create a new CryptoCurrencyHistory object.
        """
        try:
            data = json.loads(request.body)
            currency_id = data.get('currency_id')

            if not CryptoCurrency.objects.filter(ID=currency_id).exists():
                return JsonResponse({'message': 'Currency not found'}, status=404)
            currency = CryptoCurrency.objects.get(ID=currency_id)

            CryptoCurrencyHistory.objects.create(currency=currency, date=data['date'], price=data['price'])
            data = {'message': 'Success'}
        except json.JSONDecodeError:
            data = {'message': 'Invalid JSON data'}
        except KeyError:
            data = {'message': 'Missing currency_id, date, or price in JSON data'}
        return JsonResponse(data)

    def put(self, request, ID):
        """
        Handle PUT request to update an existing CryptoCurrencyHistory object.
        """
        try:
            data = json.loads(request.body)
            post = CryptoCurrencyHistory.objects.get(ID=ID)
            post.date = data['date']
            post.price = data['price']
            if 'currency_id' in data:
                currency_id = data['currency_id']
                currency = CryptoCurrency.objects.get(ID=currency_id)
                post.currency = currency
            post.save()

            date_obj = datetime.strptime(post.date, '%Y-%m-%d')

            data = {
                'message': 'Success',
                'currency_history': {
                    'ID': post.ID,
                    'currency_id': post.currency_id if post.currency else None,
                    'date': date_obj.strftime('%Y-%m-%d'),
                    'price': str(post.price),
                }
            }
        except CryptoCurrencyHistory.DoesNotExist:
            data = {'message': 'Currency history not found'}
        except json.JSONDecodeError:
            data = {'message': 'Invalid JSON data'}
        except KeyError:
            data = {'message': 'Missing currency_id, date, or price in JSON data'}
        return JsonResponse(data)

    def delete(self, request, ID):
        """
        Handle DELETE request to delete a CryptoCurrencyHistory object based on ID.
        """
        try:
            currency_history = CryptoCurrencyHistory.objects.get(ID=ID)
            currency_history.delete()
            data = {'message': 'Success'}
        except CryptoCurrencyHistory.DoesNotExist:
            data = {'message': 'Currency history not found'}
        return JsonResponse(data)
    

    
class CryptoCurrencyHistoryListView(View):
    """
    A view to retrieve a list of all cryptocurrencies with their history.
    """

    def get(self, request):
        """
        Handle GET request to retrieve all cryptocurrencies with their history.
        """
        try:
            all_cryptocurrencies = CryptoCurrency.objects.all()
            response_data = []

            for cryptocurrency in all_cryptocurrencies:
                cryptocurrency_histories = cryptocurrency.cryptocurrencyhistory_set.all()
                history_data = []
                for history in cryptocurrency_histories:
                    history_entry = {
                        'date': history.date.strftime('%d/%m/%Y'),
                        'price': str(history.price)
                    }
                    history_data.append(history_entry)

                cryptocurrency_data = {
                    'currency_name': cryptocurrency.name,
                    'image': cryptocurrency.image,
                    'history': history_data
                }
                response_data.append(cryptocurrency_data)

            return JsonResponse(response_data, safe=False)
        except Exception as e:
            return JsonResponse({'message': 'An error occurred while processing the request', 'error': str(e)}, status=500)