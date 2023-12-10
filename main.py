from PIL import Image

def nearest_neighbour_(source_image,target_image,point):
    """
    using nearest neighbour method to zoom out image
    :param source_image: input image
    :param target_image: output image which is zoomed out by method
    :param point:
    :return: pixel of target_image corresponds to the source image
    """
    src_width,src_height=source_image.size
    target_width,target_height=target_image.size
    target_x,target_y=point

    src_x=int(target_x*src_width/target_width)
    src_y=int(target_y*src_height/target_height)

    return source_image.getpixel((src_x,src_y))

def nearest_neightbour(src_image,target_image):
    target_width,target_height=target_image.size
    for width in range(target_width):
        for height in range(target_height):
            target_pixel=nearest_neighbour_(src_image,target_image,(width,height))
            target_image.putpixel(xy=(width,height),value=target_pixel)
    return target_image


def simple_bilinear_interpolation_(source_image,target_image,point):
    """
    :param source_image: input image
    :param target_image: output image which is zoomed out by method
    :param point: 
    :return: 
    """
    src_width,src_height=source_image.size
    target_width,target_height=target_image.size
    x_target,y_target=point

    # calculate the corresponding position of target image to source image
    x_src=int(x_target*src_width/target_width)
    y_src=int(y_target*src_height/target_height)
    x1_src, y1_src = x_src, y_src
    if x1_src >= src_width - 2:
        x1_src = src_width - 2
    if y1_src >= src_height - 2:
        y1_src = src_height - 2
    x2_src, y2_src = x1_src + 1, y1_src + 1

    p11=source_image.getpixel((x1_src,y1_src))
    p12=source_image.getpixel((x1_src,y2_src))
    p21=source_image.getpixel((x2_src,y1_src))
    p22=source_image.getpixel((x2_src,y2_src))

    r = p11[0]*(x2_src-x_src)*(y2_src-y_src)+p21[0]*(x_src-x1_src)*(y2_src-y_src)+p12[0]*(x2_src-x_src)*(y_src-y1_src)+p22[0]*(x_src-x1_src)*(y_src-y1_src)
    g = p11[1]*(x2_src - x_src)*(y2_src - y_src) + p21[1]*(x_src - x1_src)*(y2_src - y_src) + p12[1]*(
        x2_src - x_src)*(y_src - y1_src) + p22[1]*(x_src - x1_src)*(y_src - y1_src)
    b = p11[2]*(x2_src - x_src)*(y2_src - y_src) + p21[2]*(x_src - x1_src)*(y2_src - y_src) + p12[2]*(
        x2_src - x_src)*(y_src - y1_src) + p22[2]*(x_src - x1_src)*(y_src - y1_src)
    return (int(r),int(g),int(b))

def simple_bilinear_interpolation(src_image,target_image):
    target_width,target_height=target_image.size
    for x in range(target_width):
        for y in range(target_height):
            target_pixel=simple_bilinear_interpolation_(src_image,target_image,(x,y))
            target_image.putpixel(xy=(x,y),value=target_pixel)
    return target_image


def bilinear_interpolation_(source_image,target_image,point):
    """
    :param source_image: input image
    :param target_image: output image which is zoomed out by method
    :param point:
    :return:
    """
    src_width,src_height=source_image.size
    target_width,target_height=target_image.size
    x_target,y_target=point

    # calculate the corresponding position of target image to source image
    x_src=int((x_target+0.5)*src_width/target_width-0.5)
    y_src=int((y_target+0.5)*src_height/target_height-0.5)
    x1_src, y1_src = x_src,y_src
    if x1_src>=src_width-2:
        x1_src=src_width-2
    if y1_src>=src_height-2:
        y1_src=src_height-2
    x2_src, y2_src = x1_src + 1, y1_src + 1

    p11=source_image.getpixel((x1_src,y1_src))
    p12=source_image.getpixel((x1_src,y2_src))
    p21=source_image.getpixel((x2_src,y1_src))
    p22=source_image.getpixel((x2_src,y2_src))

    r = p11[0]*(x2_src-x_src)*(y2_src-y_src)+p21[0]*(x_src-x1_src)*(y2_src-y_src)+p12[0]*(x2_src-x_src)*(y_src-y1_src)+p22[0]*(x_src-x1_src)*(y_src-y1_src)
    g = p11[1]*(x2_src - x_src)*(y2_src - y_src) + p21[1]*(x_src - x1_src)*(y2_src - y_src) + p12[1]*(
        x2_src - x_src)*(y_src - y1_src) + p22[1]*(x_src - x1_src)*(y_src - y1_src)
    b = p11[2]*(x2_src - x_src)*(y2_src - y_src) + p21[2]*(x_src - x1_src)*(y2_src - y_src) + p12[2]*(
        x2_src - x_src)*(y_src - y1_src) + p22[2]*(x_src - x1_src)*(y_src - y1_src)
    return (int(r),int(g),int(b))

def bilinear_interpolation(src_image,target_image):
    target_width,target_height=target_image.size
    for x in range(target_width):
        for y in range(target_height):
            target_pixel=bilinear_interpolation_(src_image,target_image,(x,y))
            target_image.putpixel(xy=(x,y),value=target_pixel)
    return target_image

def zoom_out_images(src_images,target_image_size,method="nearest_neighbour"):
    target_image=Image.new(mode='RGB',size=target_image_size,color=0)
    assert method in ("nearest_neighbour","simple_bilinear_interpolation","bilinear_interpolation"), "nearest_neighbour, simple_bilinear_interpolation or bilinear_interpolation"
    if method=="nearest_neighbour":
        nearest_neightbour(src_images,target_image)
    if method=="simple_bilinear_interpolation":
        simple_bilinear_interpolation(src_images,target_image)
    if method=="bilinear_interpolation":
        bilinear_interpolation(src_images,target_image)
    return target_image


if __name__ == '__main__':
    img=Image.open('src_images/dog01.jpg')
    target_img=zoom_out_images(src_images=img,
                    target_image_size=(int(img.width*3),int(img.height*3)),
                               method="bilinear_interpolation")
    # path_target_img="./desc_images/dog01_simple_bilinear_interpolation.jpg"
    # path_target_img = "./desc_images/dog01_nearest_neighbour.jpg"
    path_target_img = "./desc_images/dog01_bilinear_interpolation.jpg"
    target_img.save(fp=path_target_img)
    print(target_img.size)
    target_img.show()

