SET NAMES utf8mb4;

SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------

-- Table structure for access

-- ----------------------------

DROP TABLE IF EXISTS `access`;

CREATE TABLE
    `access` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `create_time` datetime(6) NOT NULL DEFAULT current_timestamp(6) COMMENT '创建时间',
        `update_time` datetime(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6) COMMENT '更新时间',
        `access_name` varchar(15) NOT NULL COMMENT '权限名称',
        `parent_id` int(11) NOT NULL DEFAULT 0 COMMENT '父id',
        `scopes` varchar(255) NOT NULL COMMENT '权限范围标识',
        `access_desc` varchar(255) DEFAULT NULL COMMENT '权限描述',
        `menu_icon` varchar(255) DEFAULT NULL COMMENT '菜单图标',
        `is_check` tinyint(1) NOT NULL DEFAULT 0 COMMENT '是否验证权限 True为验证 False不验证',
        `is_menu` tinyint(1) NOT NULL DEFAULT 0 COMMENT '是否为菜单 True菜单 False不是菜单',
        PRIMARY KEY (`id`),
        UNIQUE KEY `scopes` (`scopes`)
    ) ENGINE = InnoDB AUTO_INCREMENT = 14 DEFAULT CHARSET = utf8mb4 COMMENT = '权限表';

-- ----------------------------

-- Records of access

-- ----------------------------

BEGIN;

INSERT INTO `access`
VALUES (
        1,
        '2022-05-18 18:28:15.699736',
        '2022-05-18 18:28:15.699771',
        '用户中心',
        0,
        'user',
        NULL,
        NULL,
        0,
        1
    );

INSERT INTO `access`
VALUES (
        2,
        '2022-05-18 18:28:55.162023',
        '2022-05-18 18:28:55.162070',
        '用户管理',
        1,
        'user_m',
        NULL,
        NULL,
        0,
        1
    );

INSERT INTO `access`
VALUES (
        3,
        '2022-05-18 18:31:48.630306',
        '2022-05-18 18:31:48.630354',
        '角色管理',
        1,
        'role_m',
        NULL,
        NULL,
        0,
        1
    );

INSERT INTO `access`
VALUES (
        4,
        '2022-05-18 18:32:45.768538',
        '2022-05-19 07:27:43.328990',
        '用户查询',
        2,
        'user_query',
        NULL,
        NULL,
        1,
        0
    );

INSERT INTO `access`
VALUES (
        5,
        '2022-05-18 18:33:05.634450',
        '2022-05-18 18:33:05.634498',
        '用户添加',
        2,
        'user_add',
        NULL,
        NULL,
        1,
        0
    );

INSERT INTO `access`
VALUES (
        6,
        '2022-05-18 18:33:35.677990',
        '2022-05-18 18:33:35.678038',
        '用户编辑',
        2,
        'user_update',
        NULL,
        NULL,
        1,
        0
    );

INSERT INTO `access`
VALUES (
        7,
        '2022-05-18 18:33:53.455916',
        '2022-05-18 18:33:53.455964',
        '用户删除',
        2,
        'user_delete',
        NULL,
        NULL,
        1,
        0
    );

INSERT INTO `access`
VALUES (
        8,
        '2022-05-18 18:34:55.614617',
        '2022-05-19 11:32:14.861397',
        '角色分配',
        2,
        'user_role',
        NULL,
        NULL,
        1,
        0
    );

INSERT INTO `access`
VALUES (
        9,
        '2022-05-18 18:35:16.093767',
        '2022-05-19 09:15:13.190683',
        '角色查询',
        3,
        'role_query',
        NULL,
        NULL,
        1,
        0
    );

INSERT INTO `access`
VALUES (
        10,
        '2022-05-18 18:35:35.856673',
        '2022-05-19 09:14:55.453576',
        '角色添加',
        3,
        'role_add',
        NULL,
        NULL,
        1,
        0
    );

INSERT INTO `access`
VALUES (
        11,
        '2022-05-18 18:35:53.266453',
        '2022-05-19 09:14:41.721341',
        '角色编辑',
        3,
        'role_update',
        NULL,
        NULL,
        1,
        0
    );

INSERT INTO `access`
VALUES (
        12,
        '2022-05-18 18:36:27.876248',
        '2022-05-19 09:14:23.501602',
        '角色删除',
        3,
        'role_delete',
        NULL,
        NULL,
        1,
        0
    );

INSERT INTO `access`
VALUES (
        13,
        '2022-05-19 09:13:06.535110',
        '2022-05-19 09:13:56.906714',
        '权限分配',
        3,
        'role_access',
        NULL,
        NULL,
        1,
        0
    );

COMMIT;

-- ----------------------------

-- Table structure for access_log

-- ----------------------------

DROP TABLE IF EXISTS `access_log`;

CREATE TABLE
    `access_log` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `create_time` datetime(6) NOT NULL DEFAULT current_timestamp(6) COMMENT '创建时间',
        `update_time` datetime(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6) COMMENT '更新时间',
        `user_id` int(11) NOT NULL COMMENT '用户ID',
        `target_url` varchar(255) DEFAULT NULL COMMENT '访问的url',
        `user_agent` varchar(255) DEFAULT NULL COMMENT '访问UA',
        `request_params` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL COMMENT '请求参数get|post',
        `ip` varchar(32) DEFAULT NULL COMMENT '访问IP',
        `note` varchar(255) DEFAULT NULL COMMENT '备注',
        PRIMARY KEY (`id`)
    ) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COMMENT = '用户操作记录表';

-- ----------------------------

-- Records of access_log

-- ----------------------------

BEGIN;

COMMIT;

-- ----------------------------

-- Table structure for role

-- ----------------------------

DROP TABLE IF EXISTS `role`;

CREATE TABLE
    `role` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `create_time` datetime(6) NOT NULL DEFAULT current_timestamp(6) COMMENT '创建时间',
        `update_time` datetime(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6) COMMENT '更新时间',
        `role_name` varchar(15) NOT NULL COMMENT '角色名称',
        `role_status` tinyint(1) NOT NULL DEFAULT 0 COMMENT 'True:启用 False:禁用',
        `role_desc` varchar(255) DEFAULT NULL COMMENT '角色描述',
        PRIMARY KEY (`id`)
    ) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COMMENT = '角色表';

-- ----------------------------

-- Records of role

-- ----------------------------

BEGIN;

COMMIT;

-- ----------------------------

-- Table structure for role_access

-- ----------------------------

DROP TABLE IF EXISTS `role_access`;

CREATE TABLE
    `role_access` (
        `role_id` int(11) NOT NULL,
        `access_id` int(11) NOT NULL,
        KEY `role_id` (`role_id`),
        KEY `access_id` (`access_id`),
        CONSTRAINT `role_access_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`) ON DELETE CASCADE,
        CONSTRAINT `role_access_ibfk_2` FOREIGN KEY (`access_id`) REFERENCES `access` (`id`) ON DELETE CASCADE
    ) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

-- ----------------------------

-- Records of role_access

-- ----------------------------

BEGIN;

COMMIT;

-- ----------------------------

-- Table structure for system_params

-- ----------------------------

DROP TABLE IF EXISTS `system_params`;

CREATE TABLE
    `system_params` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `create_time` datetime(6) NOT NULL DEFAULT current_timestamp(6) COMMENT '创建时间',
        `update_time` datetime(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6) COMMENT '更新时间',
        `params_name` varchar(255) NOT NULL COMMENT '参数名',
        `params` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '参数',
        PRIMARY KEY (`id`),
        UNIQUE KEY `params_name` (`params_name`)
    ) ENGINE = InnoDB AUTO_INCREMENT = 3 DEFAULT CHARSET = utf8mb4 COMMENT = '系统参数表';

-- ----------------------------

-- Records of system_params

-- ----------------------------

BEGIN;

INSERT INTO `system_params`
VALUES (
        1,
        '2022-06-04 18:03:00.648479',
        '2022-06-19 09:18:35.423468',
        'wechat_auth',
        '{\"appid\":\"1111\",\"secret\":\"cabf85d20e60140a85cd\",\"redirect_uri\":\"http://auth.binkuolo.com/api/v1/wechat\",\"expire\":1}'
    );

INSERT INTO `system_params`
VALUES (
        2,
        '2022-06-07 21:42:48.946171',
        '2022-06-19 09:19:24.337017',
        'tencent_sms',
        '{\"secret_id\":\"xV4\",\"secret_key\":\"J3XHm46sOdcKejaBX7\",\"region\":\"ap-guangzhou\",\"app_id\":\"140042\",\"sign\":\"签名\",\"template_id\":\"7896\",\"expire\":10}'
    );

COMMIT;

-- ----------------------------

-- Table structure for user

-- ----------------------------

DROP TABLE IF EXISTS `user`;

CREATE TABLE
    `user` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `create_time` datetime(6) NOT NULL DEFAULT current_timestamp(6) COMMENT '创建时间',
        `update_time` datetime(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6) COMMENT '更新时间',
        `username` varchar(20) DEFAULT NULL COMMENT '用户名',
        `user_type` tinyint(1) NOT NULL DEFAULT 0 COMMENT '用户类型 True:超级管理员 False:普通管理员',
        `password` varchar(255) DEFAULT NULL,
        `nickname` varchar(255) NOT NULL DEFAULT 'binkuolo' COMMENT '昵称',
        `user_phone` varchar(11) DEFAULT NULL COMMENT '手机号',
        `user_email` varchar(255) DEFAULT NULL COMMENT '邮箱',
        `full_name` varchar(255) DEFAULT NULL COMMENT '姓名',
        `user_status` int(11) NOT NULL DEFAULT 0 COMMENT '0未激活 1正常 2禁用',
        `header_img` varchar(255) DEFAULT NULL COMMENT '头像',
        `sex` int(11) DEFAULT 0 COMMENT '0未知 1男 2女',
        `remarks` varchar(30) DEFAULT NULL COMMENT '备注',
        `client_host` varchar(19) DEFAULT NULL COMMENT '访问IP',
        PRIMARY KEY (`id`)
    ) ENGINE = InnoDB AUTO_INCREMENT = 2 DEFAULT CHARSET = utf8mb4 COMMENT = '用户表';

-- ----------------------------

-- Records of user

-- ----------------------------

BEGIN;

INSERT INTO `user`
VALUES (
        1,
        '2022-05-18 18:25:56.776176',
        '2022-06-19 09:04:35.791494',
        'admin',
        1,
        '$pbkdf2-sha256$29000$TYnxfk.pNYZwLgXA2DsHgA$8x2oHJzqMjATdVnHIO86DsU3xhQ7IzvIB.1H8tDyHpQ',
        '冰阔落',
        '19391008993',
        'binkuolo@163.com',
        NULL,
        1,
        'https://thirdwx.qlogo.cn/mmopen/vi_32/gTJ63Ml8FDvibSWh4qibP64T9t6aHCA5eUUB9EFjBKIAzFHG2q8K8fWbRWrAOWvGZFZraSB7Hx278POsD5YSPduw/132',
        0,
        'string',
        NULL
    );

COMMIT;

-- ----------------------------

-- Table structure for user_role

-- ----------------------------

DROP TABLE IF EXISTS `user_role`;

CREATE TABLE
    `user_role` (
        `user_id` int(11) NOT NULL,
        `role_id` int(11) NOT NULL,
        KEY `user_id` (`user_id`),
        KEY `role_id` (`role_id`),
        CONSTRAINT `user_role_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE,
        CONSTRAINT `user_role_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`) ON DELETE CASCADE
    ) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

-- ----------------------------

-- Records of user_role

-- ----------------------------

BEGIN;

COMMIT;

-- ----------------------------

-- Table structure for user_wechat

-- ----------------------------

DROP TABLE IF EXISTS `user_wechat`;

CREATE TABLE
    `user_wechat` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `create_time` datetime(6) NOT NULL DEFAULT current_timestamp(6) COMMENT '创建时间',
        `update_time` datetime(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6) COMMENT '更新时间',
        `city` varchar(255) DEFAULT NULL COMMENT '城市',
        `country` varchar(255) DEFAULT NULL COMMENT '国家',
        `headimgurl` varchar(255) DEFAULT NULL COMMENT '微信头像',
        `nickname` varchar(255) DEFAULT NULL COMMENT '微信昵称',
        `openid` varchar(255) NOT NULL COMMENT 'openid',
        `unionid` varchar(255) DEFAULT NULL COMMENT 'unionid',
        `province` varchar(255) DEFAULT NULL COMMENT '省份',
        `sex` int(11) DEFAULT NULL COMMENT '性别',
        `user_id` int(11) NOT NULL,
        PRIMARY KEY (`id`),
        UNIQUE KEY `openid` (`openid`),
        UNIQUE KEY `user_id` (`user_id`),
        UNIQUE KEY `unionid` (`unionid`),
        CONSTRAINT `fk_user_wec_user_a1775abb` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE
    ) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COMMENT = '用户微信';

-- ----------------------------

-- Records of user_wechat

-- ----------------------------

BEGIN;

COMMIT;

SET FOREIGN_KEY_CHECKS = 1;