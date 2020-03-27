from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

import time
import datetime

from scorerank.models import ClientInfo

# Create your views here.
class AddScoreView(View):

    """增加客户分数信息"""
    def post(self, request):

        # 接收参数
        score = request.POST.get('score')
        client_name = request.POST.get('client_name')

        # 参数校验
        if not all([score, client_name]):
            return JsonResponse({'code': 401, 'msg': '数据不完整', 'data': None})

        # 校验客户是否存在
        try:
            client_info = ClientInfo.objects.get(client_name=client_name)
        except ClientInfo.DoesNotExist:
            # 客户不存在
            client_info = None
        if client_info:
            client_info.score = score
            client_info.update_time = datetime.datetime.now()
            client_info.save()
            return JsonResponse({'code': 200, 'msg': '添加成功', 'data': None})
        else:
            client_info = ClientInfo.objects.create(client_name=client_name,score=score,create_time=datetime.datetime.now(),update_time=datetime.datetime.now())
            client_info.save()
            return JsonResponse({'code': 200, 'msg': '添加成功', 'data': None})


class QueryScoreView(View):
    """获取分数信息"""
    def get(self, request):

        # 接收参数
        client_name = request.GET.get('client_name')
        start_rank = request.GET.get('start_rank')
        end_rank = request.GET.get('end_rank')

        # 参数校验
        if not all([client_name]):
            return JsonResponse({'code': 401, 'msg': '参数不完整', 'data': None})

        # 校验客户是否存在
        try:
            single_client = ClientInfo.objects.filter(client_name=client_name,is_valid='1')
        except ClientInfo.DoesNotExist:
            # 客户不存在
            return JsonResponse({'code': 401, 'msg': '参数错误', 'data': None})
        client_infos = ClientInfo.objects.all().order_by('-score')
        client_list = []
        single_client_rank = {}
        rank = 1
        for client in client_infos:
            info = {}
            info["client_name"] = client.client_name
            info["score"] = client.score
            info["rank"] = rank
            if client_name == client.client_name:
                single_client_rank = info
            client_list.append(info)
            rank += 1
        if all([start_rank, end_rank]):
            start = int(start_rank)-1
            if start < 0:
                return JsonResponse({'code': 401, 'msg': '参数错误', 'data': None})
            client_list = client_list[start:int(end_rank)+1]
        client_list.append(single_client_rank)
        # 返回应答
        return JsonResponse({'code': 200, 'msg': '查询成功', 'data': client_list})