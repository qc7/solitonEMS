from django.urls import path

from contracts import views

urlpatterns = [
    path("manage_job_contracts", views.manage_job_contracts, name="manage_job_contracts"),
    path("view_user_contracts", views.view_user_contracts, name="view_user_contracts"),
    path("terminate_contract/<int:contract_id>/", views.terminate_contract, name="terminate_contract"),
    path("edit_contract_page/<int:contract_id>/", views.edit_contract_page, name="edit_contract_page"),
    path("terminated_contracts", views.terminated_contracts_page, name="terminated_contracts_page")
]
