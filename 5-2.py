# 불리언 2nd
# 여러줄 주석  Shift + Alt + A
# 한줄한줄 Ctrl + /

x = 5

# 1)
if x > 3:                    # x 가 3보다 크면 Hello라고 출력
    print("Hello","\n")


# 2)
if x > 7:
    print("Hello","\n")      # x가 7보다 크면 Hello라고 출력하고
else:                        # 그게 아니라면
    print("Hi","\n")         # Hi라고 출력해라


# 3)
if x > 7:
    print("Hello","\n")      # x가 7보다 큰지 보구
elif x == 3:                 # x가 3인지 보구   else if
    print("Bye","\n")
else:                        # 그게 아니면
    print("Hi","\n")         # Hi로 간다.
