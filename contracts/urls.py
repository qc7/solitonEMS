from django.urls import path

from contracts import views

urlpatterns = [

    path("manage_job_contracts", views.manage_job_contracts, name="manage_job_contracts"),
    path("terminate_contract/<int:contract_id>/", views.terminate_contract, name="terminate_contract"),
    path("edit_contract_page/<int:contract_id>/", views.edit_contract_page, name="edit_contract_page"),
    path("terminated_contracts", views.terminated_contracts_page, name="terminated_contracts_page"),
    path("activate_contract/<int:contract_id>/", views.activate_contract, name="activate_contract"),
    path("user_contracts_page", views.user_contracts_page, name="user_contracts_page"),

]
