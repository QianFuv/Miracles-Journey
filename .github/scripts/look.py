import argparse
from pan123 import pan123openAPI

def list_folders_recursive(api, parent_id=0, indent=0, cache=None):
    """
    递归列出所有目录结构
    """
    if cache is None:
        cache = set()
    
    if parent_id in cache:
        return
    cache.add(parent_id)

    last_file_id = None
    while True:
        params = {"parentFileId": parent_id, "limit": 100}
        if last_file_id:
            params["lastFileId"] = last_file_id
        
        res = api.file.list_v2(**params)
        # 添加API响应验证
        if not res.success:
            print(f"获取目录 {parent_id} 失败: {res.message}", flush=True)
            return
        if "fileList" not in res.data:  # 验证数据结构
            print(f"目录 {parent_id} 返回数据异常: {res.data}", flush=True)
            return

        # 添加根目录标识
        if parent_id == 0 and indent == 0:
            print("- 根目录 (ID: 0)", flush=True)

        has_folders = False
        for item in res.data["fileList"]:
            if item["type"] == 1:
                has_folders = True
                print("  " * indent + f"- {item['filename']} (ID: {item['fileId']})", flush=True)
                list_folders_recursive(api, item["fileId"], indent + 1, cache)
        
        # 提示空目录
        if not has_folders and indent == 0 and parent_id == 0:
            print("（根目录下没有文件夹）", flush=True)

        # 修复分页逻辑
        last_file_id = res.data.get("lastFileId")
        if last_file_id in (-1, None, "") or len(res.data["fileList"]) < params["limit"]:
            break

def main():
    parser = argparse.ArgumentParser(description="列出123云盘所有目录结构及ID")
    parser.add_argument("--client_id", required=True, help="开发者客户端ID")
    parser.add_argument("--client_secret", required=True, help="开发者客户端密钥")
    args = parser.parse_args()

    pan = pan123openAPI(args.client_id, args.client_secret)
    token_res = pan.refresh_access_token()
    # 增强认证提示
    if not token_res.success:
        print(f"认证失败: {token_res.message}（请检查client_id和client_secret）", flush=True)
        return
    else:
        print("认证成功，开始遍历目录...", flush=True)

    print("\n目录结构:")
    list_folders_recursive(pan)

if __name__ == "__main__":
    main()