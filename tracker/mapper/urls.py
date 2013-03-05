from django.conf.urls import patterns
#from django.views.generic.simple import redirect_to, direct_to_template
from django.views.generic.base import TemplateView

urlpatterns = patterns( 
                       '',
                       ( r'^$', TemplateView.as_view(template_name='map.html') ),
                       ( r'^plain$', TemplateView.as_view(template_name='map_plain.html') ),
                       ( r'^upload$', TemplateView.as_view(template_name='upload.html') ),

 )
