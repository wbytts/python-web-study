安装：`pip install pipenv`

初始化：`pipenv install`


指定一个版本的python创建环境：`pipenv --python 3.6`
> 需要注意，这里指定的Python必须是系统已经安装的、可以在环境变量中搜索到的版本号，如果指定未安装的版本，会提示错误


安装指定的包（不管是否激活了虚拟环境）：`pipenv install xxx`
只安装在开发环境中：`pipenv install --dev requests --three`
进入虚拟环境命令行：`pipenv shell`
查看安装的包及其依赖关系：`pipenv graph`
使用配置的环境运行py文件：`pipenv run python xxx.py`
生成requirements.txt文件(--dev可选)：`pipenv lock -r [--dev] > requirements.txt`
通过requirements.txt文件安装包：`pipenv install -r requirements.txt`
删除包：`pipenv uninstall 包名`
删除所有包：`pipenv uninstall --all`
列出虚拟环境的Python可执行文件（解释器信息）：`pipenv --py`
列出虚拟环境路径（虚拟环境信息）：`pipenv --venv`
列出本地工程路径（目录信息）：`pipenv --where`
生成lockfile：`pipenv lock`
将Pipfile和Pipfile.lock文件里面的包导出为requirements.txt文件：`pipenv lock -r`
检查安全漏洞：`pipenv check`
卸载Pipfile.lock没有指定的包：`pipenv clean`
指定源安装：`pipenv install --pypi-mirror 镜像地址`
安装的时候跳过lock步骤：添加 `--skip-lock` 选项



常用环境变量：
- `PIPENV_VENV_IN_PROJECT`：设置了这个(一般设置1即可），就会把虚拟环境放在项目下的 `.venv` 文件夹里，忽略其他配置
- `WORKON_HOME`：定义本地电脑默认的虚拟环境存放位置
- `PIPENV_TIMEOUT`：环境设置超时时间
- `PIPENV_INSTALL_TIMEOUT`：安装依赖的超时时间
- `PIPENV_IGNORE_VIRTUALENVS`：设为1表示忽略venv
- `PIPENV_VERBOSITY`:设为 -1 则不显示警告信息

Pipfile文件：
- `[[source]]`：配置项目里下载依赖的源配置
  - `url`：下载依赖的地址（通常是pip源）
  - `verify_ssl`：是否验证SSL
  - `name`：源的名称，通常是 pypi
- `[packages]`：项目用到的包
- `[dev-packages]`：项目里仅在开发时用到的包
- `[requires]`：需要的其他内容


`.env` 文件：可以设置一些环境变量，在程序开发的时候模拟环境变量；pipenv也可以自动加载.env文件
```py
import os
os.environ['环境变量名称']
```



