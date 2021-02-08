import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = plt.imread('4.ppm')
# plt.imshow(img[:, :, 1])
# plt.show()
img_hight=img.shape[0]
img_widht=img.shape[1]

# print(img_hight)
# print(img_widht)

r = img[:, :, 0]
g = img[:, :, 1]
b = img[:, :, 2]
# print(np.shape(U_r))
# print(np.shape(V_r))
num_components =900
U_r, s_r, V_r = np.linalg.svd(r, full_matrices=True)
temp_r=np.dot(U_r[:, :num_components],np.diag(s_r[:num_components]))
reconstruct_r=np.dot(temp_r,V_r[:num_components, :])

U_g, s_g, V_g = np.linalg.svd(g, full_matrices=True)
temp_g=np.dot(U_g[:, :num_components],np.diag(s_g[:num_components]))
reconstruct_g=np.dot(temp_g,V_g[:num_components, :])

U_b, s_b, V_b = np.linalg.svd(b, full_matrices=True)
temp_b=np.dot(U_b[:, :num_components],np.diag(s_b[:num_components]))
reconstruct_b=np.dot(temp_b,V_b[:num_components, :])


img_c=np.zeros((img_hight,img_widht,3))


for i in range(img_hight):
    for j in  range(img_widht):
        img_c[i,j,0]=reconstruct_r[i,j]
        img_c[i,j,1]=reconstruct_g[i,j]
        img_c[i,j,2]=reconstruct_b[i,j]



# im_RGB = np.concatenate((reconstruct_r, reconstruct_g, reconstruct_b), axis=1)

# rgb = np.dstack((reconstruct_r,reconstruct_g,reconstruct_b))
plt.imshow(img_c.astype('uint8'))
plt.show()
