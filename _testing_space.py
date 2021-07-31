height = [4, 2, 0, 3, 2, 5]


# If it starts or ends in 0, It can be removed/ignored
water = 0

for i in range(len(height) - 1):
    if i > 0:
        maxL = max(height[:i])
        maxR = max(height[i + 1:])

        if maxL > height[i] and maxR > height[i]:
            water += min(maxL, maxR) - height[i]

return water

print(water)
