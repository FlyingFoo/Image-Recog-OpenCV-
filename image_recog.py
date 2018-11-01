import cv2
from matplotlib import pyplot as plt

# Match func; enable popup for visual feedback
def template_match(template, image, popup = True):
    template_img = cv2.imread(template)
    img = cv2.imread(image)
    w, h = template_img.shape[:-1]
    # Comparison Method
    method = eval('cv2.TM_CCOEFF_NORMED') # All comparison methods: TM_CCOEFF_NORMED; TM_SQDIFF; TM_SQDIFF_NORMED
     
    while True:
        res = cv2.matchTemplate(template_img, img, method)
        _, max_val, _, max_loc = cv2.minMaxLoc(res)
        # Threshold for match
        threshold = 0.9
        print(max_loc, max_val)
        if max_val < threshold:
            print("Match not found")
            return None, None
        else:
            # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
            top_left = max_loc
            # Find Center
            templateCenter = (top_left[0] + w/2, top_left[1] + h/2)
            # Deprecated Var
            offset = (top_left[0] + w/2 + 150, top_left[1] + h/2 + 200)
            if popup:
                if templateCenter:
                    print("Match found")
                    plt.subplot(121),plt.imshow(res)
                    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
                    plt.subplot(122),plt.imshow(img)
                    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
                    plt.suptitle(method)
                    plt.show()
            return templateCenter, img, offset

Test = template_match("testTemp.jpg","testImg.jpg") #Popup value is already set to True
