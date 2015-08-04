# -*- coding: utf8 -*-
"""
Forms for Helios
"""


from django import forms
from models import Election
from widgets import *
from fields import *
from django.conf import settings


class ElectionForm(forms.Form):
  short_name = forms.SlugField(max_length=25, label="نام کوتاه", help_text='فاصله ای در این قسمت استفاده نکنید: sharif-elect-2015')
  name = forms.CharField(max_length=100, label="نام کامل", widget=forms.TextInput(attrs={'size':60}), help_text='نام کامل برای انتخابات را وارد کنید: انتخابات شریف ۲۰۱۵')
  description = forms.CharField(max_length=4000, label="توضیحات", widget=forms.Textarea(attrs={'cols': 70, 'wrap': 'soft'}), required=False)
  election_type = forms.ChoiceField(label="نوع انتخابات", choices = Election.ELECTION_TYPES)
  use_voter_aliases = forms.BooleanField(required=False, initial=False, label="استفاده از نام مستعار رای‌دهنده", help_text='اگر این گزینه را انتخاب کنید، نام رای‌دهنده با یک اسم مستعار بری مثال "V12" جایگزین خواهد شد')
  #use_advanced_audit_features = forms.BooleanField(required=False, initial=True, help_text='disable this only if you want a simple election with reduced security but a simpler user interface')
  randomize_answer_order = forms.BooleanField(required=False, initial=False, label="تصادفی بودن پاسخ‌ها", help_text='این گزینه را انتخاب کنید در صورتی که می‌خواهید گزینه ها برای رای‌دهنده در ترتیب تصادفی نمایش داده شوند')
  private_p = forms.BooleanField(required=False, initial=False, label="خصوصی؟", help_text='یک انتخابات خصوصی تنها برای رای‌دهندگان ثبت‌نام شده باز خواهد بود')
  help_email = forms.CharField(required=False, initial="", label="پست‌الکترونیک کمک", help_text='پست‌الکترونیک برای اینکه رای‌دهنده برای دریافت کمک با شما مکاتبه کند.')
  
  if settings.ALLOW_ELECTION_INFO_URL:
    election_info_url = forms.CharField(required=False, initial="", label="آدرس دریافت اطلاعات انتخابات", help_text="آدرس دریافت فایل PDF اطلاعات اضافی انتخابات برای مثال گفته‌های متقاضیان")
  

class ElectionTimesForm(forms.Form):
  # times
  voting_starts_at = SplitDateTimeField(help_text = 'UTC date and time when voting begins',
                                   widget=SplitSelectDateTimeWidget)
  voting_ends_at = SplitDateTimeField(help_text = 'UTC date and time when voting ends',
                                   widget=SplitSelectDateTimeWidget)

  
class EmailVotersForm(forms.Form):
  subject = forms.CharField(max_length=80)
  body = forms.CharField(max_length=4000, widget=forms.Textarea)
  send_to = forms.ChoiceField(label="Send To", initial="all", choices= [('all', 'all voters'), ('voted', 'voters who have cast a ballot'), ('not-voted', 'voters who have not yet cast a ballot')])

class TallyNotificationEmailForm(forms.Form):
  subject = forms.CharField(max_length=80)
  body = forms.CharField(max_length=2000, widget=forms.Textarea, required=False)
  send_to = forms.ChoiceField(label="Send To", choices= [('all', 'all voters'), ('voted', 'only voters who cast a ballot'), ('none', 'no one -- are you sure about this?')])

class VoterPasswordForm(forms.Form):
  voter_id = forms.CharField(max_length=50, label="Voter ID")
  password = forms.CharField(widget=forms.PasswordInput(), max_length=100)

