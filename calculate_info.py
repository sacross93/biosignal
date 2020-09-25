import bisect
import csv
import datetime
import json
import os.path
import random
import re
import shutil
import tempfile
from ftplib import FTP
from itertools import product

import MySQLdb
import dateutil
import numpy as np
import pandas
import pytz
import requests
from django.conf import settings
from django.contrib.auth.models import User
from django.core.cache import cache
from django.db import connection
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, Http404
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from pyfluent.client import FluentSender

from sa_api.models import Device, Client, Bed, Channel, Room, FileRecorded, ClientBusSlot, Review, \
    DeviceConfigPresetBed, DeviceConfigItem, NumberInfoFile, WaveInfoFile, SummaryFileRecorded, NumberGEC, NumberPIV, \
    Annotation, AnnotationComment, AnnotationLike, Count_info
#from .forms import UploadFileForm, UploadReviewForm


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# AuthenticationForm 모델폼 import
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# jango.contrib.auth 내 함수 login을 import함.
# (views.py 내 정의한 함수 login과 구분하기 위해 auth_log로 재 명명함)
from django.contrib.auth import login as auth_login



tmp_data = dict()
for summary in SummaryFileRecorded.objects.all():
    month = summary.record.begin_date.strftime('%Y-%m')
    if month not in tmp_data.keys():
        tmp_data[month] = {'collected_files': 0, 'collected_hours': 0}
    tmp_data[month]['collected_files'] += 1
    tmp_data[month]['collected_hours'] += (summary.record.end_date -summary.record.begin_date).total_seconds( ) /3600

tmp_data.keys()

count_info = Count_info.objects.all()
count_info.delete()
for key in tmp_data.keys():
    #print(key)
    #print(tmp_data[key]['collected_files'])
    #print(tmp_data[key]['collected_hours'])

    count_info = Count_info(month=key,collected_files=tmp_data[key]['collected_files'], collected_hours=tmp_data[key]['collected_hours'])
    count_info.save()