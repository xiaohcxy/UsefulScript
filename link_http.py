def process_url(url):
    #添加http请求头
    http_url = "http://" + url

    #添加https请求头
    https_url = "https://" + url

    return http_url, https_url

#按行读取txt文件
txt_path = input("输入txt文件路径（绝对路径）：")
http_address = []
https_address = []

with open(txt_path, "r") as file:
    for line in file:
        #去除行尾的换行符
        line = line.strip()

        #处理每行数据并添加到相应的列表
        http_addr, https_addr = process_url(line)
        http_address.append(http_addr)
        https_address.append(https_addr)

#将结果写入txt文件
with open("http_address.txt", "w") as http_file:
    for address in http_address:
        http_file.write(address + "\n")

with open("https_address.txt", "w") as https_file:
    for address in https_address:
        https_file.write(address + "\n")