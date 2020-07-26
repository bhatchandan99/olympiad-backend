from django.conf.urls import url
from .views import QuizListView, CategoriesListView,\
    ViewQuizListByCategory, QuizUserProgressView, QuizMarkingList,\
    QuizMarkingDetail, QuizDetailView, QuizTake, index,profile, login_user, logout_user,contact,examdates,faqs,coordinator,register_school,myquiz,home,handlerequest,handleresponse
from django.urls import path
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [         path('applyindividual/',view =  views.register, name="applyindividual"),
                        path('applyschool/',view =  views.register_school, name="applyschool"),
                        path('examdates/',view =  views.examdates, name="examdates"),
                        path('faqs/',view =  views.faqs, name="faqs"),
                        path('coordinator/',view =  views.coordinator, name="coordinator"),
                        path('paper/',view =  views.paper, name="paper"),
                        path('subscriptions/profile/',view =  views.profile, name="profile"),
                        path('subscriptions/change-password/' ,view=views.change_password, name="change_password"),
                        path('loginhandle/reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name="reset_password"),
                        path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name="password_reset_done"),
                        path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name="password_reset_confirm"),
                        path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),name="password_reset_complete"),
                        path("request/",views.handlerequest, name="request"),
                        path("response/",views.handleresponse, name="response"),
                        path("home/",views.home, name="home"),
                        path("update_student/",views.update_student, name="update_student"),

                        # path("loginhandle/",views.loginhandle, name="loginhandle"),
                        path("loginhandle/",views.login_user, name="loginhandle"),
                        #path("loginhandle/subscriptions/", views.subscriptions, name="subscriptions"),
                        # path("loginhandle/logouthandle/",views.logouthandle, name="logouthandle"),
                        path("loginhandle/logouthandle/",views.logout_user, name="logout"),
                        path('activate/<uidb64>/<token>/', views.ActivateAccount.as_view(), name='activate'),
                        path("contact/",views.contact, name="contact"),
                        path("subscriptions/",view = views.subscribe , name="subscriptions"),

                        url(regex=r'^$', view=index, name='index'),
                        # url(regex=r'^login/$', view=login_user, name='login'),
                        # url(regex=r'^logout/$', view=logout_user, name='logout'),
                       url(regex=r'^quizzes/$',
                           view= views.myquiz,
                           name='quiz_index'),

                       url(regex=r'^category/$',
                           view=CategoriesListView.as_view(),
                           name='quiz_category_list_all'),

                       url(regex=r'^category/(?P<category_name>[\w|\W-]+)/$',
                           view=ViewQuizListByCategory.as_view(),
                           name='quiz_category_list_matching'),

                       url(regex=r'^progress/$',
                           view=QuizUserProgressView.as_view(),
                           name='quiz_progress'),

                       url(regex=r'^marking/$',
                           view=QuizMarkingList.as_view(),
                           name='quiz_marking'),

                       url(regex=r'^marking/(?P<pk>[\d.]+)/$',
                           view=QuizMarkingDetail.as_view(),
                           name='quiz_marking_detail'),

                       #  passes variable 'quiz_name' to quiz_take view
                       url(regex=r'^(?P<slug>[\w-]+)/$',
                           view=QuizDetailView.as_view(),
                           name='quiz_start_page'),

                       url(regex=r'^(?P<quiz_name>[\w-]+)/take/$',
                           view=QuizTake.as_view(),
                           name='quiz_question'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
