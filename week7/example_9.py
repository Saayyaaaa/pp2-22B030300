import os

# f = open('test.txt', 'r')
# fpath = 'test.txt'
# # print(fpath)
# print(
#     os.path.join(
#         os.getcwd(),
#         'tests',
#         fpath,
#     )
# )
os.remove('test.txt')
print(os.path.abspath(fpath))
if os.path.exists(fpath):
    os.remove(fpath)
    print('del file')