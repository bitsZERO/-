import re


def reg_search(text, regex_list):
    results = []
    for regex_dict in regex_list:
        result_dict = {}
        for key, pattern in regex_dict.items():
            match = re.search(pattern, text, re.DOTALL)  # 匹配的数据
            if match:  # 进行关键字的提取判断
                if key == '换股期限':
                    dates = re.findall(r'(\d{4}) 年 (\d{1,2}) 月 (\d{1,2}) 日', match.group(1))
                    formatted_dates = [f'{date[0]}-{int(date[1]):02d}-{int(date[2]):02d}' for date in dates]
                    result_dict[key] = formatted_dates
                else:
                    result_dict[key] = match.group(1)
            else:
                result_dict[key] = None
        results.append(result_dict)
    return results


# 测试例子
text = '''
标的证券：本期发行的证券为可交换为发行人所持中国长江电力股份有限公司股票（股票代码：600900.SH，股票简称：长江电力）的可交换公司债券。
换股期限：本期可交换公司债券换股期限自可交换公司债券发行结束之日满 12 个月后的第一个交易日起至可交换债券到期日止，即 2023 年 6 月 2 日至 2027 年 6 月 1 日止。
'''

regex_list = [
    {
        '标的证券': r'股票代码：([A-Z0-9.]+)',
        '换股期限': r'换股期限：.+?(\d{4}.+日)',
    }
]

results = reg_search(text, regex_list)
print(results)
