# -*- coding:utf-8 -*-
"""
@Des: 角色管理
"""
from typing import List
from fastapi import Query, APIRouter, Security
from core.Auth import check_permissions
from core.Response import res_antd, success, fail
from schemas.role import CreateRole, UpdateRole, RoleList
from models.base import Role
from tortoise.queryset import F

router = APIRouter(prefix="/role")


@router.get(
    "/all",
    summary="所有角色下拉选项专用",
    dependencies=[Security(check_permissions, scopes=["user_role"])],
)
async def all_roles_options(user_id: int = Query(None)):
    # 查询启用的角色
    roles = (
        await Role.annotate(label=F("role_name"), value=F("id"))
        .filter(role_status=True)
        .values("label", "value")
    )
    user_roles = []
    if user_id:
        # 当前用户角色
        user_role = await Role.filter(user__id=user_id, role_status=True).values_list(
            "id"
        )
        user_roles = [i[0] for i in user_role]
    data = {"all_role": roles, "user_roles": user_roles}
    return success(msg="所有角色下拉选项专用", data=data)


@router.post(
    "", summary="角色添加", dependencies=[Security(check_permissions, scopes=["role_add"])]
)
async def create_role(post: CreateRole):
    """
    <h1>请求参数说明:</h1>
    <ul>
        <li>role_name: 角色名称(字符串)</li>
        <li>role_status: 角色状态(布尔值)</li>
        <li>role_desc: 角色描述(字符串)</li>
    </ul>
    """
    import time
    params = post.dict()
    for i in range(10000):
        result = await Role.create(**params)
        params.update({'role_name': '张三' + str(time.time())})

    if not result:
        return fail(msg="创建失败!")
    return success(msg="创建成功!")


@router.delete(
    "",
    summary="角色删除",
    dependencies=[Security(check_permissions, scopes=["role_delete"])],
)
async def delete_role(role_id: int):
    """
    删除角色
    :param role_id:
    :return:
    """
    role = await Role.get_or_none(pk=role_id)
    if not role:
        return fail(msg="角色不存在!")
    result = await Role.filter(pk=role_id).delete()
    if not result:
        return fail(msg="删除失败!")
    return success(msg="删除成功!")


@router.put(
    "",
    summary="角色修改",
    dependencies=[Security(check_permissions, scopes=["role_update"])],
)
async def update_role(post: UpdateRole):
    """
    更新角色
    :param post:
    :return:
    """
    data = post.dict()
    data.pop("id")
    result = await Role.filter(pk=post.id).update(**data)
    if not result:
        return fail(msg="更新失败!")
    return success(msg="更新成功!")


@router.get(
    "",
    summary="角色列表",
    response_model=RoleList,
    dependencies=[Security(check_permissions, scopes=["role_query"])],
)
async def get_all_role(
    pageSize: int = 10,
    current: int = 1,
    role_name: str = Query(None),
    role_status: bool = Query(None),
    create_time: List[str] = Query(None),
) -> RoleList:
    """
    角色列表
    :param role_status:
    :param pageSize:
    :param current:
    :param role_name:
    :param create_time:
    :return:
    """
    query: dict = {}
    if role_name:
        query.setdefault("role_name", role_name)
    if role_status is not None:
        query.setdefault("role_status", role_status)
    if create_time:
        query.setdefault("create_time__range", create_time)

    role = Role.annotate(key=F("id")).filter(**query).all()
    # 总数
    total = await role.count()
    # 查询
    data = (
        await role.limit(pageSize)
        .offset(pageSize * (current - 1))
        .order_by("-create_time")
        .values(
            "key",
            "id",
            "role_name",
            "role_status",
            "role_desc",
            "create_time",
            "update_time",
        )
    )
    return res_antd(code=True, data=data, total=total)
