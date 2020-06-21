import django_filters
from django_filters import DateFilter, CharFilter
from .models import *

class OrderFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name = 'pub_date', lookup_expr='gte', label='Start Date')
	end_date = DateFilter(field_name = 'pub_date', lookup_expr='lte', label='End Date')

	class Meta:
		model = Order
		fields = '__all__'
		exclude = ['customer', 'pub_date']