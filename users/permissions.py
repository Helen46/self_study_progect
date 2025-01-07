from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="admin").exists()


class IsYourObject(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj == request.user:
            return True
        return False


class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="teachers").exists()


class IsAutor(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.autor == request.user:
            return True
        return False
