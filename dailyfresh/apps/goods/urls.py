from django.conf.urls import url
from goods.views import DetailView

urlpatterns = [
    # url(r'^$', IndexView.as_view(), name='index'), # 首页
    url(r'^$', DetailView.as_view(), name='detail'), # 首页
]
