def canPlaceFlowers(flowerbed=[1,0,0,0,1], n=1):
    count = 0
    zeros = 0

    # Look at each space in flowerbed
    for i in range(0, len(flowerbed)):

        # First and last index needs one less zero because no neighbor
        if i == 0:
            zeros += 1

        if i == len(flowerbed) - 1:
            zeros += 1

        # Restart the zeros count
        if flowerbed[i] == 1:
            zeros = 0

        # Increment zeros count
        else:
            zeros += 1

            # If zeros count is 3 then a flower can go there
            if zeros >= 3:
                count += 1
                zeros = 1

    # Number flower spaces available is enough to accomodate n flowers
    if count >= n:
        return True
    else:
        return False
print(canPlaceFlowers())
