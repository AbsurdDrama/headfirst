

# TODO : 最原始写法 try / except / finally
# try:
#     man_file = open('man_data.txt', 'w')
#     other_file = open('other_data.txt', 'w')
#     print(man, file=man_file)
#     print(other, file=other_file)
# except IOError:
#     print('IOError was break.')
# finally:
#     if 'man_file' in locals():
#         man_file.close()
#     if 'other_file' in locals():
#         other_file.close()

# TODO : 利用 with 保证打开文件的关闭
# try:
#     with open('man_data2.txt', 'w') as man_file2, open('other_data2.txt', 'w') as other_file2:
#         print(man, file=man_file2)
#         print(other, file=other_file2)
# except IOError as err:
#     print('IOError:2 ' + str(err))
#
