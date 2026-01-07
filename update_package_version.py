import os
import json
import re
from pathlib import Path

# 定义要更新的版本
VERSION_MAP = {
    r'gradio==6\.1\.0': 'gradio==6.2.0',
    r'langchain==1\.1\.3': 'langchain==1.2.0',
    r'langchain-openai==1\.1\.3': 'langchain-openai==1.1.6',
}

def update_ipynb_file(file_path):
    """更新单个ipynb文件中的依赖版本"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        modified = False
        
        # 遍历所有cell
        for cell in notebook.get('cells', []):
            if cell['cell_type'] == 'code':
                source = cell.get('source', [])
                
                # source 可能是字符串或列表
                if isinstance(source, list):
                    source_str = ''.join(source)
                else:
                    source_str = source
                
                # 检查并替换版本
                updated_source = source_str
                for old_pattern, new_version in VERSION_MAP.items():
                    updated_source = re.sub(old_pattern, new_version, updated_source)
                
                if updated_source != source_str:
                    modified = True
                    # 更新cell中的source
                    if isinstance(source, list):
                        cell['source'] = [updated_source]
                    else:
                        cell['source'] = updated_source
        
        # 如果有修改，保存文件
        if modified:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(notebook, f, ensure_ascii=False, indent=1)
            return True
        return False
    
    except Exception as e:
        print(f"❌ 处理文件失败: {file_path}")
        print(f"   错误信息: {e}")
        return False

def main():
    """主函数，遍历所有ipynb文件"""
    base_path = Path(r'D:\课件')  # 根据你的路径修改
    
    if not base_path.exists():
        print(f"❌ 路径不存在: {base_path}")
        return
    
    ipynb_files = list(base_path.rglob('*.ipynb'))
    
    if not ipynb_files:
        print("❌ 没有找到任何 .ipynb 文件")
        return
    
    print(f"🔍 找到 {len(ipynb_files)} 个 ipynb 文件\n")
    print("开始更新版本号...")
    print("-" * 60)
    
    updated_count = 0
    failed_count = 0
    
    for file_path in sorted(ipynb_files):
        relative_path = file_path.relative_to(base_path)
        
        if update_ipynb_file(file_path):
            print(f"✅ 已更新: {relative_path}")
            updated_count += 1
        else:
            # 检查是否实际没有需要更新的内容
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                if any(pattern in content for pattern in ['gradio==6.1.0', 'langchain==1.1.3', 'langchain-openai==1.1.3']):
                    failed_count += 1
                else:
                    print(f"⏭️  跳过: {relative_path} (无需更新)")
    
    print("-" * 60)
    print(f"\n✨ 更新完成!")
    print(f"   成功更新: {updated_count} 个文件")
    if failed_count > 0:
        print(f"   更新失败: {failed_count} 个文件")

if __name__ == '__main__':
    main()