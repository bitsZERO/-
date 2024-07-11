import requests
import pandas as pd
import json
url = 'https://iftp.chinamoney.com.cn/ags/ms/cm-u-bond-md/BondMarketInfoListEN'
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}
data = {
    "pageNo": 1,
    "pageSize": 15,
    "bondType": 100001,
    "issueYear": 2023,
}

res = requests.post(url=url, headers=headers, data=data, verify=False)
# 在请求时发现网站的SSL有问题，无法请求到，CA证书
print(res)

# data = res   #
# 构建DataFrame
# df = pd.DataFrame(data, columns=['ISIN', 'Bond Code', 'Issuer', 'Bond Type', 'Issue Date', 'Latest Rating'])
#
# # 保存为CSV文件
# df.to_csv('treasury_bonds_2023.csv', index=False, encoding='utf-8')
#
# print("数据已保存为 treasury_bonds_2023.csv")
# print(res)
# print(res.status_code)
