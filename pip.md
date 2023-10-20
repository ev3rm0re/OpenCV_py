## pip 卸载所有包命令

```bash
pip freeze > requirements.txt # 导出所有安装的包
pip uninstall -r requirements.txt -y
```