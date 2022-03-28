import sys
sys.stdin = open('/Users/yonggeonlee/Desktop/development/drageon/practice_coding/inflearn/input.txt', 'rt')
blocks = [list(map(int, input().split())) for _ in range(7)]
# print(blocks)

def check_rotation(a) :
    cnt = 0 
    for i in range(7):
        # tmp = []
        for j in range(2,5):
            print(i, j)
            if blocks[i][j-2 : j+3] == blocks[i][j-2 : j+3][::-1]:
                cnt += 1
                print(blocks[i][j-2 : j+3], blocks[i][j-2 : j+3][::-1])
    for i in range(7):
        tmp = []
        for j in range(7):
            tmp.append(blocks[j][i])
        for k in range(2,5):
            if tmp[k-2 : k+3] == tmp[k-2:k+3][::-1]:
                cnt+=1
                print(tmp[k-2 : k+3], tmp[k-2:k+3][::-1])
        # print(tmp)
        # if blocks[j-2 : j+3] == tmp[j-2 : j+3][::-1]:
        #     cnt += 1
        #         # print(blocks[i][j-2 : j+3], blocks[i][j-2 : j+3][::-1])
    # for i in range(7):
    #     for j in range(2,5):
    #         print(i, j)
    #         if blocks[j][i-2: i+3] == blocks[j][i-2 : i+3][::-1]:
    #             cnt += 1
    #             print(blocks[j][i-2: i+3], blocks[j][i-2 : i+3][::-1])

    return cnt

b = check_rotation(blocks)
print(b)