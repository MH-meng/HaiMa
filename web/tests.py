from web import models
from django.utils import timezone


# 自定义的函数，不是视图
def change_info(request):  # 修改网站访问量和访问ip等信息
    # 每一次访问，网站总访问次数加一
    count_nums = models.VisitNumber.objects.filter(id=1)
    if count_nums:
        count_nums = count_nums[0]
        count_nums.count += 1
    else:
        count_nums = models.VisitNumber()
        count_nums.count = 1
    count_nums.save()

    # 记录访问ip和每个ip的次数
    if 'HTTP_X_FORWARDED_FOR' in request.META:  # 获取ip
        client_ip = request.META['HTTP_X_FORWARDED_FOR']
        client_ip = client_ip.split(",")[0]  # 所以这里是真实的ip
    else:
        client_ip = request.META['REMOTE_ADDR']  # 这里获得代理ip
    # print(client_ip)

    ip_exist = models.Interview.objects.filter(useip=str(client_ip))
    if ip_exist:  # 判断是否存在该ip
        uobj = ip_exist[0]
        uobj.people += 1
    else:
        uobj = models.Interview()
        uobj.useip = client_ip
        uobj.people = 1
    uobj.save()

    # 增加今日访问次数
    date = timezone.now().date()
    today = models.DayNumber.objects.filter(day=date)
    if today:
        temp = today[0]
        temp.count += 1
    else:
        temp = models.DayNumber()
        temp.dayTime = date
        temp.count = 1
    temp.save()


