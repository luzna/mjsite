from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from django.conf import settings
from django.conf.urls.static import static
import main
from main import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^/?$', 'main.views.index'),
    url(r'^kontakt/$', 'main.views.kontakt'),
    url(r'^odp/$', 'main.views.odp'),
    url(r'^koncerty/$', 'main.views.koncerty'),
    url(r'^bio/$', 'main.views.bio'),
    url(r'^nagrody/$', 'main.views.nagrody'),
    url(r'^mainpage/$', 'main.views.mainpage'),
    url(r'^galeria/$', 'main.views.galeria'),
    url(r'^media/$', 'main.views.media'),
    url(r'^przyjaciele/$', 'main.views.przyjaciele'),
    url(r'^guestbook/$', 'main.views.guestbook'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),
#    url(settings.STATIC_URL, 'django,views.static.server', {'document_root': settings.STATIC_ROOT})
)




