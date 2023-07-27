from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
app_name = 'myapp'
urlpatterns = [
    path('', Test.as_view(), name='Test'),
    path('DashboardView/', DashboardView.as_view(), name='DashboardView'),
    path('DashboardColorView/', DashboardColorView.as_view(), name='DashboardColorView'),


    path('BuyerView/', BuyerView.as_view(), name='BuyerView'),
    path('StyleView/', StyleView.as_view(), name='StyleView'),
    path('ProductionLineView/', ProductionLineView.as_view(), name='ProductionLineView'),
    path('OrderQtyView/<int:id>/', OrderQtyView.as_view(), name='OrderQtyView'),
    path('SaveOrderQty/', SaveOrderQty.as_view(), name='SaveOrderQty'),
    path('OrederCMPreportView/', OrederCMPreportView.as_view(), name='OrederCMPreportView'),
    path('OrderQtyDetailView/<int:id>/',OrderQtyDetailView.as_view(), name='OrderQtyDetailView'),
    path('EditOrderQtyView/<int:pk>', EditOrderQtyView.as_view(), name='EditOrderQtyView'),
    path('ETAView/', ETAView.as_view(), name='ETAView'),

    path('ProductionInputView/', ProductionInputView.as_view(), name='ProductionInputView'),
    path('DailyProductionView/', DailyProductionView.as_view(), name='DailyProductionView'),
    path('DailyTargetView/', DailyTargetView.as_view(), name='DailyTargetView'),
    path('DailyTargetFilterView/', DailyTargetFilterView, name='DailyTargetFilterView'),
    path('LineDataEntryView/', LineDataEntryView, name='LineDataEntryView'),
    path('LineDataEntrySave/', LineDataEntrySave.as_view(), name='LineDataEntrySave'),
    path('ProductionLineOutputDetail/', ProductionLineOutputDetail.as_view(), name='ProductionLineOutputDetail'),

    path('DailyAttendanceView/', DailyAttendanceView.as_view(), name='DailyAttendanceView'),

    path('AccInventoyList/', AccInventoyList.as_view(), name='AccInventoyList'),
    path('AccVarientList/', AccVarientList.as_view(), name='AccVarientList'),
    path('create/', ProductCreate.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdate.as_view(), name='update_product'),
    path('delete-image/<int:pk>/', delete_image, name='delete_image'),
    path('delete-variant/<int:pk>/', delete_variant, name='delete_variant'),
    path('WarehouseMgrView/', WarehouseMgrView.as_view(), name='WarehouseMgrView'),
    path('AccRequestStatusChange/<int:pk>/', AccRequestStatusChange.as_view(), name='AccRequestStatusChange'),
    path('WH_to_Production_Acc/', WH_to_Production_Acc.as_view(), name='WH_to_Production_Acc'),

    path('FabricInvoiceList/', FabricInvoiceList.as_view(),name='FabricInvoiceList'),
    path('fabriccreate/', FabricProductCreate.as_view(), name='create_fabric'),
    path('fabricupdate/<int:pk>/', FabricProductUpdate.as_view(), name='update_fabric'),
    path('delete_fabric_image/<int:pk>/', delete_fabric_image, name='delete_fabric_image'),
    path('delete_fabric/<int:pk>/', delete_fabric, name='delete_fabric'),
    path('FabricRequesttoWH/', FabricRequesttoWH.as_view(), name='FabricRequesttoWH'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)