from rest_framework import permissions

class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    仅管理员可以进行修改，其他用户有查看权限。
    自定义的权限类继承了 BasePermission 这个基础的父类，
    并实现了父类中的钩子方法 def has_permission。
    此方法在每次请求到来时被唤醒执行，里面简单判断了请求的种类是否安全（即不更改数据的请求），
    如果安全则直接通过，不安全则只允许管理员用户通过。
    """

    def has_permission(self, request, view):
        # 所有用户都可以进行GET HEAD OPTIONS请求
        if request.method in permissions.SAFE_METHODS:
            return True
        # 仅管理员可进行其它操作
        return request.user.is_superuser
