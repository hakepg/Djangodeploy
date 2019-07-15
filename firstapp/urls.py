from firstapp.views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter
router.register(r'addresses',AddressViewset)
router.register(r'Companies',CompanyViewset)
router.register(r'addresses]',EmployeViewset)
