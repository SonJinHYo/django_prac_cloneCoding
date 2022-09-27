from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    # first,last name은 서양식. editable = False를 해서 사용하지 않게 설정
    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, blank=True,editable=False)
    # 대신 name을 설정. 단, 이 업데이트는 기존 사용자의 정보도 건들기 때문에 디폴트값을 정해주어야 migrations이 가능하다
    name = models.CharField(max_length=150,default='NoName')

    # models.py를 수정할 때 마다 migration을 만들고 migrate를 해주어야 한다.
    # python코드와 db를 동기화 해주기 위해서!
    is_host = models.BooleanField(default=False)