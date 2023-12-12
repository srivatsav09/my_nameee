from import_export import resources
from .models import CSV

class CSVResources(resources.ModelResource):
    class Meta:
        model = CSV