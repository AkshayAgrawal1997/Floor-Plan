import xml.etree.ElementTree as ET
import cv2
import numpy as np


#root = ET.fromstring(country_data_as_string)



def array_objects(filename,new_filename):
	count=0
	im = cv2.imread(filename)
	tree = ET.parse(new_filename)
	root = tree.getroot()
	print root.tag
	for child in root:
		print child.tag, child.attrib



	arr = []

	for y in root.findall('ov'):
		for z in y.findall('o'):
			for u in z.findall('gom.std.OSymbol'):
				x0=int(float(u.get('x0')));
				x1=int(float(u.get('x1')));
				y0=int(float(u.get('y0')));
				y1=int(float(u.get('y1')));
				label=u.get('label');
				direction=u.get('direction');
				#im = cv2.drawContours(im,[box],0,(0,0,255),2)
				cv2.rectangle(im,(x0,y0),(x1,y1),(0,255,0),2);
				cv2.putText(im,label, (x0,y0), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255))
				count=count+1
				arr.append(label)

				#cv2.putText(im,direction, (x1,y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255))
				#print x0

	for y in root.findall('av'):
		for z in y.findall('a'):
			for u in z.findall('gom.std.OSymbol'):
				x0=int(float(u.get('x0')));
				x1=int(float(u.get('x1')));
				y0=int(float(u.get('y0')));
				y1=int(float(u.get('y1')));
				label=u.get('label');
				direction=u.get('direction');
				#im = cv2.drawContours(im,[box],0,(0,0,255),2)
				cv2.rectangle(im,(x0,y0),(x1,y1),(0,255,0),2);
				cv2.putText(im,label, (x0,y0), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255))
				count=count+1
				arr.append(label)

				#cv2.putText(im,direction, (x1,y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255))


				#print x0

	# print count
	# print arr
	arr1=set(arr)
	# print arr1
	# print len(arr1)
	ua=[]
	k=0
	for e in arr1:
		ua.append(e)
		k=k+1
	# print ua
	return ua,len(ua),arr
#cv2.imshow("image",im)
# cv2.imwrite("bounded_image1.tiff",im)
# cv2.imshow("image",im)
# cv2.waitKey(0)
# cv2.destroyAllWindows()