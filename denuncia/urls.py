from cruds.urls import crud_urls, crud_for_app 
from denuncia.models import Denuncia

from denuncia.views import DenunciaCreateView

urlpatterns = []
urlpatterns += crud_urls(Denuncia, create_view=DenunciaCreateView.as_view())

