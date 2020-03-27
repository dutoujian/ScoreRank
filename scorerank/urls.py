from django.conf.urls import url
from scorerank.views import AddScoreView, QueryScoreView

urlpatterns = [
    url(r'^add$', AddScoreView.as_view(), name='add'), # 增加客户分数信息
    url(r'^query$', QueryScoreView.as_view(), name='query'), # 获取分数信息
]