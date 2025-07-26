#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import os
import re
import argparse
from pathlib import Path

def get_staged_files(repo_path=None):
    """获取git已暂存的文件列表"""
    try:
        cmd = ['git', 'diff', '--cached', '--name-only']
        if repo_path:
            cmd.extend(['-C', repo_path])
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip().split('\n') if result.stdout.strip() else []
    except subprocess.CalledProcessError as e:
        print(f"获取git暂存文件失败: {e}")
        return []
    except FileNotFoundError:
        print("错误: 未找到git命令，请确保git已安装并在PATH中")
        return []

def extract_name_from_toml(file_path):
    """从TOML文件中提取name字段的值"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        for line in content.split('\n'):
            line = line.strip()
            if not line.startswith('name'):
                continue
            
            # 匹配 name = "..." (双引号，内部可以包含单引号)
            double_quote_pattern = r'^\s*name\s*=\s*"([^"]*)"'
            match = re.match(double_quote_pattern, line)
            if match:
                return match.group(1)
            
            # 匹配 name = '...' (单引号，内部的单引号需要转义)
            single_quote_pattern = r"^\s*name\s*=\s*'([^']*)'"
            match = re.match(single_quote_pattern, line)
            if match:
                return match.group(1)
            
            # 匹配三重引号的情况 (虽然在name字段中不常见，但为了完整性)
            triple_quote_pattern = r'^\s*name\s*=\s*"""([^"]*?)"""'
            match = re.match(triple_quote_pattern, line, re.DOTALL)
            if match:
                return match.group(1)
        
        return None
    except Exception as e:
        print(f"读取文件 {file_path} 失败: {e}")
        return None

def main():
    """主函数"""
    # 设置命令行参数
    parser = argparse.ArgumentParser(
        description='从Git已暂存的.pw.toml文件中提取name字段并用中文顿号连接输出'
    )
    parser.add_argument(
        'repo_path', 
        nargs='?', 
        default=None,
        help='Git仓库路径（可选，默认为当前目录）'
    )
    parser.add_argument(
        '-r', '--repo',
        dest='repo_path_flag',
        help='Git仓库路径（使用-r参数指定）'
    )
    
    args = parser.parse_args()
    
    # 确定仓库路径
    repo_path = args.repo_path or args.repo_path_flag or os.getcwd()
    repo_path = os.path.abspath(repo_path)
    
    print(f"使用Git仓库路径: {repo_path}")
    
    # 检查路径是否存在
    if not os.path.exists(repo_path):
        print(f"错误: 路径 {repo_path} 不存在")
        return
    
    # 检查是否在git仓库中
    if not os.path.exists(os.path.join(repo_path, '.git')):
        # 尝试使用git命令检查
        try:
            result = subprocess.run(
                ['git', '-C', repo_path, 'rev-parse', '--git-dir'], 
                capture_output=True,
                check=True
            )
        except subprocess.CalledProcessError:
            print(f"错误: {repo_path} 不是git仓库")
            return
    
    # 获取已暂存的文件
    staged_files = get_staged_files(repo_path)
    
    if not staged_files:
        print("没有找到已暂存的文件")
        return
    
    # 筛选出.pw.toml文件
    pw_toml_files = [f for f in staged_files if f.endswith('.pw.toml')]
    
    if not pw_toml_files:
        print("没有找到已暂存的.pw.toml文件")
        return
    
    print(f"找到 {len(pw_toml_files)} 个已暂存的.pw.toml文件:")
    for file in pw_toml_files:
        print(f"  - {file}")
    print()
    
    # 提取name字段
    names = []
    for file_path in pw_toml_files:
        # 构建完整的文件路径
        full_path = os.path.join(repo_path, file_path)
        if os.path.exists(full_path):
            name = extract_name_from_toml(full_path)
            if name:
                names.append(name)
                print(f"从 {file_path} 提取到: {name}")
            else:
                print(f"警告: 在 {file_path} 中未找到name字段")
        else:
            print(f"警告: 文件 {file_path} 不存在")
    
    # 输出结果
    if names:
        result = "、".join(names)
        print(f"\n提取到的所有name值 (共{len(names)}个):")
        print(result)
    else:
        print("\n未提取到任何name值 (0个)")

if __name__ == "__main__":
    main()