from django.conf.urls import url
#from user import views
from django.contrib.auth.decorators import login_required
from user.views import RegisterView,ActiveView,LoginView, LogoutView, UserInfoView, UserOrderView, AddressView

urlpatterns = [
    #　#对应于from user import views
    #url(r'^register$',views.register,name='register'),
    #url(r'^register_handle$', views.register_handle, name='register_handle'), # 注册处理
    url(r'register$',RegisterView.as_view(),name='register'),
    url(r'^active/(?P<token>.*)$', ActiveView.as_view(), name='active'),  # 用户激活
    #?P<token>作为关键字捕获？？？？ .*
    url(r'^login$', LoginView.as_view(), name='login'),  # 登录
    url(r'^logout$', LogoutView.as_view(), name='logout'),  # 注销登录

    url(r'^$', UserInfoView.as_view(), name='user'),  # 用户中心-信息页
    url(r'^order/(?P<page>\d+)$', UserOrderView.as_view(), name='order'),  # 用户中心-订单页
    url(r'^address$', AddressView.as_view(), name='address'),  # 用户中心-地址页
]
