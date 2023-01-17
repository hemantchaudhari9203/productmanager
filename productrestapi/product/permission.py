from rest_framework import permissions
class employee_permissions(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user=request.user
        if user.is_staff:
            if user.has_perm("product.add_product"): #appname.verb_modelname [verb:[add,change, delete, view]]
                return True
            if user.has_perm("product.delete_product"):
                return True
            if user.has_perm("product.view_product"):
                return True
            if user.has_perm("product.change_product"):
                return True
            return False
        return False


    # def has_object_permission(self, request, view, obj):
    #     return obj.owner==request.user