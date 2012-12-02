from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns("chat.views",
    url("^chat/create/$", "create", name="create"),
    url("^chat/system_message/$", "system_message", name="system_message"),
    url("^chat/(?P<slug>.*)$", "room", name="room"),
)
