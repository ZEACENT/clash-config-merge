import yaml
from pathlib import Path

def merge_yaml_files(amatrix_file, baiyue_file, zeacent_file):
    # Check if files exist before proceeding
    for file in [amatrix_file, baiyue_file, zeacent_file]:
        if not Path(file).is_file():
            print(f"Error: File not found: {file}")
            return
    
    with open(amatrix_file, 'r', encoding='utf-8') as f:
        amatrix_data = yaml.safe_load(f)
    
    with open(baiyue_file, 'r', encoding='utf-8') as f:
        baiyue_data = yaml.safe_load(f)

    with open(zeacent_file, 'r', encoding='utf-8') as f:
        zeacent_data = yaml.safe_load(f)
    
    merged_proxies = amatrix_data['proxies'] + baiyue_data['proxies']
    proxy_names = [proxy['name'] for proxy in merged_proxies]
    
    zeacent_data['proxies'] = merged_proxies
    zeacent_data['group-temp-selector']['proxies'] = proxy_names
    
    with open(zeacent_file, 'w', encoding='utf-8') as f:
        yaml.dump(zeacent_data, f, allow_unicode=True, sort_keys=False)
    
    print(f"Merge done: {zeacent_file}")

if __name__ == "__main__":
    amatrix_file = "amatrixap.yaml"
    baiyue_file = "白月光.yaml"
    zeacent_file = "zeacent.yaml"
    
    merge_yaml_files(amatrix_file, baiyue_file, zeacent_file)