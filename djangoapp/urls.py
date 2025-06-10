from django.urls import path
from .import views as v



urlpatterns =[
    path('',v.home,name='home'),
    path('package/',v.package,name='package'),
    path('about/',v.about,name='about'),
    path('contact/',v.contact,name='contact'),
    path('userreg/', v.userreg, name='userreg'),
    path('uselog/', v.uselog, name='uselog'),
    path('logout/',v.usrlogout,name='logout'),
    path('vendor/',v.vendor,name='vendor'),
    path('vendsignin/',v.vendsignin,name='vendsignin'),
    path('booking/',v.booking,name='booking'),
    path('packreg/',v.packreg,name='packreg'),
    path('kerala/',v.kerala,name='kerala'),
    path('kashmir/',v.kashmir,name='kashmir'),
    path('dubai/',v.dubai,name='dubai'),
    path('paris/',v.paris,name='paris'),
    path('approvedpack/',v.approvedpack,name='approvedpack'),
   
   
   
]