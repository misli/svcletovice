from leprikon.site.urls import *


urlpatterns = [
    path('survey/', include('cmsplugin_survey.urls', namespace='survey')),
] + urlpatterns
