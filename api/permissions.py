from rest_framework import permissions


class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # bu faqat user ko`rish uchun yozilgan
        if request.method in permissions.SAFE_METHODS:
            return True
        # bu faqat superuser o`zgartirish uchun yozilgan
        return obj.author == request.user
