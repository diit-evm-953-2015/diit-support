from django.conf.urls import patterns, url

urlpatterns = patterns('privatemessages.views',
    url(r'^send_message/$', 'send_message_view', name='send_message'),
    url(r'^send_message_onpage/(?P<recipient_id>\d+)/$', 'send_message_onpage_view',),
    url(r'^send_message_api/(?P<thread_id>\d+)/$', 'send_message_api_view', name='send_message_api'),
    url(r'^chat/(?P<thread_id>\d+)/$', 'chat_view',name='chat'),
    url(r'^$', 'messages_view'),
)