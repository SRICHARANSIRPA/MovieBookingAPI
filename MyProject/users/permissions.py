from rest_framework.permissions import BasePermission, SAFE_METHODS
from MyProject.users.serializers import *


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class UserBasePermission:
    user = None
    attr = None

    def __init__(self, user, attr):
        self.user = user
        self.attr = attr

    def check_for_permission(self):
        if self.user.is_anonymous:
            return False
        current_role = UserRole.objects.filter(user=self.user,is_current=True).first()
        if not current_role:
            return False
        flag = True

        for i in self.attr:
            flag = flag & current_role.role.__getattribute__(i)
        # print('flag -',flag)
        return flag

    def check_object_permission(self):
        if self.user.is_anonymous:
            return False
        current_role = UserRole.objects.filter(user=self.user, is_current=True).first()
        if not current_role:
            return False
        return current_role.role.Name == 'Admin' | current_role.role


class TicketBooking(BasePermission):
    def __init__(self):
        self.UserBasePermission = None

    def has_permission(self, request, view):
        self.UserBasePermission = UserBasePermission(request.user, ['can_book_ticket'])
        return self.UserBasePermission.check_for_permission()

    # def has_object_permission(self, request, view, obj):
    #     self.UserBasePermission = UserBasePermission(request.user, ['can_book_ticket'])


class CancelTicket(BasePermission):
    def __init__(self):
        self.UserBasePermission = None

    def has_permission(self, request, view):
        self.UserBasePermission = UserBasePermission(request.user, ['can_cancel_ticket'])
        return self.UserBasePermission.check_for_permission()


class AddCinema(BasePermission):
    def __init__(self):
        self.UserBasePermission = None

    def has_permission(self, request, view):
        self.UserBasePermission = UserBasePermission(request.user, ['can_add_cinema'])
        return self.UserBasePermission.check_for_permission()


class UpdateTicket(BasePermission):
    def __init__(self):
        self.UserBasePermission = None

    def has_permission(self, request, view):
        self.UserBasePermission = UserBasePermission(request.user, ['can_update_ticket'])
        return self.UserBasePermission.check_for_permission()


class AddTicket(BasePermission):
    def __init__(self):
        self.UserBasePermission = None

    def has_permission(self, request, view):
        self.UserBasePermission = UserBasePermission(request.user, ['can_add_ticket'])
        return self.UserBasePermission.check_for_permission()


class IsAdmin(BasePermission):
    def __init__(self):
        self.UserBasePermission = None

    def has_permission(self, request, view):
        self.UserBasePermission = UserBasePermission(request.user, ['can_add_ticket','can_update_ticket', 'can_add_cinema', 'can_cancel_ticket','can_book_ticket'])
        return self.UserBasePermission.check_for_permission()

