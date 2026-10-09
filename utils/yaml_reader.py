import yaml
#读YAML 文件的读取数据工具
def read_yaml(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)