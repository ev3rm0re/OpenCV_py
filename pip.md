## pip 卸载所有包命令

```bash
pip freeze > requirements.txt # 导出所有安装的包
pip uninstall -r requirements.txt -y
```

## pip 安装依赖命令

```bash
pip install -r requirements.txt
```