from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('signin', views.user_signin),
    path('register', views.register_user),
    path('category', views.CategoryView.as_view()),
    path('all_startups', views.AllStartupListing.as_view()),
    path('user/<int:pk>', views.UserDetail.as_view()),
    path('user_details/<int:pk>', views.UserAdditionalDetailsView.as_view()),
    path('user_ext_post', views.UserExtensionPostView.as_view({'get': 'user_extension_list'})),
    path('startup/<int:pk>', views.StartupListing.as_view()),
    path('startup_post', views.StartupPost.as_view({'get': 'startup_list'})),
    path('startupbyid/<int:pk>', views.StartupById.as_view()),
    path('change_password', views.ChangePassword.as_view()),
    path('product_image', views.ProductUploadImage.as_view()),
    path('product_post', views.ProductPost.as_view({'get': 'product_list'})),
    path('productbystartup/<int:pk>', views.ProductByStartup.as_view()),
    path('productbyid/<int:pk>', views.ProductById.as_view()),
    path('deletestartupbyid/<int:pk>', views.DeleteStartup.as_view()),
    path('user_logout/<int:pk>', views.UserLogOut.as_view()),
    path('editproduct/<int:pk>', views.EditProduct.as_view()),
    path('deleteproduct/<int:pk>', views.DeleteProduct.as_view()),
    path('startupbycat/<int:pk>', views.StartUpByCategory.as_view()),
    path('suwd/<int:pk>', views.StartupByIdWithDepth.as_view()),
    path('startup-products/<int:pk>', views.ProductByStartupNoAuth.as_view()),
    path('catbyid/<int:pk>', views.CategoryById.as_view()),
    path('update_post', views.UpdatePost.as_view({'get': 'update_list'})),
    path('updatebyproduct/<int:pk>', views.UpdatesByProduct.as_view()),
    path('updatebyid/<int:pk>', views.UpdateById.as_view()),
    path('deleteproductupdate/<int:pk>', views.DeleteProductUpdate.as_view()),
    path('editProductUpdate/<int:pk>', views.EditProductUpdate.as_view()),
    path('oauth/login/', views.SocialLoginView.as_view()),
    path('user_count', views.UserCount.as_view()),
<<<<<<< HEAD
]
=======
]
>>>>>>> 075f2352f3d91a3fc297fa5b48fe0a7d3d56e564
