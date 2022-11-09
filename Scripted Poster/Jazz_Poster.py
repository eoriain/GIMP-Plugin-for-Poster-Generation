# !/usr/bin/env python

from gimpfu import *

def jazz_poster(file1, file2, file3, file4, file5, file6, file7, str1, str2, str3, str4, font1, font2):
       # make a new image
       posterW, posterH = 2480, 3508
       posterImage = gimp.Image(posterW, posterH, RGB)
       gimp.Display(posterImage)
       gimp.message("new image created")
       
       # make the background colours
       bColor = gimpcolor.RGB(90, 21, 3)
       fColor = gimpcolor.RGB(100, 92, 20)
       gimp.set_background(bColor)
       gimp.set_foreground(fColor)
       gimp.message("b and f colors made")

       # make background
       backLayer = gimp.Layer(posterImage, "background",posterW, posterH, RGB_IMAGE, 100, NORMAL_MODE)
       posterImage.add_layer(backLayer)
       pdb.gimp_drawable_fill(backLayer, 1)
       gimp.message("background made")

       # make image 1 - load, scale, copy, make_layer, paste, anchor, translate
       backgroundImage = pdb.file_jpeg_load(file1, file1)
       pdb.gimp_image_scale(backgroundImage, 728, 410)
       pdb.gimp_edit_copy(backgroundImage.layers[0])
       layer1 = gimp.Layer(posterImage, "backgroundImage",728, 410, RGB_IMAGE, 100, NORMAL_MODE)
       posterImage.add_layer(layer1)
       floatingLayer = pdb.gimp_edit_paste(layer1, False)
       pdb.gimp_floating_sel_anchor(floatingLayer)
       layer1.translate(875, 1550)
       pdb.gimp_layer_scale(layer1, 3550, 2550, 1)
       pdb.gimp_item_transform_rotate(layer1, 1.55,1, 0, 0)
       gimp.message("Background made")

       # make image 2 - load, scale, copy, make_layer, paste, anchor, translate, scale and rotate
       bloomBackImage = pdb.file_png_load(file2, file2)
       pdb.gimp_image_scale(bloomBackImage, 446, 280)
       pdb.gimp_edit_copy(bloomBackImage.layers[0])
       layer2 = gimp.Layer(posterImage, "bloomBackImage", 446, 280, RGBA_IMAGE, 100, NORMAL_MODE)
       posterImage.add_layer(layer2)
       floatingLayer = pdb.gimp_edit_paste(layer2, False)
       pdb.gimp_floating_sel_anchor(floatingLayer)
       layer2.translate(3*posterW/4, 2*posterH/9)
       pdb.gimp_layer_scale(layer2, 2676, 1680, 1)
       pdb.gimp_item_transform_rotate(layer2, 5.2, 1, 0, 0)
       gimp.message("Bloom Back made")

       # make image 3 - load, scale, copy, make_layer, paste, anchor, translate, scale and rotate
       corkImage = pdb.file_png_load(file3, file3)
       pdb.gimp_image_scale(corkImage, 418, 179)
       pdb.gimp_edit_copy(corkImage.layers[0])
       layer3 = gimp.Layer(posterImage, "corkImage", 418, 179, RGBA_IMAGE, 100, NORMAL_MODE)
       posterImage.add_layer(layer3)
       floatingLayer = pdb.gimp_edit_paste(layer3, False)
       pdb.gimp_floating_sel_anchor(floatingLayer)
       layer3.translate(posterW/3, 4*posterH/9)
       pdb.gimp_layer_scale(layer3, 1574, 857, 1)
       pdb.gimp_item_transform_rotate(layer3, 1.1, 1, 0, 0)
       gimp.message("Cork made")

       # make image 4 - load, scale, copy, make_layer, paste, anchor, translate and scale
       logoImage = pdb.file_png_load(file4, file4)
       pdb.gimp_image_scale(logoImage, 425, 248)
       pdb.gimp_edit_copy(logoImage.layers[0])
       layer4 = gimp.Layer(posterImage, "logoImage", 425, 248, RGBA_IMAGE, 100, NORMAL_MODE)
       posterImage.add_layer(layer4)
       floatingLayer = pdb.gimp_edit_paste(layer4, False)
       pdb.gimp_floating_sel_anchor(floatingLayer)
       layer4.translate(3*posterW/10, posterH/9)
       pdb.gimp_layer_scale(layer4, 1660, 952, 1)
       gimp.message("Logo made")

       # make image 5 - load, scale, copy, make_layer, paste, anchor, translate, scale and rotate
       bloomFrontImage = pdb.file_png_load(file5, file5)
       pdb.gimp_image_scale(bloomFrontImage, 446, 280)
       pdb.gimp_edit_copy(bloomFrontImage.layers[0])
       layer5 = gimp.Layer(posterImage, "bloomFrontImage", 446, 280, RGBA_IMAGE, 100, NORMAL_MODE)
       posterImage.add_layer(layer5)
       floatingLayer = pdb.gimp_edit_paste(layer5, False)
       pdb.gimp_floating_sel_anchor(floatingLayer)
       layer5.translate(3*posterW/4, 2*posterH/9)
       pdb.gimp_layer_scale(layer5, 2676, 1680, 1)
       pdb.gimp_item_transform_rotate(layer5, 5.2, 1, 0, 0)
       gimp.message("Bloom Front made")

       # make image 6 - load, scale, copy, make_layer, paste, anchor, translate and scale
       zImage = pdb.file_png_load(file6, file6)
       pdb.gimp_image_scale(zImage, 425, 248)
       pdb.gimp_edit_copy(zImage.layers[0])
       layer6 = gimp.Layer(posterImage, "zImage", 425, 248, RGBA_IMAGE, 100, NORMAL_MODE)
       posterImage.add_layer(layer6)
       floatingLayer = pdb.gimp_edit_paste(layer6, False)
       pdb.gimp_floating_sel_anchor(floatingLayer)
       layer6.translate(3*posterW/10, posterH/9)
       pdb.gimp_layer_scale(layer6, 1660, 952, 1)
       gimp.message("Z made")

       # make image 7 - load, flip, scale, copy, make_layer, paste, anchor, translate, scale and rotate
       saxImage = pdb.file_png_load(file7, file7)
       pdb.gimp_image_flip(saxImage, 0)
       pdb.gimp_image_scale(saxImage, 486, 514)
       pdb.gimp_edit_copy(saxImage.layers[0])
       layer7 = gimp.Layer(posterImage, "saxImage", 486, 514, RGBA_IMAGE, 100, NORMAL_MODE)
       posterImage.add_layer(layer7)
       floatingLayer = pdb.gimp_edit_paste(layer7, False)
       pdb.gimp_floating_sel_anchor(floatingLayer)
       layer7.translate(posterW/4, 3*posterH/5)
       pdb.gimp_layer_scale(layer7, 2800, 3030, 1)
       pdb.gimp_item_transform_rotate(layer7, 0,1, 0, 0)
       gimp.message("Sax made")     

       # Add Text Layers - Classify the font, set the colour
       textLayer1 = pdb.gimp_text_fontname(posterImage, None, -20, 2000, str1, 100, True, 300, PIXELS, font1)
       pdb.gimp_text_layer_set_color(textLayer1, '#ffffff')
       textLayer2 = pdb.gimp_text_fontname(posterImage, None, -20, 2500, str2, 100, True, 300, PIXELS, font1)
       pdb.gimp_text_layer_set_color(textLayer2, '#ffffff')
       textLayer3 = pdb.gimp_text_fontname(posterImage, None, -20, 3000, str3, 100, True, 300, PIXELS, font1)
       pdb.gimp_text_layer_set_color(textLayer3, '#ffffff')
       textLayer4 = pdb.gimp_text_fontname(posterImage, None, 425, 2950, str4, 100, True, 411, PIXELS, font2)
       pdb.gimp_text_layer_set_color(textLayer4, '#cf0e2b')
       # Add "Bold" and "Bold Italic" to the font type in the register to add these characteristics to the text layers where applicable.       

# end filter

register(
     "python_fu_jazz_poster",
     "Jazz Poster maker",
     "Jazz Poster maker with some interface",
     "EOR",
     "@MSCIM2021",
     "2021",
     "Eoghan's Jazz Poster",
     "",
     [# add input argumenst
         (PF_FILE, "file1", "Choose Background Image", ""),
         (PF_FILE, "file2", "Choose Bloom Back Image", ""),
         (PF_FILE, "file3", "Choose Cork Image", ""),
         (PF_FILE, "file4", "Choose Logo Image", ""),
         (PF_FILE, "file4", "Choose Bloom Front Image", ""),
         (PF_FILE, "file4", "Choose Z Image", ""),
         (PF_FILE, "file7", "Choose Saxophone Image", ""),
         (PF_STRING, "str1", "Copyright Text 1", "Paint"),
         (PF_STRING, "str2", "Copyright Text 2", "The Town"),
         (PF_STRING, "str3", "Copyright Text 3", "With"),
         (PF_STRING, "str4", "Copyright Text 4", "Jazz"),
         (PF_FONT, "font1", "Copyright Font 1", "Gabriola Bold"),
         (PF_FONT, "font2", "Copyright Font 2", "Gabriola Bold Italic"),
         
     ],
     [],
     jazz_poster,
     menu = "<Image>/File/Create/EoghanORiain's Plug-in/"
)
 
main()
