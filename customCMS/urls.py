from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('login_admin', views.admin_login),
    url('home_cms', views.HomeCMSView.as_view({'get': 'home_cms_list'})),
    url('activated_home_cms', views.ActvatedHomeCMSView.as_view({'get': 'activated_list'})),
    url('edit_home_cms/<int:pk>', views.EditHomeCMS.as_view()),
    url('active_home_cms/<int:pk>', views.ActiveHomeCMS.as_view()),
    url('category_cms', views.CategoryCMSView.as_view({'get': 'category_cms_list'})),
    url('edit_category_cms/<int:pk>', views.EditCategoryCMS.as_view()),
    url('activated_category_cms', views.ActvatedCategoryCMSView.as_view({'get': 'activated_list'})),
    url('active_category_cms/<int:pk>', views.ActiveCategoryCMS.as_view()),
    url('contact_cms', views.ContactCMSView.as_view({'get': 'contact_cms_list'})),
    url('edit_contact_cms/<int:pk>', views.EditContactCMS.as_view()),
    url('activated_contact_cms', views.ActivatedContactCMSView.as_view({'get': 'activated_list'})),
    url('active_contact_cms/<int:pk>', views.ActiveContactCMS.as_view()),
    url('about_cms', views.AboutCMSView.as_view({'get': 'about_cms_list'})),
    url('edit_about_cms/<int:pk>', views.EditAboutCMS.as_view()),
    url('activated_about_cms', views.ActivatedAboutCMSView.as_view({'get': 'activated_list'})),
    url('active_about_cms/<int:pk>', views.ActiveAboutCMS.as_view()),
    url('cms_category', views.CategoryView.as_view({'get': 'category_cms_list'})),
    url('edit_category/<int:pk>', views.EditCategory.as_view()),
    url('category_status/<int:pk>', views.CategoryStatus.as_view()),
    url('footer_cms', views.FooterCMSView.as_view({'get': 'footer_list'})),
    url('activated_footer_cms', views.ActivatedFooterCMSView.as_view({'get': 'activated_list'})),
    url('edit_footer_cms/<int:pk>', views.EditFooterCMS.as_view()),
    url('active_footer_cms/<int:pk>', views.ActiveFooterCMS.as_view()),
    url('edit_contact_form/<int:pk>', views.EditContactForm.as_view()),
    url('get_contact_form/<int:pk>', views.GetContactForm.as_view()),
]
